Задание 1: 
код:
cut -d: -f1 /etc/passwd | sort
скриншот:
![Screenshot 2024-09-09 162853](https://github.com/user-attachments/assets/4650e7a5-41a1-45a9-9c1c-2e582cf4b4e3)

Задание 2: 
код:
cat /etc/protocols | tail -n 5 | sort -nrk2 | awk '{print $2, $1}'
скриншот:
![Screenshot 2024-09-09 163103](https://github.com/user-attachments/assets/828331c6-5642-4f0d-b69f-5675321caa1d)

Задание 3: 
код:
msg="$1"
border="+$(printf '%0.s-' $(seq ${#msg} + 2))+"
echo "$border"
echo "| $msg |"
echo "$border"
скриншот:
![Screenshot 2024-09-09 163331](https://github.com/user-attachments/assets/df98ec16-0516-45c2-8155-5a4e1c7de6c7)

Задание 4: 
код:
grep -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' main.cpp | sort | uniq
скриншот:



Задание 7: 
код:
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
скриншот:


Задание 8: 
код:
find . -name "*.$1" -print0 | tar -czvf archive.tar.gz --null -T -
