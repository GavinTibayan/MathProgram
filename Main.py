# Code goes here!
import random
final = int(0)
HWQ = int(input("How many questions do you want?:\t"))
while HWQ <= 0:
    HWQ = int(input("That is not a valid number, please type in another number.:\t"))
final2 = HWQ
LN = int(input("What's the highest number?:\t"))
while LN <= 0:
    LN = int(input("That is not a valid number, please type in another number.:\t"))
SN = int(input("What's the lowest number?:\t"))
while SN <= 0:
    SN = int(input("That is not a valid number, please type in another number.:\t"))
Op = int(input("What operation do you want?:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n\t"))
while Op <= 0 or Op > 4:
    Op = int(input("That is not a valid number, please type in another number.:\t"))
# Loop:
while HWQ > 0:
    HWQ = HWQ - 1
    print(f"Question:")
    if Op == 1:
        x = random.randint(SN, LN)
        y = random.randint(SN, LN)
        ans = x+y
        print(f"{x} + {y} = ?")
        Uans = int(input())
        if Uans == ans:
            print("Correct!")
            final = int(final+1)
        else:
            print("Incorrect:")
    if Op == 2:
        x = random.randint(SN, LN)
        y = random.randint(SN, LN)
        ans = x-y
        print(f"{x} - {y} = ?")
        Uans = int(input())
        if Uans == ans:
            print("Correct!")
            final = int(final+1)
        else:
            print("Incorrect:")
    if Op == 3:
        x = random.randint(SN, LN)
        y = random.randint(SN, LN)
        ans = x*y
        print(f"{x} * {y} = ?")
        Uans = int(input())
        if Uans == ans:
            print("Correct!")
            final = int(final+1)
        else:
            print("Incorrect:")
    if Op == 4:
        x = random.randint(SN, LN)
        y = random.randint(SN, LN)
        x = x*y
        ans = x//y
        print(f"{x} // {y} = ?")
        Uans = int(input())
        if Uans == ans:
            print("Correct!")
            final = int(final +1)
        else:
            print("Incorrect:")
print("You got",final,"/",final2,"questions correct!")
