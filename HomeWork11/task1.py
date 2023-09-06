# Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения, *умножения матриц


class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        if data is None:
            self.data = [[0] * cols for _ in range(rows)]
        else:
            if len(data) != rows or any(len(row) != cols for row in data):
                raise ValueError("Неверные размеры данных")
            self.data = data

    def __str__(self):
        return '\n'.join([" ".join(map(str, row)) for row in self.data])

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if (isinstance(other, Matrix)
            and self.rows == other.rows
                and self.cols == other.cols):
            new_data = ([[self.data[i][j] + other.data[i][j]
                        for j in range(self.cols)]
                        for i in range(self.rows)])
            return Matrix(self.rows, self.cols, new_data)
        raise ValueError("Матрицы не подходят для сложения")

    def __mult__(self, other):
        if isinstance(other, (int, float)):
            new_data = ([[self.data[i][j] * other
                        for j in range(self.cols)]
                        for i in range(self.rows)])
            return Matrix(self.rows, self.cols, new_data)

        if isinstance(other, Matrix) and self.cols == other.rows:
            new_data = ([[sum(self.data[i][k] * other.data[k][j]
                        for k in range(self.cols))
                        for j in range(other.cols)]
                        for i in range(self.rows)])
            return Matrix(self.rows, other.cols, new_data)
        raise ValueError("Матрицы не подходят для умножения")


m1 = Matrix(3, 3)
m1.data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(f'Матрица 1: {m1.data}')
m2 = Matrix(3, 3)
m2.data = [[3, 3, 3], [4, 4, 4], [5, 5, 5]]
print(f'Матрица 2: {m2.data}')
print()
print(f'Сравнение значений элементов двух матриц: {m1.__eq__(m2)}\n')
print(f'Сложение матриц: \n{m1.__add__(m2)}')
print(f'Умножение матриц: \n{m1.__mult__(m2)}')
