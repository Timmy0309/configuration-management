import csv
import sys

def interpret(binary_file, memory_dump_file, start, end):
    memory = {}
    with open(binary_file, 'rb') as f:
        code = f.read()

    MASK_3 = (1 << 3) - 1        # 0b111
    MASK_11 = (1 << 11) - 1      # 0b11111111111
    MASK_22 = (1 << 22) - 1      # 0b1111111111111111111111
    MASK_25 = (1 << 25) - 1      # 0b1111111111111111111111111

    pc = 0  # Program counter
    while pc < len(code):
        opcode = code[pc] & MASK_3  # Биты 0-2
        if opcode == 2:  # LOAD_CONST
            if pc + 7 > len(code):
                print(f"Ошибка: недостаточно байт для чтения LOAD_CONST по адресу {pc}")
                sys.exit(1)
            instr_bytes = code[pc:pc+7]
            instr = int.from_bytes(instr_bytes, byteorder='little')
            B = (instr >> 3) & MASK_22  # Биты 3-24
            C = (instr >> 25) & MASK_25  # Биты 25-49
            memory[B] = C
            pc += 7
        elif opcode == 7:  # READ_MEM
            if pc + 6 > len(code):
                print(f"Ошибка: недостаточно байт для чтения READ_MEM по адресу {pc}")
                sys.exit(1)
            instr_bytes = code[pc:pc+6]
            instr = int.from_bytes(instr_bytes, byteorder='little')
            B = (instr >> 3) & MASK_22
            C = (instr >> 25) & MASK_22
            memory[B] = memory.get(C, 0)
            pc += 6
        elif opcode == 5:  # WRITE_MEM
            if pc + 8 > len(code):
                print(f"Ошибка: недостаточно байт для чтения WRITE_MEM по адресу {pc}")
                sys.exit(1)
            instr_bytes = code[pc:pc+8]
            instr = int.from_bytes(instr_bytes, byteorder='little')
            B = (instr >> 3) & MASK_22
            C = (instr >> 25) & MASK_11
            D = (instr >> 36) & MASK_22
            addr = memory.get(B, 0) + C
            memory[addr] = memory.get(D, 0)
            pc += 8
        elif opcode == 1:  # BIN_OP_GT
            if pc + 10 > len(code):
                print(f"Ошибка: недостаточно байт для чтения BIN_OP_GT по адресу {pc}")
                sys.exit(1)
            instr_bytes = code[pc:pc + 10]
            instr = int.from_bytes(instr_bytes, byteorder='little')
            B = (instr >> 3) & MASK_11  # Смещение
            C = (instr >> 25) & MASK_22  # Адрес второго операнда
            D = (instr >> 47) & MASK_22  # Базовый адрес первого операнда
            E = (instr >> 69) & MASK_22  # Адрес для результата
            addr = D + B
            val1 = memory.get(addr, 0)
            val2 = memory.get(C, 0)
            memory[E] = int(val1 > val2)
            pc += 10
        else:
            print(f"Неизвестный опкод: {opcode} по адресу {pc}")
            sys.exit(1)

    # Сохранение диапазона памяти
    with open(memory_dump_file, 'w', newline='') as f_mem:
        mem_writer = csv.writer(f_mem)
        for addr in range(start, end+1):
            mem_writer.writerow([addr, memory.get(addr, 0)])

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Использование: python interpreter.py <binary_file> <memory_dump_file> <memory_start> <memory_end>")
        sys.exit(1)
    interpret(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
