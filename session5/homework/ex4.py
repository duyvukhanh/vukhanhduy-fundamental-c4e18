def F(n):  
    if n == 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return F(n-1)+F(n-2)

month = int(input("Enter months: "))

x = 1
for i in range(month+1):
    x = x + F(i)
    print("Month",i,":",x," pair(s) of rabbit")