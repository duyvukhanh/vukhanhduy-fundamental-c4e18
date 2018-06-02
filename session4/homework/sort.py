number_list = [1,5,2,4,3,6,8,7,9,-5]

for i in range (len(number_list)-1,0,-1):
    for j in range(i):
        if number_list[j] > number_list[j+1]:
            number_list[j], number_list[j+1] = number_list[j+1], number_list[j]
print(number_list)
