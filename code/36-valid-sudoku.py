def isValidSudoku(board):
    INDICES = (
        [[(j,i) for i in xrange(9)] for j in xrange(9)] +
        [[(i,j) for i in xrange(9)] for j in xrange(9)] +
        [[(x+i,y+j) for i in xrange(0,3) for j in xrange(0,3)]
         for x in xrange(0,9,3) for y in xrange(0,9,3)]
    )

    for constraint in INDICES:
        numbers = [ board[row][col]
                    for (row,col) in constraint
                    if board[row][col] != '.' ]
        if len(set(numbers)) < len(numbers):
            return False

    return True
