numb = int(input("Enter number: "))
prime = True
for i in range(2,numb):
    if numb % i == 0:
        prime = False
        break
if prime == True:
    print("Prime")
else:
    print("Not prime")