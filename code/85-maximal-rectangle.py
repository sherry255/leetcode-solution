def maximalRectangle(matrix):
    while not matrix:
        return 0

    w = len(matrix[0])
    h = len(matrix)

    l = [[w for _ in xrange(w)] for _ in xrange(h)]
    r = [[0 for _ in xrange(w)] for _ in xrange(h)]

    rl = [[0 for _ in xrange(w)] for _ in xrange(h)]
    rr = [[w for _ in xrange(w)] for _ in xrange(h)]
    rh = [[0 for _ in xrange(w)] for _ in xrange(h)]

    largest = 0

    for y in xrange(h):
        for x in xrange(w):
            if matrix[y][x] == '1':
                l[y][x] = min(l[y][x-1] if x>0 else w, x)

        for x in xrange(w-1, -1, -1):
            if matrix[y][x] == '1':
                r[y][x] = max(r[y][x+1] if x+1<w else 0, x+1)

        for x in xrange(w):
            if matrix[y][x] == '1':
                rl[y][x] = max(rl[y-1][x] if y > 0 else 0, l[y][x])
                rr[y][x] = min(rr[y-1][x] if y > 0 else w, r[y][x])
                rh[y][x] = (rh[y-1][x] if y > 0 else 0) +1

                area = rh[y][x] * (rr[y][x]-rl[y][x])
                if area > largest:
                    largest = area

    return largest
