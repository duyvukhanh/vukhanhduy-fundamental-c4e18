# for i in range(6):
#     print(" "*(6-i),"*"*i)



# print("*"*5)
# for i in range(5):
#     for j in range(5):


# for i in range(5):
#     for j in range(5):
#         print(" "*(j-1),"*"*j)
#     print()
      

for i in range(10):
    for j in range(10):
        if  j <= 10 - i -1:
            print(" ", end="")
        else:
            print("*", end="")
    print()