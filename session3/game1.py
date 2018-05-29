from random import randint
n = randint(0,100)
loop = True
count = 0
while loop:
    if count < 7:
        m = int(input("Guess my number:"))
        if m < n:
            print("Be qua")
        elif m > n:
            print("To qua")
        else:
            print("Bingo")
            loop = False
        count += 1
    else:
        print("Het luot doan roi nhok")
        loop = False

        

