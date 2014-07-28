def to_octo(x):
    res = ""
    while x:
        res += str(x%8)
        x //= 8
    return res[::-1]
