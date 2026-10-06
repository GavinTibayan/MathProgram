# Code goes here!
import random

HWQ = int(input("How many questions do you want?:\t"))
while HWQ <= 0:
    HWQ = int(input("That is not a valid number, please type in another number.:\t"))
LN = int(input("What's the highest number?:\t"))
while LN <= 0:
    LN = int(input("That is not a valid number, please type in another number.:\t"))
SN = int(input("What's the lowest number?:\t"))
while SN <= 0:
    SN = int(input("That is not a valid number, please type in another number.:\t"))
Op = int(input("What operation do you want?:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n\t"))
while Op <= 0 or Op > 4:
    Op = int(input("That is not a valid number, please type in another number.:\t"))
x = random.randint(SN,LN)
y = random.randint(SN,LN)

# Loop:
for Question  in range(1,HMQ+1):
    print(f"Question {Question}:")
    ans = x*y
    ans = x//y