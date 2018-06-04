numb = int(input("How many B Bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))
rep = 1
for i in range(time//2):
    rep = rep * 2
bacterias = numb * rep 

print("After",time,"minutes, we would have",bacterias,"bacterias")