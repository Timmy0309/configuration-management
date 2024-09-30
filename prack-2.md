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
solve minimize sum1;
output ["Digits: \(digits)\nSum: \(sum1)"];
## скриншот:
![Screenshot 2024-09-23 165541](https://github.com/user-attachments/assets/86225fdc-641b-428f-b0df-e6ea04d42bc2)

# Задание 5:
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/b4a5a73b-1be7-44c7-ba30-c3e33e07b36b)
## код:
enum PACKAGES = { root, menu_1_0_0, menu_1_1_0, menu_1_2_0, menu_1_3_0, menu_1_4_0, menu_1_5_0, dropdown_1_8_0, dropdown_2_0_0, dropdown_2_1_0, dropdown_2_2_0, dropdown_2_3_0, icons_1_0_0, icons_2_0_0 };

array[PACKAGES] of var 0..1: installed;
constraint installed[root] == 1;

constraint ((installed[root] == 1 -> installed[menu_1_0_0] == 1) \/ 
    (installed[root] == 1 -> installed[menu_1_1_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_2_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_3_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_4_0] == 1) \/
    (installed[root] == 1 -> installed[menu_1_5_0] == 1));
    
constraint (installed[root] == 1 -> installed[icons_1_0_0] == 1);

constraint (installed[menu_1_1_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_1_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_2_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_2_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_3_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_3_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_4_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_4_0] == 1 -> installed[dropdown_2_0_0] == 1);
constraint (installed[menu_1_5_0] == 1 -> installed[dropdown_2_3_0] == 1) \/ 
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_2_0] == 1) \/ 
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_1_0] == 1) \/  
    (installed[menu_1_5_0] == 1 -> installed[dropdown_2_0_0] == 1);
    
constraint (installed[menu_1_0_0] == 1) -> (installed[dropdown_1_8_0] == 1);
constraint ((installed[dropdown_2_0_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_1_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_2_0] == 1) -> (installed[icons_2_0_0] == 1));
constraint ((installed[dropdown_2_3_0] == 1) -> (installed[icons_2_0_0] == 1));

solve minimize(sum(installed));
output ["Installed packages: ", show(installed)];

## Скриншот:
![Screenshot 2024-09-30 162843](https://github.com/user-attachments/assets/ae60b88a-652f-4c0d-9b20-5f9c47c2247a)

# Задание 6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
## код
enum PACKAGES = {root, foo_1_0_0, foo_1_1_0, left, right, shared_1_0_0, shared_2_0_0, target_1_0_0, target_2_0_0};

array[PACKAGES] of var 0..1: includ;

constraint includ[root] == 1;
constraint includ[root] <= includ[foo_1_1_0] + includ[foo_1_0_0];
constraint includ[root] <= includ[target_2_0_0];

constraint includ[foo_1_1_0] <= includ[left] + includ[right];

constraint includ[left] <= includ[shared_1_0_0] + includ[shared_2_0_0];

constraint includ[right] <= includ[shared_1_0_0];

constraint includ[shared_1_0_0] <= includ[target_1_0_0];

solve minimize sum(includ);

output [
    "Included packages: \(includ)\n",
];
## скриншот
![Screenshot 2024-09-23 172524](https://github.com/user-attachments/assets/1cc85e5d-2c47-49cd-ad2e-ef69bfa4c57c)

# Задание 7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.
## код
## скриншот
