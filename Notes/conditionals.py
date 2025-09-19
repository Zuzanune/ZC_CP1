# ZC 1st Conditionals Notes
import random
player_hp = 20
player_dex = 4
player_attack = 3
player_damage = random.randint(2,6)
monster_hp = 15
monster_attack = 3
monster_damage = random.randint(1,3)
monster_dex = 2
hit_roll = random.randint(1,20) + player_attack

if hit_roll >= 10 + monster_dex:
    print ("you hit! roll for damage")
    damage_roll = random.randint(2,7) + player_damage
    print (f"you did {damage_roll} damage")
else:
    print ("darn, you missed")


