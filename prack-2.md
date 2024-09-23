# Задание 1:
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
## код: pip show matplotlib

## скриншот:
![Screenshot 2024-09-16 173635](https://github.com/user-attachments/assets/7b4ea9ee-89a1-4391-a019-b0abf06b4acc)
## код для получения пакета прямо из репозитория: git clone https://github.com/matplotlib/matplotlib.git
## скриншот:
![Screenshot 2024-09-21 222009](https://github.com/user-attachments/assets/f6e09dbb-59ab-481f-b593-5a095f42ec0c)


# Задание 2: 
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
## код: npm view express
## скриншот:
![Screenshot 2024-09-21 125704](https://github.com/user-attachments/assets/dd1391a6-7156-4cd7-995a-cdab4af2b99e)
## код для получения пакета прямо из репозитория: git clone https://github.com/expressjs/express.git
## скриншот:
![Screenshot 2024-09-21 222049](https://github.com/user-attachments/assets/9e8d020f-e295-44dc-b04b-36bd48123f2d)


# Задание 3: 
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
## код для matplotlib: 
echo 'digraph G { node [shape=box]; matplotlib [label="matplotlib"]; numpy [label="numpy"]; pillow [label="pillow"]; cycler [label="cycler"]; matplotlib -> numpy; matplotlib -> pillow; matplotlib -> cycler; }' > matplotlib.dot
dot -Tpng matplotlib.dot -o matplotlib.png
fim matplotlib.png
## код для express:
echo 'digraph G { node [shape=box]; express [label="express"]; accepts [label="accepts"]; array_flatten [label="array-flatten"]; content_type [label="content-type"]; express -> accepts; express -> array_flatten; express -> content_type; }' > express.dot
dot -Tpng express.dot -o matplotlib.png
fim matplotlib.png
## Скриншот:
![Screenshot 2024-09-21 222516](https://github.com/user-attachments/assets/9e2da581-8a5e-4599-b49f-f8e14b26f028)
![Screenshot 2024-09-21 222611](https://github.com/user-attachments/assets/e80ee1e7-a9c6-4d33-a9b3-4fe96f751574)


# Задание 4:
Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
## код:
include "globals.mzn"; 
array[1..6] of var 0..9: digits;
constraint all_different(digits);
var int: sum1 = digits[1] + digits[2] + digits[3];
var int: sum2 = digits[4] + digits[5] + digits[6];
constraint sum1 = sum2;
constraint sum1 >= 0; 
solve satisfy;
output ["Digits: \(digits)\nSum: \(sum1)"];
## скриншот:
![Screenshot 2024-09-21 224927](https://github.com/user-attachments/assets/62ed1d7b-8549-421f-9ba6-f88d4a7a0f95)
![Screenshot 2024-09-21 224937](https://github.com/user-attachments/assets/3e0c0a05-3070-4ae2-a98a-36c55fce7fc4)

# Задание 5:
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/b4a5a73b-1be7-44c7-ba30-c3e33e07b36b)
## код:

## Скриншот:

