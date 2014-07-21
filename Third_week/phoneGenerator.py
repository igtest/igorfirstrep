import random, string

def return_number():
    phone = random.randint(1000000,9999999)
    return phone
def return_name():
    size = random.randint(4,10)
    chars = string.ascii_lowercase
    name = ''.join(random.choice(chars) for x in range(size))
    return name

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
