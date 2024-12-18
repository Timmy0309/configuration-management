
# Описание
Инструмент командной строки для визуализации графа зависимостей для пакетов ОС alpine Linux (apk)

# Установка

1. Установка программы и переход в директорию
   ```bash
   git clone <URL репозитория>
   cd <директория проекта>
   ```
   
2. Установка plantUML
   Скачайте PlantUML с официального сайта
   
4. Убедитесь, что у вас установлен Python

5. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate     # Для Windows
   ```

# Конфигурационный файл

Для запуска визуализатора необходимо подготовить конфигурационный файл формата toml.
Файл conffile.toml должен содержать данные в следующем формате:
```bash
path_plantUML = "Путь к программе для визуализации графов". 
package_name = "Имя анализируемого пакета". 
output_file = "Путь к файлу с изображением графа зависимостей". 
url_repos = "URL-адрес репозитория". 
```

# Запуск визуализатора

С готовым конфигурационным файлом confile.toml выполнить следующую команду
   ```bash
   python main.py
   ```

# Выходные данные

Программа создает картинку графа зависимостей пакета:

- **dependency_graph.png** -- Граф в формате png (растровое изображение)

### Примеры выходных данных:
Файл dependency_graph.png


### Результаты тестирования
![Screenshot 2024-10-30 163417](https://github.com/user-attachments/assets/ff71c04d-ed0d-40d0-bc8e-d86632f50d1e)
