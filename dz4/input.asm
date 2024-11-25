# Инициализация первого вектора
LOAD_CONST 200, 10    # vector1[0] = 10
LOAD_CONST 201, 15    # vector1[1] = 15
LOAD_CONST 202, 20    # vector1[2] = 20
LOAD_CONST 203, 25    # vector1[3] = 25
LOAD_CONST 204, 30    # vector1[4] = 30

# Инициализация второго вектора
LOAD_CONST 210, 5     # vector2[0] = 5
LOAD_CONST 211, 15    # vector2[1] = 15
LOAD_CONST 212, 25    # vector2[2] = 25
LOAD_CONST 213, 20    # vector2[3] = 20
LOAD_CONST 214, 35    # vector2[4] = 35

# Сравнение элементов и сохранение результатов
BIN_OP_GT 220, 200, 0, 210   # result[0] = vector1[0] > vector2[0]
BIN_OP_GT 221, 201, 0, 211   # result[1] = vector1[1] > vector2[1]
BIN_OP_GT 222, 202, 0, 212   # result[2] = vector1[2] > vector2[2]
BIN_OP_GT 223, 203, 0, 213   # result[3] = vector1[3] > vector2[3]
BIN_OP_GT 224, 204, 0, 214   # result[4] = vector1[4] > vector2[4]
