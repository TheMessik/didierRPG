from didierRPG.Hero import Hero
from didierRPG.Item import Item

hero = Hero("Jozko")
hero.save_state()

print(hero)
print(hero.skills)
print(hero.equipment)

hero.load_state("Jozko")

sword = Item("testSword", dict(), "hand")

hero.equip(sword)

print(hero.equipped())
hero.save_state()

