import random, string

def return_number():
    phone = random.randint(1000000,9999999)
    return phone
def return_name():
    size = random.randint(4,10)
    chars = string.ascii_lowercase
    name = ''.join(random.choice(chars) for x in range(size))
    return name

def gen_phoneBook()
    phone_book = []
    index = 0
    while index < 100000:
        phone = return_number()
        name = return_name()
        if phone in phone_book or name in phone_book:
            continue
        else:
            phone_book.append([phone,name])
            index += 1
    f = open('phone.txt', 'w')
    for index in phone_book:
        f.write(str(index) + '\n')
    f.close()

def gen_phoneBookFaster():
    numbers = set()
    while len(numbers) < 100000:
        phone = return_number()
        name = return_name()
        if phone in numbers or name in numbers:
            continue
        else:
            numbers.add((phone, name))
    f = open('phone_new.txt', 'w')
    for index in numbers:
        f.write(str(index) + '\n')
    f.close()

gen_phoneBookFaster()

