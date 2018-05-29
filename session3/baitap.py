print("Hi there, here you favorite things so far")
n = ["death note", "netflix", "teaching"]
print(*n, sep=",")
m = input("name one thing u want to add: ")
n.append(m)
print(*n, sep=",")