def sieve(n):
    array = []
    array_temp = []
    for x in range(2,n+1):
        array.append(x)
    count_n = 0
    while True:
        p = array[count_n]
        count_n += 1
        if count_n >= len(array):
            break
        count = 1
        while count<=len(array):
            count += 1
            key = count*p
            if key > max(array):
                break
            if key in array_temp:
                continue
            array_temp.append(key)
            array.remove(key)
    return array

print(sieve(1000))
