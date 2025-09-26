

#Character ----> Hero
#         ¦_____Enemy



from character import Character

class Hero (Character):
    def __init__(self):
        super().__init__()
        #self.max_health = 100.0(moved)

        #move this var later vv
        self.health_potion_str = 5


        self.stats = {
            "name" : "Hero",
            "strength" : 7,
            "health" : 100.00,

        }

        self.inventory = ["sword", "health potion", "rope"]
    def print_stats(self):
        print("Your stats are: ")
        for key, value in self.stats.items():
            print(f"{key}, {value}")


    def set_name(self, name):
        self.stats["name"] = name
        self.print_stats()

    def move(self):
        pass

    def attack(self):
        pass

    def take_damage(self, damage):
        self.stats["health"] = self.stats["health"] - damage
        print (f"Your health is now {self.stats['health']}")


    def heal(self, item_name):
        if (self.inventory.count ("health potion") <= 0):
            print (f"You don't have any {item_name}")
            return
        
        print(f"You'be used a {item_name}, you've restored {self.health_potion_str} Health")
        if (self.stats["health"] >= self.max_health):
            print("You've reached max health!")
            self.stats["health"] = self.max_health

    def use_item(self):
        pass




hero = Hero()

hero.set_name("Ruby")
hero.print_stats()
hero.

#print(f"Here are your Hero Stats {player.stats}")