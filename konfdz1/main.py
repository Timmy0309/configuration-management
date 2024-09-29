import os
import tarfile
import json
import argparse
import shlex
import datetime
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import scrolledtext
import xml.etree.ElementTree as ET


class ShellEmulator:
    def __init__(self, config_path):
        self.load_config(config_path)
        self.current_directory = 'vfs'
        self.history = []
        self.list_user = {}
        self.install_user()
        self.gui()

    def load_config(self, conf_path):
        tree = ET.parse(conf_path)
        rootxml = tree.getroot()
        self.user_name = rootxml.find('username').text
        self.vfs_path = rootxml.find('vfs_path').text
        self.iamlocate = ""
        self.log_file_path = rootxml.find('log_file_path').text

        #self.unpack_vfs()
    def unpack_vfs(self):
        print(self.vfs_path)
        if not os.path.exists(self.vfs_path):
            raise FileNotFoundError("VFS file not found.")

        with tarfile.open(self.vfs_path) as tar:
            tar.extractall(path='vfs')

    def install_user(self):
        with tarfile.open(self.vfs_path, 'r') as tar:
            for member in tar.getmembers():
                self.list_user[member.name.split('/')[-1]] = "Timofey"
    def log_action(self, action):
        timestamp = datetime.datetime.now().isoformat()
        self.history.append({'timestamp': timestamp, 'user': self.user_name, 'action': action})

    def save_log(self):
        with open(self.log_file_path, 'w') as log_file:
            json.dump(self.history, log_file, indent=4)

    def gui(self):
        self.root = tk.Tk()
        self.root.title('Shell Emulator')
        self.prompt_label = tk.Label(self.root, text=f'{self.user_name}@emulator:~$', width=100)
        self.prompt_label.pack()
        self.entry = tk.Entry(self.root, width=70)
        self.entry.pack()
        self.entry.bind('<Return>', self.execute_command)
        self.info = tk.Text(self.root)
        self.info.pack()
    def execute_command(self, event):
        comand_input = self.entry.get()
        self.entry.delete(0, tk.END)
        comand = comand_input.strip().split()
        if not comand:
            return
        action = ' '.join(comand)
        self.info.insert(tk.END, '\n')
        self.info.insert(tk.END, f'{self.user_name}@emulator:{self.iamlocate}$ {action}\n')

        if comand[0] == 'exit':
            self.save_log()
            self.root.quit()
        elif comand[0] == 'ls':
            if len(comand) > 1 and comand[1] == '-l':
                self.listls(comand[2] if len(comand) > 2 else "")
            else:
                self.printls(self.ls(comand[1] if len(comand) > 1 else ""))
        elif comand[0] == 'cd':
            self.cd(comand[1] if len(comand) > 1 else "")
        elif comand[0] == 'chown':
            if len(comand) != 3:
                self.info.insert(tk.END, "chown user file")
            else:
                self.chown(comand[1], comand[2])
        elif comand[0] == 'mv':
            if len(comand) != 3:
                self.info.insert(tk.END, "mv file path/new name file")
            else:
                self.mv(comand[1], comand[2])
        else:
            self.info.insert(tk.END, f'unknown command {comand[0]}')

        self.log_action(action)

    def ls(self, temp_path: str):
        if temp_path == "":
            with tarfile.open(self.vfs_path, 'r') as tar:
                out = []
                for member in tar.getmembers():
                    if self.iamlocate == "":
                        if '/' not in member.name:
                            out.append(member.name)
                    elif member.name.startswith(self.iamlocate+"/") and member.name.count('/') == self.iamlocate.count('/')+1:
                        out.append(member.name.split('/')[-1])
                if len(out) != 0:
                    return out
        elif temp_path == "~" or temp_path == "/":
            with tarfile.open(self.vfs_path, 'r') as tar:
                out = []
                for member in tar.getmembers():
                    if '/' not in member.name:
                        out.append(member.name)
                if len(out) != 0:
                    return out
                else:
                    return "ГГ"
        elif (temp_path == ".." or temp_path == "../") and self.iamlocate != "":
            with tarfile.open(self.vfs_path, 'r') as tar:
                out = []
                for member in tar.getmembers():
                    if self.iamlocate != "arxive":
                        path = self.iamlocate.split('/')
                        path_to_dir = ""
                        for i in range(len(path)-1):
                            path_to_dir = path_to_dir + path[i] + "/"
                        if member.name.startswith(path_to_dir) and member.name.count('/') < 2:
                            out.append(member.name.split('/')[-1])
                    else:
                        if '/' not in member.name:
                            out.append(member.name)
                if len(out) != 0:
                    return out
                else:
                    return "Нет такого файла или папки"
        elif temp_path[:3] == "../":
            temp_path = temp_path[3:]
            with tarfile.open(self.vfs_path, 'r') as tar:
                path = self.iamlocate.split('/')
                path_to_dir = ""
                for i in range(len(path) - 1):
                    path_to_dir = path_to_dir + path[i] + "/"
                temp_path = path_to_dir + temp_path
                out = []
                for member in tar.getmembers():
                    if member.name.split('/')[:len(temp_path.split('/'))] == temp_path.split('/') and member.name.count('/') == temp_path.count('/')+1:
                        out.append(member.name.split('/')[-1])
                if len(out) != 0:
                    return out
                else:
                    return "Нет такого файла или папки"

        elif temp_path[0] == "/":
            temp_path = temp_path[1:]
            with tarfile.open(self.vfs_path, 'r') as tar:
                out = []
                for member in tar.getmembers():
                    if member.name.startswith(temp_path+"/") and member.name.count('/') == temp_path.count('/')+1:
                        out.append(member.name.split('/')[-1])
                if len(out) != 0:
                    return out
                else:
                    return "Нет такого файла или папки"
        else:
            if temp_path[:2] == "./":
                temp_path = temp_path[2:]
            if self.iamlocate != "":
                temp_path = self.iamlocate + "/" + temp_path
            with tarfile.open(self.vfs_path, 'r') as tar:
                out = []
                for member in tar.getmembers():
                    if member.name.startswith(temp_path+"/") and member.name.count('/') == temp_path.count('/')+1:
                        out.append(member.name.split('/')[-1])
                if len(out) != 0:
                    return out
                else:
                    return "Нет такого файла или папки"

    def printls(self, out):
        if out == "Нет такого файла или папки":
            self.info.insert(tk.END, "Нет такого файла или папки")
        else:
            for i in range(len(out)):
                self.info.insert(tk.END, out[i] + "  ")
    def listls(self, temp_path):
        out = self.ls(temp_path)
        if out == "Нет такого файла или папки":
            self.info.insert(tk.END, "Нет такого файла или папки")
        else:
            for i in range(len(out)):
                self.info.insert(tk.END, self.list_user[out[i]] + "  " + out[i] + '\n')

    def cd(self, temp_path: str):
        if temp_path == "" or temp_path == "~" or temp_path == "/":
            self.iamlocate = ""
            self.prompt_label.config(text=f'{self.user_name}@emulator:~$')
            return ""
        elif temp_path == ".." or temp_path == "../":
            if self.iamlocate == "":
                return ""
            if len(self.iamlocate.split('/')) == 1:
                self.iamlocate = ""
                self.prompt_label.config(text=f'{self.user_name}@emulator:~$')
                return ""
            else:
                self.iamlocate = self.iamlocate[:self.iamlocate.rfind('/')]
                self.prompt_label.config(text=f'{self.user_name}@emulator:~{self.iamlocate[:self.iamlocate.rfind('/')]}$')
                return self.iamlocate[:self.iamlocate.rfind('/')]
        elif temp_path[0] == "/":
            temp_path = temp_path[1:]
            with tarfile.open(self.vfs_path, 'r') as tar:
                for member in tar.getmembers():
                    if member.isdir() and member.name == temp_path:
                        self.iamlocate = temp_path
                        self.prompt_label.config(text=f'{self.user_name}@emulator:~{temp_path}$')
                        return temp_path
                else:
                    self.info.insert(tk.END, "Нет такого каталога")
                    return "Нет такого каталога"
        elif temp_path[:3] == "../":
            temp_path = temp_path[3:]
            if self.iamlocate == "":
                self.prompt_label.config(text=f'{self.user_name}@emulator:~$')
                return ""
            with tarfile.open(self.vfs_path, 'r') as tar:
                for member in tar.getmembers():
                    if member.isdir() and self.iamlocate != "arxive" and member.name == self.iamlocate[:self.iamlocate.rfind('/')] + "/" + temp_path:
                        self.iamlocate = self.iamlocate[:self.iamlocate.rfind('/')] + "/" + temp_path
                        self.prompt_label.config(text=f'{self.user_name}@emulator:~{self.iamlocate}$')
                        return self.iamlocate[:self.iamlocate.rfind('/')] + "/" + temp_path
                    elif member.isdir() and member.name == temp_path:
                        self.iamlocate = temp_path
                        self.prompt_label.config(text=f'{self.user_name}@emulator:~{temp_path}$')
                        return temp_path
                else:
                    self.info.insert(tk.END, "Нет такого каталога")
                    return "Нет такого каталога"
        else:
            if temp_path[:2] == "./":
                temp_path = temp_path[2:]
            with tarfile.open(self.vfs_path, 'r') as tar:
                for member in tar.getmembers():
                    if member.isdir() and self.iamlocate != "" and member.name == self.iamlocate + "/" + temp_path:
                        self.iamlocate = self.iamlocate + "/" + temp_path
                        self.prompt_label.config(text=f'{self.user_name}@emulator:~{self.iamlocate}$')
                        return self.iamlocate + "/" + temp_path
                    elif member.isdir() and self.iamlocate == "" and member.name == temp_path:
                        self.iamlocate = temp_path
                        self.prompt_label.config(text=f'{self.user_name}@emulator:~{temp_path}$')
                        return temp_path
                else:
                    self.info.insert(tk.END, "Нет такого каталога")
                    return "Нет такого каталога"

    def chown(self, new_user, path):
        path = path.split('/')[-1]
        if path in self.list_user:
            self.list_user[path] = new_user
            self.info.insert(tk.END, f"Владелец {path} изменен на {new_user}")
            return f"Владелец {path} изменен на {new_user}"
        else:
            self.info.insert(tk.END, "Нет такого файла или каталога")
            return "Нет такого файла или каталога"

    def mv(self, file, new_path):
        if len(new_path.split('/')) == 1 and "." in new_path:
            new_name = new_path
            with tarfile.open(self.vfs_path, 'r') as tar:
                members = tar.getmembers()
                for member in members:
                    if member.name.split('/')[-1] == file:
                        member.name = member.name[:member.name.rfind('/')] + "/" + new_name

                with tarfile.open(self.vfs_path, "w") as new_tar:
                    for member in members:
                        new_tar.addfile(member, tar.extractfile(member))
            self.info.insert(tk.END, f'Файл {file} переименован в {new_name}')
            return f'Файл {file} переименован в {new_name}'
        else:
            if new_path[0] == "/":
                new_path = new_path[1:]
            elif new_path[:2] == "./":
                new_path = self.iamlocate + new_path[1:]
            with tarfile.open(self.vfs_path, 'r') as tar:
                members = tar.getmembers()
                for member in members:
                    if member.name.split('/')[-1] == file:
                        old_path = member.name
                with tarfile.open('new_arxive.tar', 'w') as new_tar:
                    for member in members:
                        if member.name != old_path:
                            new_tar.addfile(member, tar.extractfile(member))
                    move = tar.getmember(old_path)
                    move.name = new_path
                    new_tar.addfile(move, tar.extractfile(move))
            os.remove('disk.tar')
            os.rename('new_arxive.tar', 'disk.tar')
            self.info.insert(tk.END, f"Файл {file} перемещён в {new_path}")
            return f"Файл {file} перемещён в {new_path}"

    def run(self):
        self.root.mainloop()



if __name__ == '__main__':
    emulator = ShellEmulator('konffile.xml')
    emulator.run()



