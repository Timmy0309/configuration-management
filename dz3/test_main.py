import pytest
from lark import Lark
from main import grammar, parse, constant

@pytest.fixture(autouse=True)
def clear_globals():
    constant.clear()

def test_dict():
    content = """
    {
        KEY : 12,
        HR : 34
    }
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "KEY": 12,
    "HR": 34
}"""


def test_dict_of_dicts():
    content = """
{
Q : 12,
W : 32,
E : {
        R : 94,
        T : 100
    }
}
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "Q": 12,
    "W": 32,
    "E": {
        "R": 94,
        "T": 100
    }
}"""

def test_comment():
    content = """
    || тест однострочного комментария
    {
        KEY : 12,
        HR : 34
    }
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "KEY": 12,
    "HR": 34
}"""


def test_line_comments():
    content = """
    --[[ тест
     многострочного
     комментария
     ]]
    {
        KEY : 12,
        HR : 34
    }
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "KEY": 12,
    "HR": 34
}"""


def test_const():
    content = """
    GET <- 23
    {
        KEY : 12,
        HR : 34
    }
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "constaint": {
        "GET": 23
    }
}
{
    "KEY": 12,
    "HR": 34
}"""


def test_const_eval():
    content = """
    GET <- 23
    {
        KEY : .GET.,
        HR : 34
    }
    """
    config_parser = Lark(grammar)
    result = parse(config_parser, content)
    assert result == """{
    "constaint": {
        "GET": 23
    }
}
{
    "KEY": 23,
    "HR": 34
}"""