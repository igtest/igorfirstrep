def fibo(n):
        print("Начинаем вычислять число Фибоначи "+str(n))
        if n == 0: result = 0
        elif n == 1: result = 1
        else: result = fibo(n - 1) + fibo(n-2)
        return result
x = fibo(10)
print(x)
