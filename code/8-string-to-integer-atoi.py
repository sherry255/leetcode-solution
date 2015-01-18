from digit import digits2int_b

def iter_digit(s):
    for c in s:
        if not c.isdigit():
            return
        yield int(c)

def atoi(str):
    s = str.strip()
    if not s:
        return 0

    if s[0] in '-+':
        sign = {'-':-1,'+':1}[s[0]]
        s = s[1:]
    else:
        sign = 1

    n = sign * digits2int_b(iter_digit(s))
    if n < -2147483648:
        return -2147483648
    if n > 2147483647:
        return 2147483647
    return n
