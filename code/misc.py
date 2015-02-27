def spiral(first, x, y, m, n):
    if m == 0 or n == 0:
        return

    if first:
        for i in xrange(x,x+m):
            yield i, y

        for i in xrange(y+1,y+n):
            yield x+m-1, i

        for c in spiral(False, x, y+1, m-1, n-1):
            yield c
    else:
        for i in xrange(x+m-1,x-1,-1):
            yield i, y+n-1

        for i in xrange(y+n-2,y-1,-1):
            yield x, i

        for c in spiral(True, x+1, y, m-1, n-1):
            yield c


def merge_intervals(intervals):
    last = intervals[0]
    
    for c in intervals[1:]:
        if last.end >= c.start:
            last.end = max(c.end, last.end)
        else:
            yield last
            last = c

    yield last
