
# Описание

Этот проект представляет собой инструмент командной строки для перобразования текста из 
входного формата (учебный конфигурационный язык) в выходной (JSON)

# Установка

Для начала, убедитесь, что у вас установлен Python. Затем выполните следующие шаги:
1. Установка программы и переход в директорию
   ```bash
   git clone <URL репозитория>
   cd <директория проекта>
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```
3. Установите необходимые зависимости (pytest для тестов, lark для работы программы):
   ```bash
   pip install pytest
   pip install lark
   ```

# Запуск скрипта

Скрипт принимает текст конфигурационного файла через стандартный ввод и выводит JSON в стандартный вывод.

Также можно запустить скрипт с вводом данных напрямую через консоль:
```bash
python script.py
```
После этого вы можете ввести конфигурацию вручную. Для завершения ввода нажмите ```Ctrl+D``` (Linux/macOS) или ```Ctrl+Z``` (Windows).
# Примеры входных и выходных данных

### Пример 1
**Входные данные:**
```
|| Настройка конфигурации сервера:
DEFAULTPORT <- 8080
{
PORT : .DEFAULTPORT.,
CONNECTION : 100
}
```
**Выходные данные (JSON):**
```json
{
    {
        "constaint": {
            "DEFAULTPORT": 8080
        }
    }
    {
        "PORT": 8080,
        "CONNECTION": 100
    }
}
```


### Пример 2
**Входные данные:**
```
--[[ Конфигурация игровых персонажей
например человека и гоблина
]]

{
PEOPLE : {
		HEALTH : 100,
		ATTACK : 10
	},
GOBLIN : {
		HEALTH : 110,
		ATTACK : 12
	}
}
```
**Выходные данные (JSON):**
```json
{
    {
        "PEOPLE": {
            "HEALTH": 100,
            "ATTACK": 10
        },
        "GOBLIN": {
            "HEALTH": 110,
            "ATTACK": 12
        }
    }
}
```

### Пример 3
**Входные данные:**
```
|| Конфигурация характеристик автомобилей:

CARS <- 3
SPEED <- 270

{
COUNTCAR : .CARS.,
TOYOTA : {
		MAXSPEED : .SPEED.,
		PASSENGERS : 4
	},
LADA : {
		MAXSPEED : 570, || на 3 скорости
		PASSENGERS : 12
	},
BUGATTI : {
		MAXSPEED : 550,
		PASSENGERS : 2
	}
}
```
**Выходные данные (JSON):**
```json
{
    {
        "constaint": {
            "CARS": 3,
            "SPEED": 270
        }
    }
    {
        "COUNTCAR": 3,
        "TOYOTA": {
            "MAXSPEED": 270,
            "PASSENGERS": 4
        },
        "LADA": {
            "MAXSPEED": 570,
            "PASSENGERS": 12
        },
        "BUGATTI": {
            "MAXSPEED": 550,
            "PASSENGERS": 2
        }
    }
}
```

# Тесты

Шаги запуска тестов:
1. Установить библиотеку pytest (необходимо, если не сделано ранее):
   ```bash
   pip install pytest
   ```
   
2. Для запуска тестирования необходимо запустить следующий скрипт:
   ```shell
   pytest -v
   ```

## Прохождение тестов:
![Screenshot 2024-10-30 175021](https://github.com/user-attachments/assets/7f8db6da-ae91-4cff-b98c-543946eca93b)

