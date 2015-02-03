import random, string

AMOUNT_OF_STRING_IN_PHONEBOOK = 100000


def return_number():
    MIN_NUMBER = 1000000
    MAX_NUMBER = 9999999
    phone = random.randint(MIN_NUMBER, MAX_NUMBER)
    return phone


def return_name():
    size = random.randint(4, 10)
    chars = string.ascii_lowercase
    name = ''.join(random.choice(chars) for x in range(size))
    return name


def gen_phoneBook():
    phone_book = []
    index = 0
    while index < AMOUNT_OF_STRING_IN_PHONEBOOK:
        phone = return_number()
        name = return_name()
        if phone in phone_book or name in phone_book:
            continue
        else:
            phone_book.append([phone, name])
            index += 1
    f = open('phone.txt', 'w')
    for index in phone_book:
        f.write(str(index) + '\n')
    f.close()


def gen_phoneBookFaster():
    phone_book = set()
    while len(phone_book) < AMOUNT_OF_STRING_IN_PHONEBOOK:
        phone = return_number()
        name = return_name()
        phone_book.add((phone, name))
    f = open('phone_new.txt', 'w')
    for index in phone_book:
        f.write(str(index) + '\n')
    f.close()


gen_phoneBookFaster()

