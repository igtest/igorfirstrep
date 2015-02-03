def easynumbers(n):
    """
    Return a list of Prime numbers
    """
    array = []
    array_temp = []
    for x in range(2, n + 1):
        array.append(x)
    count_n = 0
    while True:
        p = array[count_n]
        count_n += 1
        if count_n >= len(array):
            break
        count = 1
        while count <= len(array):
            count += 1
            key = count * p
            if key > max(array):
                break
            if key in array_temp:
                continue
            array_temp.append(key)
            array.remove(key)
    # print(p)
    return array


def maximum_prime(n):
    """
    Return the biggest Prime number
    """
    maxNum = 0
    x = easynumbers(n)
    for i in x:
        if n % i == 0:
            maxNum = i
    return maxNum


x = maximum_prime(70)
print(x)
