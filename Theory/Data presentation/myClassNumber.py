from itertools import zip_longest
class Number:
    def __init__(self, numiration, registers):
        self.registers = []
        self.numiration = numiration
        for x in registers:
            if x >= self.numiration:
                raise ValueError("Register value more than " + str(self.numiration))
            self.registers.append(x)

    def __add__(self, other):
        overflow = False
        result = []
        for x, y in zip_longest(self.registers, other.registers):
            r = x + y 
            if overflow: 
                r += 1
                overflow = False
            if r >= self.numiration: 
                r -= self.numiration 
                overflow = True 
            result.append(r) 
        if overflow: 
            result.append(1) 
        return Number(self.numiration,result)

    def __sub__(self,other):
        overflow = False
        result = []
        for x, y in zip_longest(self.registers, other.registers):
            if x < y:
                raise ValueError("First number less than seconde")
            r = x - y
            overflow = False
            if r >= self.numiration:
                r -= self.numiration
                overflow = True
            result.append(r)
        if overflow:
            result.append(1)
        return Number(self.numiration, result)
    def __mul__(self, other):
        overflow = False
        result = []
        count = 0
        for x, y in zip_longest(self.registers, other.registers):
            r = x*y
            overflow = False
            while r >= self.numiration:
                r -= self.numiration
                count += 1
                overflow = True
            result.append(r)
        if overflow:
            result.append(count)
        return Number(self.numiration, result)
    def __floordiv__(self, other):
        overflow = False
        result = []
        for x, y in zip_longest(self.registers, other.registers):
            if y == 0:
                raise ValueError("Devision by zero")
            r = x//y
            overflow = False
            if r >= self.numiration:
                r -= self.numiration
                overflow = True
            result.append(r)
        if overflow:
            result.append(1)
        return Number(self.numiration, result)

n = Number(256,(3,255))
y = Number(256,(2,3))
z = y + n
a = n - y
d = n*y
s = n//y
print(z.registers)
print(a.registers)
print(d.registers)
print(s.registers)
