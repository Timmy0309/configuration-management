import sys
from lark import Lark, Transformer, exceptions, LarkError
import json

grammar = """
start: (const_decl)* dict

const_decl: NAME "<-" value
const_eval: "." NAME "."

value:  NUMBER | dict | const_eval

dict: "{" [pair ("," pair)*] "}"
pair: NAME ":" value

NAME: /[A-Z]+/

%import common.NUMBER
%import common.WS
%ignore WS
%ignore /\|\|.*\n/x
%ignore /--\[\[.*\]\]/sx
"""

config_parser = Lark(grammar)
constant = {}


class ConfigTransformer(Transformer):
    def __init__(self):
        super().__init__()
        self.constants = {}

    def start(self, items):
        return items[-1] if items else None

    def const_decl(self, tupl):
        name, value = tupl
        if name in self.constants:
            raise LarkError(f"Константа {name} уже объявлена")
        self.constants[name] = value
        global constant
        constant['constaint'] = self.constants

    def const_eval(self, value):
        name = value[0]
        if name not in self.constants:
            raise ValueError(f"При вычислении использована неизвестная константа по имени {name}")
        return self.constants[name]

    pair = tuple
    dict = dict

    def NUMBER(self, number):
        return int(number)

    def NAME(self, token):
        return str(token)

    def value(self, tupl):
        return tupl[0]


input_text = """
GET <- 23

HRL <- {
KEY : 12,
HR : 34
}

|| пример работы однострочного комментария

--[[ пример
работы
многострочного
комментария
]]


FOO <- .HRL.

{
Q : 12,
W : 32,
E : {
        R : .FOO., || comment
        T : 100
    }
}
"""

#input_text = sys.stdin.read()


def parse(config_parser, input_text):
    try:
        global constant
        json_parse = config_parser.parse(input_text)
        transformer = ConfigTransformer()
        parsed_data = transformer.transform(json_parse)
        if 'constaint' in constant:
            result = json.dumps(constant, indent=4)
            result += "\n" + json.dumps(parsed_data, indent=4)
        else:
            result = json.dumps(parsed_data, indent=4)
        return result
    except exceptions.UnexpectedCharacters as UnexpectedCharacters:
        raise Exception(f"Неожиданный символ: \n{str(UnexpectedCharacters)}")
    except exceptions.LarkError as LarkError:
        raise Exception(f"Ошибка при обработке:\n{str(LarkError)}")


result = parse(config_parser, input_text)

sys.stdout.write(result)
