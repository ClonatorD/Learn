matrix, m = [], 0
while m != "end":
    m = [i for i in input().split()]
    if m[0] == "end":
        break
    m = list(map(int, m))
    matrix.append(m)
    m = 0
x = len(matrix)
y = len(matrix[0])
matrix2 = [[0 for j in range(y)] for i in range(x)]
for i in range(x):
    for j in range(y):
        matrix2[i][j] += (matrix[i - 1][j] + matrix[i + 1 - x][j] + matrix[i][j - 1] + matrix[i][j + 1 - y])
for i in matrix2:
    for j in i:
        print(j, end=" ")
    print()
