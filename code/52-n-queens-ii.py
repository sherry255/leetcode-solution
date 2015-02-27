"""
>>> solveNQueens(4)
[['..Q.', 'Q...', '...Q', '.Q..'], ['.Q..', '...Q', 'Q...', '..Q.']]
"""

from algorithm_x import select, solve


def is_primary(k):
    n, _ = k
    return (n == "x") or (n == "y")


def make_chess_board(s, n):
    board = [
        ["." for _ in xrange(n)]
        for _ in xrange(n) ]
    for x, y in s:
        board[y][x] = "Q"
    return map("".join, board)


def totalNQueens(n):
    cols = (
        [ ("x", x) for x in xrange(n) ] +
        [ ("y", y) for y in xrange(n) ] +
        [ ("c", c) for c in xrange(2*n-1) ] +
        [ ("d", d) for d in xrange(-n+1,n) ]
    )

    Cols = {c:set() for c in cols}

    Rows = {
        (x,y): [("x", x), ("y", y), ("c", x+y), ("d", x-y)]
        for x in xrange(n)
        for y in xrange(n)}

    for r, cols in Rows.iteritems():
        for c in cols:
            Cols[c].add(r)

    return len([
        make_chess_board(s, n)
        for s in solve(Cols, Rows, [], is_primary)])
