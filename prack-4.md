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
