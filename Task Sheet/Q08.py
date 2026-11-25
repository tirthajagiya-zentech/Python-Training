# Matrix Multiplication
#
# 1. Take two 3x3 matrix.
# 2. take user inputs to fill it up.
# 3. Multiply them both and store it in another 3x3 matrix.
# 4. Display the result.

matrix1 = []
matrix2 = []

for i in range(3):
    row = []

    for j in range(3):
        value = int(input(f"Matrix 1:{i+1},{j+1}"))
        row.append(value)
    matrix1.append(row)

for i in range(3):
    row = []

    for j in range(3):
        value = int(input(f"Matrix 2:{i+1},{j+1}"))
        row.append(value)
    matrix2.append(row)


def multiply_matricss(A,B):
    row_A, col_A = len(A), len(A[0])
    row_B, col_B = len(B), len(B[0])

    if col_A != row_B :
        print("this mulpicatiooon is not posivle")

    result = [[0 for i in range(col_B)] for i in range(row_A)]

    summ = 0
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                summ += matrix1[i][k] * matrix2[k][j]
            result[i][j] = summ
            print(result[i][j], end = " ")
            summ = 0
        print()

multiply_matricss(matrix1, matrix2)
