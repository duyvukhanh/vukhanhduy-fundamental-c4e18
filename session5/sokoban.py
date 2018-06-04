map_sokoban = {
    "sizex" : 5,
    "sizey" : 5
}
player = {
    "x" : 4,
    "y" : 0
}
boxes = [
    {"x" : 1, "y" : 1},
    {"x" : 2, "y" : 2},
    {"x" : 3, "y" : 3}
]
destinations = [
    {"x" : 2, "y" : 1},
    {"x" : 3, "y" : 2},
    {"x" : 4, "y" : 3}
]
playing = True
while playing:
    # print map
    for y in range(map_sokoban["sizey"]):
        for x in range(map_sokoban["sizex"]):
            
            
            box_is_here = False
            for box in boxes:
                if box["x"] == x and box["y"] == y:
                    box_is_here = True
                    
            player_is_here = False
            if x == player["x"] and y == player["y"]:  
                player_is_here = True

            destination_is_here = False
            for destination in destinations:
                if destination["x"] == x and destination["y"] == y:
                    destination_is_here = True


            if player_is_here:
                print("P ", end="")
            
            elif box_is_here:
                print("B ", end="")

            elif destination_is_here:
                print("D ", end="")

            else:
                print("- ", end ="")
        
        print()

    # end of print map
    # check win
    win = True
    for box in boxes:
        if box not in destinations:
            win = False
    if win == True:
        print("You win !!!")
        playing = False
    # done check win

    move = input("Your move: ").upper()
    
    dx = 0
    dy = 0
    
    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
        
    elif move == "A":
        dx = -1
        
    elif move == "D":
        dx = 1
       
    else:
        playing = False

# move player
    if 0 <= player["x"] + dx < map_sokoban["sizex"] \
    and 0 <= player["y"] + dy < map_sokoban["sizey"]:
        player["x"] += dx
        player["y"] += dy
#  move boxes   
    for box in boxes:
        if box["x"] == player["x"] and box["y"] == player["y"]:
            box["x"] += dx
            box["y"] += dy

    win = True
    for box in boxes:
        if box not in destinations:
            win = False

    
        

            
