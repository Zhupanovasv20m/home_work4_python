# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transponation(mat: list) -> list[list[int]]:
    '''Транспонирование матрицы'''
    rows = len(mat)
    cols = len(mat[0])
    trans_matrix = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(cols):
        for j in range(rows):
            trans_matrix[i][j] = mat[j][i]
    return trans_matrix


# matrix = [[1, 2, 3], [4, 5, 6]]
# print(transponation(matrix))
print(transponation([[1, 2, 3], [4, 5, 6]]))
