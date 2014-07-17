def input_int(downLimit,upLimit):
        while True:
                x = input("Input value between " +str(downLimit)+" and "+ str(upLimit)+"\n")
                if x.isdigit():
                        x = int(x)
                else:
                        continue
                if x > downLimit and x < upLimit:
                        return x
                else:
                        continue
d = input_int(10,20)
print(d)
