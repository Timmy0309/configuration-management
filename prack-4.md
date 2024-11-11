## Задача 1

На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
### код 
```
git commit
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
You have performed a fast-forward merge.
git checkout hash
git tag in
```

![Screenshot 2024-10-28 172332](https://github.com/user-attachments/assets/c5721f84-63b2-498c-ad09-c52ae1364889)


## Задача 2

Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.

### решение

![Screenshot 2024-10-28 174006](https://github.com/user-attachments/assets/977f0593-efc8-4a39-b3f2-cb475ab78634)

## Задача 3

Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

### Решение
![Screenshot 2024-11-11 172908](https://github.com/user-attachments/assets/5cae4f29-877e-4f55-8070-0cb1833631bd)

![Screenshot 2024-11-11 173411](https://github.com/user-attachments/assets/4134c675-05cf-46ee-bbdf-2ab1d5eb65f0)

![Screenshot 2024-11-11 173811](https://github.com/user-attachments/assets/bd45dba9-1444-4dcc-a30e-1c2c8053f247)

![Screenshot 2024-11-11 174252](https://github.com/user-attachments/assets/d490e6e5-1a7a-4e4e-862e-1542a4268add)

```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Mon Nov 11 17:40:41 2024 +0300
| | 
| |      add: readme.md
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Mon Nov 11 17:34:37 2024 +0300
| | 
| |     feat: info Coder 1 in readme
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Mon Nov 11 17:35:14 2024 +0300
|   
|       feat: info Coder 2 in readme
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Mon Nov 11 17:33:43 2024 +0300
| 
|      add: readme.md
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Mon Nov 11 17:32:40 2024 +0300
  
      first

```
## Задача 4
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.
### Решение

```python
import subprocess

def get_git_objects():
    objects = subprocess.check_output(["git", "rev-list", "--all", "--objects"]).decode("utf-8").splitlines()

    object_data = []

    for obj in objects:
        parts = obj.split(" ", 1)
        obj_hash = parts[0]
        path = parts[1] if len(parts) > 1 else "No path"

        try:
            obj_content = subprocess.check_output(["git", "cat-file", "-p", obj_hash]).decode("utf-8")
        except UnicodeDecodeError:
            obj_content = subprocess.check_output(["git", "cat-file", "-p", obj_hash]).decode("latin-1")

        object_data.append((obj_hash, path, obj_content))

    return object_data


def print_git_objects():
    objects = get_git_objects()
    for obj_hash, path, content in objects:
        print(f"Hash: {obj_hash}")
        print(f"Path: {path}")
        print("Content:")
        print(content)
        print("=" * 40)


if __name__ == "__main__":
    print_git_objects()

```
### Вывод
```
C:\Users\ltimo\PycharmProjects\потыкать\.venv\Scripts\python.exe C:\Users\ltimo\PycharmProjects\потыкать\main.py 
Hash: 8b2d9782ff63e7f74af34dfe7b82546b86871805
Path: No path
Content:
tree f2e7a1e630619ab7012060def50caebc22027eda
author Timophey <ltimophey06@yandex.ru> 1731337850 +0300
committer Timophey <ltimophey06@yandex.ru> 1731337850 +0300

first

========================================
Hash: f2e7a1e630619ab7012060def50caebc22027eda
Path: 
Content:
040000 tree 62755b4854d2bf6b4c838ba10ef3e61aa2e81af5	.idea
040000 tree 3ed85b759257595bbec9b0fcd2fb7f7ac2aad37c	__pycache__
100644 blob 1fa48f271c815387bb153899c5c79a29de4cacac	main.py
100644 blob daa8e18da8d44bab838d0fbf7a19176acfbc6914	test_main.py

========================================
Hash: 62755b4854d2bf6b4c838ba10ef3e61aa2e81af5
Path: .idea
Content:
100644 blob 26d33521af10bcc7fd8cea344038eaaeb78d0ef5	.gitignore
040000 tree 97824ec9b0149e48c91dce4fee530335b327c686	inspectionProfiles
100644 blob 3782dbab8ffd87fa5086293ad5e6d7e6cf545793	misc.xml
100644 blob 8feb500c56f6cb7856b0ee9588175a78a91690dd	modules.xml
100644 blob 2c80e1269497d12e018fd6afa29982e56b0fb70d	"\320\277\320\276\321\202\321\213\320\272\320\260\321\202\321\214.iml"

========================================
Hash: 26d33521af10bcc7fd8cea344038eaaeb78d0ef5
Path: .idea/.gitignore
Content:
# Default ignored files
/shelf/
/workspace.xml

========================================
Hash: 97824ec9b0149e48c91dce4fee530335b327c686
Path: .idea/inspectionProfiles
Content:
100644 blob 105ce2da2d6447d11dfe32bfb846c3d5b199fc99	profiles_settings.xml

========================================
Hash: 105ce2da2d6447d11dfe32bfb846c3d5b199fc99
Path: .idea/inspectionProfiles/profiles_settings.xml
Content:
<component name="InspectionProjectProfileManager">
  <settings>
    <option name="USE_PROJECT_PROFILE" value="false" />
    <version value="1.0" />
  </settings>
</component>
========================================
Hash: 3782dbab8ffd87fa5086293ad5e6d7e6cf545793
Path: .idea/misc.xml
Content:
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="Black">
    <option name="sdkName" value="Python 3.12 (потыкать)" />
  </component>
  <component name="ProjectRootManager" version="2" project-jdk-name="Python 3.12 (потыкать)" project-jdk-type="Python SDK" />
</project>
========================================
Hash: 8feb500c56f6cb7856b0ee9588175a78a91690dd
Path: .idea/modules.xml
Content:
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="ProjectModuleManager">
    <modules>
      <module fileurl="file://$PROJECT_DIR$/.idea/потыкать.iml" filepath="$PROJECT_DIR$/.idea/потыкать.iml" />
    </modules>
  </component>
</project>
========================================
Hash: 2c80e1269497d12e018fd6afa29982e56b0fb70d
Path: .idea/потыкать.iml
Content:
<?xml version="1.0" encoding="UTF-8"?>
<module type="PYTHON_MODULE" version="4">
  <component name="NewModuleRootManager">
    <content url="file://$MODULE_DIR$">
      <excludeFolder url="file://$MODULE_DIR$/.venv" />
    </content>
    <orderEntry type="inheritedJdk" />
    <orderEntry type="sourceFolder" forTests="false" />
  </component>
</module>
========================================
Hash: 3ed85b759257595bbec9b0fcd2fb7f7ac2aad37c
Path: __pycache__
Content:
100644 blob 74f2049539d4dd7ff47ddc7838b15e1bc9de9107	Unit_test.cpython-312-pytest-8.3.3.pyc
100644 blob 36fe924bab7e704d4d7685602410c1b9fc7a3a33	main.cpython-312.pyc
100644 blob bba419717915b70d8108ad8bb8f32b361b75b2e1	test_main.cpython-312-pytest-8.3.3.pyc

========================================
Hash: 74f2049539d4dd7ff47ddc7838b15e1bc9de9107
Path: __pycache__/Unit_test.cpython-312-pytest-8.3.3.pyc
Content:

    {
        KEY : 12,
        HR : 34
    }  
========================================
Hash: 36fe924bab7e704d4d7685602410c1b9fc7a3a33
Path: __pycache__/main.cpython-312.pyc
Content:

exceptionsÚ	LarkErrora  
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
%ignore /\|\|.*
/x
%ignore /--\[\[.*\]\]/sx
GET <- 23

    {
        KEY : .GET.,
        HR : 34
    }
========================================
Hash: bba419717915b70d8108ad8bb8f32b361b75b2e1
Path: __pycache__/test_main.cpython-312-pytest-8.3.3.pyc
Content:
    {
        KEY : 12,
        HR : 34
    }
    ú{
    "KEY": 12,
    "HR": 34
}
{
Q : 12,
W : 32,
E : {
        R : 94,
        T : 100
    }
}
    zP{
    "Q": 12,
    "W": 32,
    "E": {
        "R": 94,
        "T": 100
    }
    {
        KEY : 12,
        HR : 34
    }
    {
        KEY : 12,
        HR : 34
    }
    GET <- 23
    {
        KEY : 12,
        HR : 34
    }
    zN{
    "constaint": {
        "GET": 23
    }
}
{
    "KEY": 12,
    "HR": 34
    GET <- 23
    {
        KEY : .GET.,
        HR : 34
    }
    zN{
    "constaint": {
        "GET": 23
    }
}
{
    "KEY": 23,
    "HR": 34
   r)   r+   r-   r/   r1   r4   r
ò ò&ó*r   
========================================
Hash: 1fa48f271c815387bb153899c5c79a29de4cacac
Path: main.py
Content:
import subprocess

def get_git_objects():
    objects = subprocess.check_output(["git", "rev-list", "--all", "--objects"]).decode("utf-8").splitlines()

    object_data = []

    for obj in objects:
        parts = obj.split(" ", 1)
        obj_hash = parts[0]
        path = parts[1] if len(parts) > 1 else "No path"

        try:
            obj_content = subprocess.check_output(["git", "cat-file", "-p", obj_hash]).decode("utf-8")
        except UnicodeDecodeError:
            obj_content = subprocess.check_output(["git", "cat-file", "-p", obj_hash]).decode("latin-1")

        object_data.append((obj_hash, path, obj_content))

    return object_data


def print_git_objects():
    objects = get_git_objects()
    for obj_hash, path, content in objects:
        print(f"Hash: {obj_hash}")
        print(f"Path: {path}")
        print("Content:")
        print(content)
        print("=" * 40)


if __name__ == "__main__":
    print_git_objects()

========================================
Hash: daa8e18da8d44bab838d0fbf7a19176acfbc6914
Path: test_main.py
Content:
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
========================================
```
