from random import randint
n = randint(0,100)

loop = True
while loop:
    m = int(input("Guess my number:"))
    if m < n:
        print("small")
        
        
    elif m > n:
        print(" big")
        
       
    else:
        print("Bingo")
        loop = False
        

