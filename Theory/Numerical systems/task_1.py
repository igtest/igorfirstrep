def octoToDec(octoNum):
    length = len(octoNum)
    value = 0
    for x in octoNum:
        if int(x) > 7:
            return -1
        length -= 1
        value += int(x) * (8**length)
    return value

def octoToDecN(octoNum):
    length = len(octoNum)
    value = 0
    for x in octoNum:
        if int(x) > 7:
            return -1
        length -= 1
        value *= 8
        value += int(x)
    return value

print(octoToDec('215627'))
print(octoToDecN('215627'))
