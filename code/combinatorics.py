def product(*args):
    r = [()]
    for a in args:
        r = [x+(y,) for x in r for y in a]
    return r


def comb(l, n):
    if n == 0:
        yield ()
    else:
        for i in xrange(len(l)):
            for r in comb(l[i+1:], n-1):
                yield (l[i],) + r
