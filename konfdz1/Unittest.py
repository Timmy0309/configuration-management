from main import ShellEmulator
import unittest

class TestShelEmulator(unittest.TestCase):
    def setUp(self):
        self.shell = ShellEmulator('konffile.xml')

    def test_ls1(self):
        out = self.shell.ls("")
        self.assertIn('arxive', out)

    def test_ls2(self):
        out = self.shell.ls('/arxive/repos')
        self.assertIn('filethree.txt', out)

    def test_cd1(self):
        out = self.shell.cd('arxive')
        self.assertIn('arxive', out)

    def test_cd2(self):
        out = self.shell.cd('/arxive/repos')
        self.assertIn('arxive/repos', out)

    def test_chown1(self):
        out = self.shell.chown('Timmy', 'arxive/fileone.txt')
        self.assertIn("Владелец fileone.txt изменен на Timmy", out)

    def test_chown2(self):
        out = self.shell.chown('Timmy', 'mimimi.txt')
        self.assertIn("Нет такого файла или каталога", out)

    def test_mv1(self):
        out = self.shell.mv("fileone.txt", "filefive.txt")
        self.assertIn('Файл fileone.txt переименован в filefive.txt', out)

    def test_mv2(self):
        out = self.shell.mv("filefive.txt", "fileone.txt")
        self.assertIn('Файл filefive.txt переименован в fileone.txt', out)

if __name__ == '__main__':
    unittest.main()