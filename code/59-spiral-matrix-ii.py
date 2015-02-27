from iterator import count, izip
from misc import spiral


def generateMatrix(n):
    matrix = [[0 for _ in xrange(n)] for _ in xrange(n)]

    for (x, y), v in izip(spiral(True, 0, 0, n, n), count(1)):
        matrix[y][x] = v

    return matrix
