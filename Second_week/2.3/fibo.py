def fibo(n):
        print("Начинаем вычислять число Фибоначи "+str(n))
        if n == 0:
                result = 0
                print(result)
        elif n == 1:
                result = 1
                print(result)
        else:
                result = fibo(n - 1) + fibo(n-2)
                print(result)
        return result
x = fibo(5)
#print(x)
