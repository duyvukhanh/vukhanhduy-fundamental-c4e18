from turtle import *
color("blue")
speed(-1)
length = 100

right(140)
while length > 0:
    for i in range(4):
        forward(length)
        right(90)
    right(10)
    length -= 2

mainloop()