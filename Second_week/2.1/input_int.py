def input_int(a,b):
        downLimit = a
        upLimit = b
        while True:
                x = input("Input value between " +str(downLimit)+" and "+ str(upLimit)+"\n")
                if not x.isdigit():
                        continue
                else: x = int(x)
                if x > downLimit and x < upLimit:
                        return x
                else:
                        continue
d = input_int(10,20)
print(d)
