# Задание 1
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
## код 
```
local groupstart = "ИКБО-";
local groupend = "-20";
local groupindex = std.range(1, 24);

local studentlist = [
	{name: "Иванов И.И.", groupindex: 4, age: 19},
	{name: "Петров П.П.", groupindex: 5, age: 18},
	{name: "Сидоров С.С.", groupindex: 5, age: 18},
	{name: "Лясковский Т.М.", groupindex: 10, age: 18}
];

{
	groups: [groupstart + std.toString(i) + groupend for i in groupindex],
	students: [
	{
		age: student.age,
		group: groupstart + std.toString(student.groupindex) + groupend,
		name: student.name
	} for student in studentlist
	],
	subject: "Конфигурационное управление"
}
```
## скриншот
![Screenshot 2024-10-13 201317](https://github.com/user-attachments/assets/a3128b66-33dc-4c7e-b3c9-63769bcd5392)

# Задание 2
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
## код
```
let Group = Text
let Student = { age : Natural, group : Group, name : Text }

let createGroup : Natural -> Text =
      λ(n : Natural) → "ИКБО-" ++ Natural/show n ++ "-20"

let groups : List Text =
      [ createGroup 1
      , createGroup 2
      , createGroup 3
      , createGroup 4
      , createGroup 5
      , createGroup 6
      , createGroup 7
      , createGroup 8
      , createGroup 9
      , createGroup 10
      , createGroup 11
      , createGroup 12
      , createGroup 14
      , createGroup 15
      ]

let createStudent : Natural -> Group -> Text -> Student =
      λ(age : Natural) →
      λ(group : Group) →
      λ(name : Text) →
        { age = age, group = group, name = name }

let students : List Student =
  [ createStudent 19 (createGroup 4) "Петров П. П."
  , createStudent 18 (createGroup 5) "Иванов И. И."
  , createStudent 14 (createGroup 5) "Сидоров С. С."
  , createStudent 18 (createGroup 10) "Лясковский Т. М."
  ]

in  { groups = groups, students = students, subject = "Конфигурационное управление" }
```
## скриншот
![Screenshot 2024-10-13 202206](https://github.com/user-attachments/assets/2ff1c692-1fc9-405a-8c80-05766327753b)
![Screenshot 2024-10-13 202227](https://github.com/user-attachments/assets/3209e1f2-3649-469c-b3be-ba80e04b207f)
![Screenshot 2024-10-13 202239](https://github.com/user-attachments/assets/bd23c797-70ca-4317-8307-29d256ae60b1)

Для решения дальнейших задач потребуется программа на Питоне, представленная ниже. Разбираться в самом языке Питон при этом необязательно.
```python
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:

# Задание 3
Язык нулей и единиц.
```
10
100
11
101101
000
```
## код 
BNF = '''
E = 0 | 1 | 0 E | 1 E
'''
## скриншот
![Screenshot 2024-10-13 203144](https://github.com/user-attachments/assets/b9b09397-e904-48ff-962b-94462f06f4c3)


# Задание 4
Язык правильно расставленных скобок двух видов.
```
(({((()))}))
{}
{()}
()
{}
```
## код 
BNF = '''
E = | ( E ) | { E } | E E
'''
## скриншот
![Screenshot 2024-10-13 203351](https://github.com/user-attachments/assets/239e0a42-f0ec-45c2-bbef-6f1aa5a5d77a)

# Задание 5
Язык выражений алгебры логики.
```
((~(y & x)) | (y) & ~x | ~x) & x
y & ~(y)
(~(y) & y & ~y)
~x
~((x) & y | (y) | (x)) & x | x | (y & ~y)
```
## код 
BNF = '''

'''
## скриншот


