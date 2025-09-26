import os


#display the starting menue
def prompt():
    print("\t\t\tWelcome little adventurer!\n\n What is your name?")
    #insert name input option here

    input("Press any key to continue...")

#this clears the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


#map creation
rooms = {
    'forest of little dreams' : {'West': 'funnel canyon', 'South' : 'wish way', 'Item' : 'health potion'},
    'wish way' : {'North': 'forest of little dreams', 'East' : 'blubber cove'},
    'blubber cove' : {'West': 'wish way', 'Item' : 'key of dreams', 'Boss' : 'little whale knight'},
    'funnel canyon' : {'East': 'forest of little dreams', 'North' : 'forest of big dreams', 'Boss' : 'medium whale knight'},
    'forest of big dreams' : {'South': 'funnel canyon', 'Boss' : 'big whale knight'}
}

#list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

#track inventory
inventory = []

#track current room
current_room = "forest of little dreams"

#result of last move
msg = ""

clear()
prompt()


#gameplay loop
while True:

    clear()

    #display player info and take name
    print(f"You wake up in {current_room}\nInventory : {inventory}\n{'-' * 27}")

    #display msg
    print(msg)

    #Item indicater
    if "Item" in rooms[current_room].keys():

        nearby_Item = rooms[current_room]["Item"]

        if nearby_Item not in inventory:
            #plural
            if nearby_Item[-1] == 's':
                print(f"you see {nearby_Item}")
            #singular vowel
        elif nearby_Item[0] in vowels:
            print(f"you see an {nearby_Item}")
            #singular consanant
        else:
            print(f"you see a {nearby_Item}")

    if "Boss" in rooms[current_room].keys():

        #finding boss (add trigger upon search for boss or other actions)
        if len(inventory) <5:
            print(f"You have stumbled across {rooms[current_room]['Boss']}.")
            #break

        else:
            print(f"You do not see a {rooms[current_room]['Boss']}.")
            #break

    user_input = input("What would you like to do?:\n")

    next_move = user_input.split(' ')

#first word in action
    action = next_move[0].title()

    if len(next_move) >1:
        Item = next_move[1:]
        direction = next_move[1].title()

        Item = ' '.join(Item).title()

#Moving between rooms
    if action == "Go":


        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}"
        except:
            msg = f"You can't travel that way"

#picking up Items
    elif action == "Get":
        try:

            if Item == rooms[current_room]["Item"]:
                if Item not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    msg = f"{Item} pick up!"
                
                else:
                    msg = f"You already have {Item}."
            else:
                msg = f"Can't find {Item}"
        except:
            msg = f"Can't find {Item}"
    #exit game
    elif action == "Exit":
        break

    #any other commands
    else:
        msg = "Invalid command"

