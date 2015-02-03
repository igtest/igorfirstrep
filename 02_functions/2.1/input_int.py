def input_int():
    """
    Read a string from standard input if its value into limits
    """
    downLimit = 10
    upLimit = 20
    while True:
        x = input("Input value between " + str(downLimit) + " and " + str(upLimit) + "\n")
        if x.isdigit():
            x = int(x)
        else:
            continue
        if x > downLimit and x < upLimit:
            return x
        else:
            continue

d = input_int()
print(d)
input()