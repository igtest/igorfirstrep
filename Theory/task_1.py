def octoToDec(octoNum):
    length = len(octoNum)
    value = 0
    for x in octoNum:
        if int(x) > 7:
            return -1
        length -= 1
        value += int(x) * (8**length)
    return value
print(octoToDec('215627'))
