import unittest
import urllib.request
import toml
import os
from main import get_package_dependencies
from main import generate_plantuml_code


class MyTest(unittest.TestCase):
    def test_generate_plantuml_code(self):
        package_name = "PackageA"
        dependencies = ["PackageB", "PackageC"]
        expected_output = "    \"PackageA\" --> \"PackageB\"\n    \"PackageA\" --> \"PackageC\"\n"

        result = generate_plantuml_code(package_name, dependencies)

        self.assertEqual(result, expected_output)

    def test_get_package_dependencies(self):
        config = toml.load('conffile.toml')
        url_repos = config['url_repos']
        package_name = 'pcre'
        tar_path = "APKINDEX.tar.gz"
        urllib.request.urlretrieve(url_repos, tar_path)

        expected_output = ['libc.musl-armhf']

        result = get_package_dependencies(tar_path, package_name)
        os.remove('APKINDEX.tar.gz')
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
