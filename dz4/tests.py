import subprocess
import os
import csv

def run_test(test_name, asm_code, expected_memory, memory_range):
    asm_file = f"{test_name}.asm"
    bin_file = f"{test_name}.bin"
    log_file = f"{test_name}_log.csv"
    mem_dump_file = f"{test_name}_memory.csv"

    # Запись ассемблерного кода в файл
    with open(asm_file, 'w') as f:
        f.write(asm_code)

    # Запуск ассемблера
    assembler_cmd = ['python', 'assembler.py', asm_file, bin_file, log_file]
    subprocess.run(assembler_cmd)

    # Запуск интерпретатора
    interpreter_cmd = ['python', 'interpreter.py', bin_file, mem_dump_file, str(memory_range[0]), str(memory_range[1])]
    subprocess.run(interpreter_cmd)

    # Чтение результата из memory_dump_file
    memory = {}
    with open(mem_dump_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            addr, value = int(row[0]), int(row[1])
            memory[addr] = value

    # Проверка ожидаемых значений
    success = True
    for addr, expected_value in expected_memory.items():
        actual_value = memory.get(addr, None)
        if actual_value != expected_value:
            print(f"Тест {test_name} не пройден: адрес {addr}, ожидается {expected_value}, получено {actual_value}")
            success = False

    if success:
        print(f"Тест {test_name} пройден успешно")

    # Удаление временных файлов
    os.remove(asm_file)
    os.remove(bin_file)
    os.remove(log_file)
    os.remove(mem_dump_file)

# Примеры тестов

# Тест 1: Загрузка константы
asm_code_1 = """
LOAD_CONST 80, 886
"""
expected_memory_1 = {
    80: 886
}
memory_range_1 = (80, 80)
run_test("test_load_const", asm_code_1, expected_memory_1, memory_range_1)

# Тест 2: Чтение из памяти
asm_code_2 = """
LOAD_CONST 565, 1234
READ_MEM 356, 565
"""
expected_memory_2 = {
    356: 1234
}
memory_range_2 = (356, 356)
run_test("test_read_mem", asm_code_2, expected_memory_2, memory_range_2)

# Тест 3: Запись в память
asm_code_3 = """
LOAD_CONST 487, 100
LOAD_CONST 838, 200
WRITE_MEM 487, 309, 838
"""
expected_memory_3 = {
    409: 200  # 100 (значение по адресу 487) + 309 = 409
}
memory_range_3 = (409, 409)
run_test("test_write_mem", asm_code_3, expected_memory_3, memory_range_3)