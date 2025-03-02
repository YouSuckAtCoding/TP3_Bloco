import multiprocessing


def matrixMulti(matrix1, matrix2):
    if len(matrix1[0]) > len(matrix2):
        return
    
    result = [[0 for _ in range(len(matrix1))] for _ in range(0, len(matrix2[0]))]

    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix2[0])):
            for k in range(0, len(matrix2)):
                result[i][j] = matrix1[i][k] * matrix2[k][j]
    
    return result


matrix1 = [[1,2,3], [4,5,6]]
matrix2 = [[1,2], [4,5], [7,9]]

print(matrixMulti(matrix1, matrix2))


