def diagonal(matrix):
    n = len(matrix)
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += matrix[i][i]
        s2 += matrix[i][n - i - 1]
    return s1 - s2

arr = [
    [1,2,3,4],
    [5,4,3,2],
    [2,8,1,6],
    [9,3,5,7]
]

print(diagonal(arr)) 
