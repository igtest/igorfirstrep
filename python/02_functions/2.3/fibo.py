def fibo_show(n):
    """
    Function shows recursive method
    """
    print("Begin to calculate Fibonacci numbers " + str(n))
    if n == 0:
        result = 0
        print(result)
    elif n == 1:
        result = 1
        print(result)
    else:
        result = fibo_show(n - 1) + fibo_show(n - 2)
        print(result)
    return result


x = fibo_show(5)
# print(x)
