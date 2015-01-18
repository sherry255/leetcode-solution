"""
>>> reverse(123)
321
>>> reverse(-123)
-321
"""

from digit import int2digits, digits2int_b

def reverse(x):
    n = (-1 if (x<0) else 1) * digits2int_b(int2digits(abs(x)))
    if -2147483648 <= n <= 2147483647:
        return n
    return 0
