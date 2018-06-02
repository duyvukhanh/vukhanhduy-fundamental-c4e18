print("Guess your number game!")
input()
print("Think number 0-100")
input()
print("""
'c' if my guess is correct
'l' if my guess is larger
's' if my guess is smaller
""")

low = 0
high = 100
mid = (low+high)/2
while True:
    ans = input("Is {0} your number? ".format(mid)).upper()
    
    if ans == "S":
        low = mid
        mid = (high+low)//2
        
    elif ans == "L":
        high = mid
        mid = (high+low)//2
        
    elif ans == "C":
        print("I knew it")
        break
