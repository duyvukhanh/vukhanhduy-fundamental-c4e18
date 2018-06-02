numbers = input("Nhap day so cach nhau boi dau cach : ")
numberss = numbers.strip().split()
# numberss = list(map(int, numberss))
number_list = []
for item in numberss:
    number_list.append(int(item))
print(number_list)
a = []
is_softed = True
for i in range(len(number_list)-1):
    if number_list[i] > number_list[i+1]:
        is_softed = False
        
        while True:
            minn = min(number_list)
            a.append(minn)
            number_list.remove(minn)
            if len(number_list) == 0:
        
                print(a)
        break
if is_softed:
    print("Sap xep roi")    
else:
    print("Chua sap xep")
        
