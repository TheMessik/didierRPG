class Hero:
    # skills of our hero
    # all skills are initially 0
    constitution = 0
    strength = 0
    agility = 0
    intelligence = 0

    # starting level
    level = 1

    # jobs to increase hero's level and abilities
    # TODO: balance
    def dive(self):
       print("Hero's diving")

    def fit(self):
        print("Hero's fitting")

    def woodcutting(self):
        print("Hero's cutting wood")

    def weights(self):
        print("Hero's lifting like a crazyman")

    def archery(self):
        print("Hero's got an arrow to the knee")

    def parkour(self):
        print("Hero broke his ankle while doing parkour Office style")

    def archeology(self):
        print("Hero found out where he came from")

    def read(self):
        print("Writing is for sissies")

    def monsterhunt(self):
        print("Monster dead, I think")

    def dungeon(self):
        print("Hero dead")

    def coloseum(self, other):
        assert isinstance(other, Hero), "You either fight a hero, or you don't fight at all"


def new_hero():
    hero = Hero()
    return hero
