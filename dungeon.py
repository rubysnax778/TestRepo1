





hero_stats = {
    "name" : "hero",
    "strength" : 7,
    "health" : 100.00,

}

pisscount = 0

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

def player_piss(pisscount):
    if pisscount == 0:
        print("I don't wanna")
        pisscount = 1
        return pisscount
    elif pisscount == 1:
        print("Do I have to?")
        pisscount = 2
        return pisscount
    elif pisscount == 2:
        print("a gentle warmth fills your pants, the piss is streaming")
        pisscount = 0
    return pisscount







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
    elif (action == "piss"):
        pisscount = player_piss(pisscount)
    else:
        print ("INVALID ACTION")
        


print ("END OF LOOP")




