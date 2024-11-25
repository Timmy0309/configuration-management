import sys
import csv

def assemble(input_file, output_file, log_file):
    instructions = []
    with open(input_file, 'r', encoding="utf-8") as f:
        lines = f.readlines()

    # Определение масок и максимальных значений
    MASK_3 = (1 << 3) - 1        # 0b111
    MASK_11 = (1 << 11) - 1      # 0b11111111111
    MASK_22 = (1 << 22) - 1      # 0b1111111111111111111111
    MASK_25 = (1 << 25) - 1      # 0b1111111111111111111111111

    for line_num, line in enumerate(lines, start=1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Пропуск комментариев и пустых строк
        # Удаление комментариев из строки
        line = line.split('#')[0].strip()
        if not line:
            continue  # Пропуск пустых строк после удаления комментариев
        parts = line.split(None, 1)
        mnemonic = parts[0]
        operands_str = parts[1] if len(parts) > 1 else ''
        operands = [operand.strip() for operand in operands_str.split(',')]

        try:
            if mnemonic == 'LOAD_CONST':
                if len(operands) != 2:
                    raise ValueError("ожидается 2 операнда")
                opcode = 2
                B = int(operands[0])
                C = int(operands[1])
                if B < 0 or B > MASK_22:
                    raise ValueError(f"значение B={B} выходит за пределы 22 бит")
                if C < 0 or C > MASK_25:
                    raise ValueError(f"значение C={C} выходит за пределы 25 бит")
                instr = (opcode & MASK_3) | ((B & MASK_22) << 3) | ((C & MASK_25) << 25)
                instructions.append(('LOAD_CONST', opcode, B, C, instr))

            elif mnemonic == 'READ_MEM':
                if len(operands) != 2:
                    raise ValueError("ожидается 2 операнда")
                opcode = 7
                B = int(operands[0])
                C = int(operands[1])
                if B < 0 or B > MASK_22:
                    raise ValueError(f"значение B={B} выходит за пределы 22 бит")
                if C < 0 or C > MASK_22:
                    raise ValueError(f"значение C={C} выходит за пределы 22 бит")
                instr = (opcode & MASK_3) | ((B & MASK_22) << 3) | ((C & MASK_22) << 25)
                instructions.append(('READ_MEM', opcode, B, C, instr))

            elif mnemonic == 'WRITE_MEM':
                if len(operands) != 3:
                    raise ValueError("ожидается 3 операнда")
                opcode = 5
                B = int(operands[0])
                C = int(operands[1])
                D = int(operands[2])
                if B < 0 or B > MASK_22:
                    raise ValueError(f"значение B={B} выходит за пределы 22 бит")
                if C < 0 or C > MASK_11:
                    raise ValueError(f"значение C={C} выходит за пределы 11 бит")
                if D < 0 or D > MASK_22:
                    raise ValueError(f"значение D={D} выходит за пределы 22 бит")
                instr = (opcode & MASK_3) | ((B & MASK_22) << 3) | ((C & MASK_11) << 25) | ((D & MASK_22) << 36)
                instructions.append(('WRITE_MEM', opcode, B, C, D, instr))


            elif mnemonic == 'BIN_OP_GT':

                if len(operands) != 4:
                    raise ValueError("ожидается 4 операнда")

                opcode = 1

                E = int(operands[0])  # dest_addr

                D = int(operands[1])  # base_addr

                B = int(operands[2])  # offset

                C = int(operands[3])  # src_addr2

                if B < 0 or B > MASK_11:
                    raise ValueError(f"значение B={B} выходит за пределы 11 бит")

                if C < 0 or C > MASK_22:
                    raise ValueError(f"значение C={C} выходит за пределы 22 бит")

                if D < 0 or D > MASK_22:
                    raise ValueError(f"значение D={D} выходит за пределы 22 бит")

                if E < 0 or E > MASK_22:
                    raise ValueError(f"значение E={E} выходит за пределы 22 бит")

                instr = (opcode & MASK_3) | ((B & MASK_11) << 3) | ((C & MASK_22) << 25) | ((D & MASK_22) << 47) | (
                            (E & MASK_22) << 69)

                instructions.append(('BIN_OP_GT', opcode, B, C, D, E, instr))

            else:
                raise ValueError(f"Неизвестная команда: {mnemonic}")
        except ValueError as ve:
            print(f"Ошибка в строке {line_num}: {ve}")
            sys.exit(1)

    # Запись в бинарный файл
    with open(output_file, 'wb') as f_bin, open(log_file, 'w', newline='') as f_log:
        log_writer = csv.writer(f_log)
        for instr in instructions:
            if instr[0] == 'LOAD_CONST':
                _, opcode, B, C, code = instr
                f_bin.write(code.to_bytes(7, byteorder='little'))
                log_writer.writerow(['opcode=2', f'B={B}', f'C={C}'])

            elif instr[0] == 'READ_MEM':
                _, opcode, B, C, code = instr
                f_bin.write(code.to_bytes(6, byteorder='little'))
                log_writer.writerow(['opcode=7', f'B={B}', f'C={C}'])

            elif instr[0] == 'WRITE_MEM':
                _, opcode, B, C, D, code = instr
                f_bin.write(code.to_bytes(8, byteorder='little'))
                log_writer.writerow(['opcode=5', f'B={B}', f'C={C}', f'D={D}'])

            elif instr[0] == 'BIN_OP_GT':
                _, opcode, B, C, D, E, code = instr
                f_bin.write(code.to_bytes(10, byteorder='little'))
                log_writer.writerow(['opcode=1', f'B={B}', f'C={C}', f'D={D}', f'E={E}'])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python assembler.py <input_file> <output_file> <log_file>")
        sys.exit(1)
    assemble(sys.argv[1], sys.argv[2], sys.argv[3])
