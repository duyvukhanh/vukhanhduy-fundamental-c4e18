name = input("your full name: ")
names = name.strip().split()
split_name = []
for item in names:
    split_name.append(item.lower()) 
standard_name = " ".join(split_name)
print("Updated: ",standard_name.title())
