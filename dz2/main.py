import subprocess
import tarfile
import os
import urllib.request
import toml

config = toml.load('conffile.toml')
url_repos = config['url_repos']
package_name = config['package_name']
path_plantUML = config['path_plantUML']
output_file = config['output_file']

tar_path = "APKINDEX.tar.gz"
urllib.request.urlretrieve(url_repos, tar_path)

plantuml_code = "@startuml\n"


def get_package_dependencies(tar_path, package_name):
    dependencies = []

    with tarfile.open(tar_path, 'r') as tar:
        if 'APKINDEX' in tar.getnames():
            apkindex_file = tar.extractfile('APKINDEX')

            if apkindex_file:
                apkindex_content = apkindex_file.read().decode('utf-8').splitlines()

                in_package_section = False

                for line in apkindex_content:
                    if line.startswith('P:'):
                        current_package_name = line[2:].strip()
                        if current_package_name == package_name:
                            in_package_section = True
                        else:
                            in_package_section = False

                    if in_package_section:
                        if line.startswith('D:'):
                            dependencies = line[2:].strip().split()
                            break
        for i in range(len(dependencies)):
            dependencies[i] = dependencies[i][3:dependencies[i].rfind('.so')]
    global plantuml_code
    plantuml_code += generate_plantuml_code(package_name, dependencies)
    for dep in dependencies:
        get_package_dependencies(tar_path, dep)

    return dependencies


def generate_plantuml_code(package_name, dependencies):
    plantuml_code = ""
    package_name = '"' + package_name + '"'
    # plantuml_code += "class " + package_name + "\n"
    for dep in dependencies:
        dep = '"' + dep + '"'
        plantuml_code += f"    {package_name} --> {dep}\n"
    return plantuml_code


dependencies = get_package_dependencies(tar_path, package_name)
plantuml_code += "\n@enduml"

with open('dependency_graph.txt', 'w') as file:
    file.write(plantuml_code)

subprocess.call(['java', '-jar', path_plantUML, 'dependency_graph.txt'])

print("Граф зависимостей сохранен в файл dependency_graph.png")
file_path = 'dependency_graph.txt'

try:
    os.remove(file_path)
    os.remove('APKINDEX.tar.gz')
except OSError as e:
    print(f'Ошибка при удалении файла: {str(e)}')
