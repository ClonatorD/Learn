n, p, l = int(input()), 0, 1
matrix = [[0 for j in range(n)] for i in range(n)]
z = (n ** 2)
matrix[n // 2][n // 2] = n * n
for nl in range(n // 2):
    for i in range(n - p):
        matrix[nl][i + nl] = l
        l += 1
    for i in range(nl + 1, n - nl):
        matrix[i][-nl - 1] = l
        l += 1
    for i in range(nl + 1, n - nl):
        matrix[-nl - 1][-i - 1] = l
        l += 1
    for i in range(nl + 1, n - (nl + 1)):
        matrix[-i - 1][nl] = l
        l += 1
    p += 2
for i in matrix:
    print(*i)
