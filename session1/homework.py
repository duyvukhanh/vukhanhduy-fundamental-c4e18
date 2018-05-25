
# #Calculates the area of the circle
# Radius = int(input("Radius?: "))
# Area = Radius ** 2 * 3.14
# print("Area ",Area) 
# ######
# #Convert Celsius to Fahrenheit
# C = int(input("Enter the temperature in Celsius: "))
# F = C * 1.8 + 32
# print(C,"(C) =",F,"(F)")
# ######
# #turtle exercise
from turtle import *
speed(-1)
shape("turtle")
color("green")
fillcolor("yellow")
# #draw a square
# begin_fill()
# for i in range(4):
#     forward(100)
#     left(90)
# end_fill()
# ######
# #draw a equilateral triangle
# begin_fill()
# for i in range(3):
#     forward(100)
#     left(120)
# end_fill()
# ######
# #Draw a circle
# begin_fill()
# circle(50)
# end_fill()
# ######
#Draw multi circle
for i in range(36):
    circle(50)
    left(10)


mainloop()
        
