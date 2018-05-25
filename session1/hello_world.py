# print("Hello")
# name = input("What's your name?")
# print("Hi",name)
# year = int(input("Ban sinh nam bao nhieu?"))
# age = 2018 - year
# print("tuoi la",age)

canh = int(input("nhap so canh"))
from turtle import *
speed(-1)
shape("turtle")
color("green")

# fillcolor("green")
# begin_fill()

for i in range(canh):
    forward(100)
    left(360/canh)

# for i in range(canh):
    # forward(100)
    # left(90)   
    # forward(100)
    # left(90)
    # forward(100)
    # left(90)
    # forward(100)
    # left(90)
    # right(7)
# end_fill()

mainloop()

