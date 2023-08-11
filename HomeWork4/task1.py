# Напишите функцию для транспонирования матрицы

# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

# import numpy as np // импорт библиотеки для вывода на печать матрицы


def matrix_transposition(matrix):
    matrix2 = list(map(list, [*zip(*matrix)]))
    return matrix2


matrix = [[1, 2, 3],
          [4, 5, 6]]

# print(np.matrix(matrix)) // печать матрицы с использованием библиотеки 'numpy'
print('Исходная матрица:')
for i in matrix:
    print(i)

print('Транспонированная матрица:')
for i in matrix_transposition(matrix):
    print(i)
