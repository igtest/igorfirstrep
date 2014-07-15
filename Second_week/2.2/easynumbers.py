def numbers(n):
    array = []
    for x in range(2,n+1):
        array.append(x)
    count_n = 0
    while True:
        p = array[0]
        count_n += 1
        if count_n>len(array):
            break
        count = 1
        while count<=len(array):
            count += 1
            key = count*p
            if key > max(array) or (key in array):
                break
            array.remove(key)
    #print(p)
    return array
x = numbers(10)
print(x)
