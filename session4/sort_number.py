numb_list = [10,2,-5,4]
numb_list_sorted = []

# while numb_list != []:
while True:
    minn = min(numb_list)
    numb_list_sorted.append(minn)
    numb_list.remove(minn)
    if len(numb_list) == 0:
        break
print(numb_list_sorted)





