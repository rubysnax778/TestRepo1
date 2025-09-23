

hero_stats = {
    "name" : "hero",
    "strength" : 7,
    "health" : 100.00,

}




def player_flee():
    print("You chose to flee")
    print("GAME OVER")
    return False

def player_move():
    print("you move!")
    return

def player_attack():
    print("you atacked!")

def player_stats():
    print("You are:")
    for key, value, in hero_stats.items():
        print(f"{key} : {value}" )






isPlaying = True

while (isPlaying):

    player_stats()

    print ("START OF LOOP")

    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()

    print ("Game is running")
    print(f"Player Action: {action}")



    if (action == "flee"):
            isPlaying = quit()
    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()
    elif (action == "flee"):
        player_flee()
    else:
        print ("INVALID ACTION")
        


print ("END OF LOOP")




