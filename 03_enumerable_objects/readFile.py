def readInDic():
    d = {}
    with open("phone_new.txt") as f:
        for line in f:
            number = line[1:8]
            name = line[11:-3]
            key, val = number, name
            d[key] = val
    return d


def readInTuplesList():
    lst = []
    with open("phone.txt") as f:
        for line in f:
            number = line[1:8]
            name = line[11:-3]
            lst.append((number, name))
    return lst


def readInTuplesListSort():
    lst = []
    with open("1.txt") as f:
        for line in f:
            number = line[1:8]
            name = line[11:-3]
            lst.append((number, name))
    lst.sort()
    return lst


def get_nameInDic(phone):
    book = readInDic()
    if phone in book:
        print(book[phone])
    else:
        print("The number is not exist")


def get_nameInTuplesList(phone):
    book = readInTuplesList()
    numberList = [(line[0], line[1]) for line in book if line[0] == phone]
    if numberList:
        print(numberList[0][1])
    else:
        print("The number is not exist")


def get_nameGenerator(phone):
    val = []
    book = readInTuplesList()
    numberList = ((line[0], line[1]) for line in book if line[0] == phone)
    for i in numberList:
        val = i
    if val == '[]':
        print("The number is not exist")
    else:
        print(val[1])


import time
# #get_nameInTuplesList('2253431')
##def compare_functions(f, g, v, arg):
##  i = 0
##  t1 = 0
##  t2 = 0
##  t3 = 0
##  while i < 50:
##    last_time = time.clock()
##    f(arg)
##    t1 += time.clock() - last_time
##    i += 1
##  while i < 100:
##    last_time = time.clock()
##    g(arg)
##    t2 += time.clock() - last_time
##    i += 1
##  while i < 150:
##    last_time = time.clock()
##    v(arg)
##    t3 += time.clock() - last_time
##    i += 1
##  print("1st func: " + str(t1))
##  print("2nd func: " + str(t2))
##  print("3nd func: " + str(t3))
##  print(t2 / t1)
##
##compare_functions(get_nameInDic, get_nameGenerator, get_nameInTuplesList, '7719351')
get_nameInDic('2624117')
##def get_nameInTuplesListSort(phone):
##    #book = readInTuplesList()
##    numberList = [(line[0],line[1]) for line in open("phone.txt") if line[0] == phone]
##    if numberList:
##        print(numberList[0][1])
##    else:
##        print("Not")

##get_nameInTuplesList('7535669')
