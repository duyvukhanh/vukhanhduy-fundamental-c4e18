from turtle import *
speed(-1)
shape("turtle")
length = 100
for i in range(3, 7, 1):
    if i % 2 == 0:
        color("red")
        for j in range(i):
            forward(100)
            left(360/i)
            length += 20
    else:
        color("blue")
        for j in range(i):
            forward(100)
            left(360/i)
            length += 20
mainloop()