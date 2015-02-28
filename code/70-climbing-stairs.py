def climbStairs(n):
    a, b = 0, 1
    for i in xrange(n):
        a, b = b, a+b
    return b
