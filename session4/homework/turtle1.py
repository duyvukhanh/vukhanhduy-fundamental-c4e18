from turtle import *
color("blue")
speed(-1)

for i in range(24):
    for i in range(2):
        forward(50)
        left(90)
    for i in range(3):
        forward(100)
        left(90)
    forward(50)
    left(90)
    forward(50)
    left(15)

mainloop()