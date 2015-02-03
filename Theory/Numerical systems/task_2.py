def to_binary(x):
    res = ""
    while x:
        res += str(x % 2)
        x //= 2

    if len(res) == 1:
        res += "000"
    elif len(res) == 2:
        res += "00"
    elif len(res) == 3:
        res += "0"

    return res[::-1]


def to_baseSeven(x):
    res = ""
    while x:
        res += str(x % 7)
        x //= 7
    return res[::-1]


def binToDec(binNum):
    length = len(binNum)
    value = 0
    for x in binNum:
        if int(x) > 2:
            return -1
        length -= 1
        value += int(x) * (2 ** length)
    return value


def chr_to_num(x):
    x = ord(x)
    if ord("0") <= x <= ord("9"):
        return x - ord("0")
    elif ord("a") <= x <= ord("f"):
        return x - ord("a") + 10
    else:
        return -1


def hexToSeven(hexNum):
    length = len(hexNum)
    value = ""
    for x in hexNum:
        num = chr_to_num(x)
        if int(num) >= 0:
            value += to_binary(num)
        elif int(num) == -1:
            return "Bad value"
    return to_baseSeven(binToDec(value))


print(hexToSeven("1a251ae"))
