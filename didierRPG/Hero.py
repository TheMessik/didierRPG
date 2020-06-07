import json


class Hero:
    name = ""
    # skills of our hero
    # all skills are initially 0
    constitution = 0
    strength = 0
    agility = 0
    intelligence = 0

    # inventory stuff
    # hero has initially no gear
    helmet = ""
    chest_plate = ""
    pants = ""
    left_hand = ""
    right_hand = ""
    spell = ""

    inventory = []


    # starting level
    level = 1

    def __init__(self, name):
        self.name = name

    # jobs to increase hero's level and abilities
    # TODO: balance
    def dive(self):
        """chance for a dinks drop and a slight xp increase for Constitution"""
        print("Hero's diving")

    def fit(self):
        """xp increase for Constitution"""
        print("Hero's fitting")

    def woodcutting(self):
        """chance for a dinks drop and slight xp increase for Strength"""
        print("Hero's cutting wood")

    def weights(self):
        """xp increase for Strength"""
        print("Hero's lifting like a crazyman")

    def archery(self):
        """chance for a dinks drop and slight xp increase for Agility"""
        print("Hero's got an arrow to the knee")

    def parkour(self):
        """xp increase for Agility"""
        print("Hero broke his ankle while doing parkour Office style")

    def archeology(self):
        """chance for a dinks drop and slight xp increase for Intelligence"""
        print("Hero found out where he came from")

    def read(self):
        """xp increase for Intelligence"""
        print("Writing is for sissies")

    def monsterhunt(self):
        """dinks drop and xp increase, based on the stats"""
        print("Monster dead, I think")

    def dungeon(self):
        """basically monsterhunt, but harder, with higher rewards"""
        print("Hero dead")

    def coloseum(self, other, wager):
        """ challenge other hero, with a wager"""
        assert isinstance(other, Hero), "You either fight a hero, or you don't fight at all"

    # inventory





    # hero creation and loading
    def new_hero(self, name):
        hero = Hero(name)
        return hero

    def save_state(self):
        data = {
            "name": self.name,
            "constitution": self.constitution,
            "strength": self.strength,
            "agility": self.agility,
            "intelligence": self.intelligence,
            "level": self.level
        }

        with open(f"didierRPG/hero_data/{self.name}", "w") as file:
            json.dump(data, file, indent=4)

    def load_state(self, name):
        with open(f"didierRPG/hero_data/{name}", "r") as file:
            data = json.load(file)
            self.name = data["name"]
            self.constitution = data["constitution"]
            self.strength = data["strength"]
            self.agility = data["agility"]
            self.intelligence = data["intelligence"]
            self.level = data["level"]

        return self
