



hero_stats = {
    "name" : "hero",
    "strength" : 7,
    "health" : 100.00,

}

hero_max_health = 100.0

health_potion_str = 5
hero_inventory = ["sword", "health potion", "rope"]

pisscount = 0

#player functions

def player_heal(item_name):

    if (hero_inventory.count({item_name}) <= 0):
        print(f"You don't have any {item_name}(s)")
        return

    print (f"you've used a {item_name}, you've restored {health_potion_str}")
    hero_stats["health"] = hero_stats["health"] + health_potion_str

# Health maxxed at 100.0
# Use health potion
# Keep health potion is already at max health

    if (hero_stats["health"] >= hero_max_health):
        hero_stats["health"] = hero_max_health
        print ("You've reached Max Health!")
        print(f"your health is now {hero_stats['health']}")
        hero_inventory.remove("health potion")
        print(f"your inventory is now {hero_inventory}")


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


def player_griddy():
    print("omg  I'm witaly gwiddying wight now")
    return False


def player_backflip():
    print("you backflip in place for no reason. good job leon kennedy.")
    return False


def use_item():
    item_name = input(f"What item do you want to use? {hero_inventory}\n")
    print (f"The item you want to use is {item_name}")
    match item_name:
        case "sword":
            pass
        case "health potion":
            player_heal(item_name)
        case "rope":
            pass
        case _:
            print(f"{item_name} is not in your")


#temp functions
def damage_player():
    hero_stats["health"] = hero_stats["health"] - 10
    print(f"Your health is now {hero_stats['health']}")







isPlaying = True

hero_stats["name"] = input("what is your name>\n")
player_stats()

while (isPlaying):


    #print ("START OF LOOP")

    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()

    print ("Game is running")
    print(f"Player Action: {action}")



    if (action == "flee"):
            isPlaying = quit()
    elif (action == "attack"):
        player_attack()
    elif (action == "move"):
        player_move()
    elif (action == "use"):
        use_item()
    elif (action == "flee"):
        player_flee()
    elif (action == "piss"):
        pisscount = player_piss(pisscount)
    elif (action == "griddy"):
        pisscount = player_griddy()
    elif (action == "backflip"):
        pisscount = player_backflip()
    else:
        print ("INVALID ACTION")
        


#print ("END OF LOOP")




