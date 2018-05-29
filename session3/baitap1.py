print("Hi there, here you favorite things so far")
n = ["death note", "netflix", "teaching"]
for index, item in enumerate(n):
    print("{0}. {1}".format(index+1, item))
print("*" * 20)
m = int(input("position you want to update: "))
n[m-1]=input("fav u want to update: ")
for index, item in enumerate(n):
    print("{0}. {1}".format(index+1, item))