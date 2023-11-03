# Напишите функцию для транспонирования матрицы

def my_transposition(matrix: list[int]):
    res_matrix = []
    for i in range(len(matrix[0])):

        cur_row = []
        for j in range(len(matrix)):
            cur_row.append(matrix[j][i])

        res_matrix.append(cur_row)
    return res_matrix


def print_matrix_nice(matrix):  # печать матрицы в виде прямоугольника, а не в строчку
    for i in range(len(matrix)):
        print(matrix[i])


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

print('Исходная матрица:')
print_matrix_nice(matrix)
print('Транспонированная матрица:')
print_matrix_nice(my_transposition(matrix))
