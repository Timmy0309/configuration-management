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
