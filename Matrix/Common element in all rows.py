def commonElement(matrix):
    common=set(matrix[0])

    for row in matrix[1:]:
        common &= set(row)

    return common

matrix = [
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [4, 3, 7, 8]
]

print(commonElement(matrix))