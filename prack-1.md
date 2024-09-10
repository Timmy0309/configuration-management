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
![Screenshot 2024-09-10 223529](https://github.com/user-attachments/assets/18460c74-359e-4598-a87a-1bdda1589ff7)

Задание 5: 
код:
chmod +x "file.c"
sudo cp "file.c" /usr/local/bin/
скриншот:
![Screenshot 2024-09-10 235502](https://github.com/user-attachments/assets/d26a5b14-c8bc-48d7-962d-b2c83a6278c7)

Задание 6: 
код:
for file in "file.c"; do
  if [[ "$file" =~ \.(c|js|py)$ ]]; then
    first_line=$(head -n 1 "$file")
    if [[ "$file" =~ \.c$ && "$first_line" =~ ^// ]] || \
       [[ "$file" =~ \.js$ && "$first_line" =~ ^// ]] || \
       [[ "$file" =~ \.py$ && "$first_line" =~ ^# ]]; then
      echo "$file has a comment in the first line."
    else
      echo "$file does not have a comment in the first line."
    fi
  fi
done
скриншот:
![Screenshot 2024-09-10 234753](https://github.com/user-attachments/assets/0df55188-af06-450b-bb5e-cddcaa9e1d82)


Задание 7: 
код:
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
скриншот:
![Screenshot 2024-09-10 230502](https://github.com/user-attachments/assets/c9fce292-a1c5-43fc-a36b-2fa9f61b74ae)


Задание 8: 
код:
find . -name "*.cpp" -print0 | tar -czvf archive.tar.gz --null -T -
скриншот:
![Screenshot 2024-09-10 231126](https://github.com/user-attachments/assets/8ee4b6f3-281d-43a9-8d8c-397d74501fa9)


Задание 9: 
код:
sed 's/    /\t/g' "test.txt" > "test1.txt"
скриншот:
![Screenshot 2024-09-10 225645](https://github.com/user-attachments/assets/dc98d721-f563-4210-8fff-ba723861a1e5)

Задание 10: 
код:
find "$1" -type f -empty -name "*.txt"
скриншот:
![Screenshot 2024-09-10 231651](https://github.com/user-attachments/assets/b412699f-6573-48ba-8087-983a2cd018a9)
