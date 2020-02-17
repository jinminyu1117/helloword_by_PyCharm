import math
num = int(input("Please input a number:"))
try:
    print(math.sqrt(num))
except:
    print("Bad number")
    print("You must input an abslute number")
    print(math.sqrt(abs(num)))
