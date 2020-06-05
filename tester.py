from didierRPG.Hero import *

print("Hello World")
hero = Hero("Jozko")

print(hero)
print(hero.name)
print(hero.strength)

hero.save_state()

hero2 = Hero(None).load_state("Jozko")
print(hero2.name)
print(hero2.strength)

