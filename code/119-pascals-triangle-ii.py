def getRow(rowIndex):
    if rowIndex == 0:
        return [1]

    row = getRow(rowIndex - 1)
    return [1] + [row[i-1]+row[i] for i in xrange(1, rowIndex)] + [1]
