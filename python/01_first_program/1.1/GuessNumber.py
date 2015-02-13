import random

randomInt = random.randint(0, 100)

print("I think of a number...Guess!")

flag = 0
count = 0
while flag == 0:
    print("Input your value: ")
    count += 1
    value = input()
    s = int(value)
    # print(s)
    if s > randomInt:
        print("Your value is bigger")
        continue
    if s < randomInt:
        print("Your value is less")
        continue
    if s == randomInt:
        print("You are guess!")
        flag = 1

print("I think of a number " + repr(randomInt))
print("You made " + repr(count) + " attempts")

