# ZC 1st Conditionals Notes
import random
player_hp = 20
player_dex = 4
player_attack = 7
player_damage = 2
monster_hp = 15
monster_attack = 3
monster_damage = random.randint(1,3)
monster_dex = 2
hit_roll = random.randint(1,20) + player_attack
crit = 20 + player_attack

if hit_roll >= 10 + monster_dex:
    print ("you hit! roll for damage")
    damage_roll = random.randint(2,7) + player_damage
    print (f"you did {damage_roll} damage")
elif hit_roll == crit:
    print ("you crit! that means you roll for damage twice")
    crit_damage_roll1 = random.randint(2,7) + player_damage
    crit_damage_roll2 = random.randint(2,7)
    critdamage = crit_damage_roll1 + crit_damage_roll2
    print (f"you did {critdamage} damage. Nice crit!")
else:
    print ("darn, you missed")
print ("your turn is over")


