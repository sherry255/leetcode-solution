def int2digits(x):
    while x:
        yield x%10
        x = x // 10

def digits2int_b(it):
    i = 0
    for d in it:
        i = i * 10 + d
    return i

def digits2int_l(it):
    r = 0
    for i, d in enumerate(it):
        r += d * (10 ** i)
    return r


def roman_int_map():
    return (
        ( 'M', 1000),
        ('CM',  900),
        ( 'D',  500),
        ('CD',  400),
        ( 'C',  100),
        ('XC',   90),
        ( 'L',   50),
        ('XL',   40),
        ( 'X',   10),
        ('IX',    9),
        ( 'V',    5),
        ('IV',    4),
        ( 'I',    1))

def _int2roman(n):
    for r, i in roman_int_map():
        yield r*(n//i)
        n = n%i

def int2roman(n):
    return "".join(_int2roman(n))

def _roman2int(s):
    for r, i in roman_int_map():
        while s.startswith(r):
            yield i
            s = s[len(r):]

def roman2int(s):
    return sum(_roman2int(s))
