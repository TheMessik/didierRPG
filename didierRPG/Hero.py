import json
import math


class Hero:
    def __init__(self, name):
        self.name = name

    name = ""
    # skills of our hero
    # all skills are initially 0
    skills = {
        "constitution": 0,
        "strength": 0,
        "agility": 0,
        "intelligence": 0
    }

    skills_improve_mult = {
        "constitution": 0,
        "strength": 0,
        "agility": 0,
        "intelligence": 0
    }

    skills_improve_offset = {
        "constitution": 0,
        "strength": 0,
        "agility": 0,
        "intelligence": 0
    }

    skills_use_mult = {
        "constitution": 0,
        "strength": 0,
        "agility": 0,
        "intelligence": 0
    }

    skills_use_offset = {
        "constitution": 0,
        "strength": 0,
        "agility": 0,
        "intelligence": 0
    }

    # starting level
    experience = 0

    # inventory stuff
    # hero has initially no gear
    # can equip items using equip(Item)
    equipment = {
        "helmet": None,
        "chestplate": None,
        "pants": None,
        "hand": None,
        "spell": None
    }

    inventory = []

    # ripped from skyrim, bite me
    def get_level(self):
        return math.floor(-2.5 + math.sqrt(8 * self.experience + 1225) / 10)

    def level_up(self, skill, skill_use_mult, skill_use_offset):
        self.experience += skill_use_mult + skill_use_offset
        cost = self.cost_next_level(skill)

        if self.experience >= cost:
            self.skills[skill] += 1

    def cost_next_level(self, skill):
        return self.skills_improve_mult[skill] * math.pow(self.skills[skill] - 1, 1.95) \
               + self.skills_improve_offset[skill]


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
        skill_improve_mult = 2
        skill_improve_offset = 0

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

    # inventory methods
    def equip(self, item):
        self.equipment[item.type_of_item] = item

    def equipped(self):
        return self.equipment

    def show_inventory(self):
        return self.inventory





    # hero creation and loading
    def new_hero(self, name):
        hero = Hero(name)
        return hero

    def save_state(self):
        data = {
            "name": self.name,
            "constitution": self.skills["constitution"],
            "strength": self.skills["strength"],
            "agility": self.skills["agility"],
            "intelligence": self.skills["intelligence"],
            "level": self.level
        }

        with open(f"didierRPG/hero_data/{self.name}", "w") as file:
            json.dump(data, file, indent=4)

    def load_state(self, name):
        with open(f"didierRPG/hero_data/{name}", "r") as file:
            data = json.load(file)
            self.name = data["name"]
            self.skills["constitution"] = data["constitution"]
            self.skills["strength"] = data["strength"]
            self.skills["agility"] = data["agility"]
            self.skills["intelligence"] = data["intelligence"]
            self.level = data["level"]

        return self
