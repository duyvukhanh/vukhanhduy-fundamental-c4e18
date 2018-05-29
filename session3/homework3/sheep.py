ship_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Hello my name is Duy and these are my ship sizes")
print(ship_sizes)
biggest = ship_sizes[0]
biggest_index = 0
total = 0
for i in range(len(ship_sizes)):
        if ship_sizes[i] > biggest:
            biggest = ship_sizes[i]
            biggest_index = i
print("Now my biggest sheep has size",biggest,"let's shear it")
ship_sizes[biggest_index] = 8
print("After shearing, here is my flock")
print(ship_sizes)
for j in range(4):
    print("MONTH",j+1)
    biggest = ship_sizes[0]
    biggest_index = 0
    for i in range(len(ship_sizes)):
        ship_sizes[i] = ship_sizes[i] + 50
    print("1 month has passed, now here is my flock")
    print(ship_sizes)
    for i in range(len(ship_sizes)):
        total = total + ship_sizes[i]
    print("My flock has size in total:",total)
    print("i would get",total,"* 2$ =",total*2,"$")
    for i in range(len(ship_sizes)):
        if ship_sizes[i] > biggest:
            biggest = ship_sizes[i]
            biggest_index = i
    print("Now my biggest sheep has size",biggest,"let's shear it")
    ship_sizes[biggest_index] = 8
    print("After shearing, here is my flock")
    print(ship_sizes)
    print()
    print()

