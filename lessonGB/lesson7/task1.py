from copy import deepcopy


class Matrix:
    def __init__(self, param: list):
        self.matrix = deepcopy(param)

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other):
        result = []
        for item in zip(self.matrix, other.matrix):
            result.append([sum([i, j]) for i, j in zip(*item)])
        return Matrix(result)


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[0, 0], [1, 1], [0, 1]])
print(matrix1)
print()
print(matrix2)
print()
print(matrix1 + matrix2)
