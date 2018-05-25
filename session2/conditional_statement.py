yob = int(input("Nam sinh: "))
age = 2018 - yob
if age < 10:
    print("baby")
elif age <= 18:
    print("Teenager")
elif age==24:
    print("Lay chong thoi")
else:
    print("Not baby")
print("Pye")