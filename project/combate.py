#ZC 1st combate simulater
import random
enemy_names = ["Goblin", "red sludge", "skeleton", "zombie", "kobald", "wrath", "Boss"]
boss_names = ["Death Lord", "Red Dragon", "Champion", "Demon Lord", "Bone Mass", "Goblin boss"]
difficulty = 10
user_HP = random.randint(20,40)
user_AC = 10
healing_potions = 3
user_STR = random.randint(8, 12)
user_DEX = random.randint(8,12)
user_SS = random.randint(0,1)
mon_HP = random.randint(1, difficulty)
mon_AC = random.randint(8 + int(difficulty/10), 10 + int(difficulty/10))
mon_STR = random.randint(8,17)
mon_DEX = random.randint(7, 15)
print ("Ho there adventurer! what might be your name?")
user_name = input()
print ("what class might you be")
uclass= input("choose fighter, rouge, or wizard:  ")
if uclass == "fighter" or "Fighter":
    user_crit_chance = [19, 20]
    user_damage = 20
    user_AC += 2
    user_HP += 15
    user_STR += 5
elif uclass == "rouge" or "Rouge":
  user_crit_chance = [18,19,20]
    user_damage = 15
    user_AC += 1
    user_HP += 5
    user_DEX += 5
    user_AC += (user_DEX - 10)/2
else:
  user_crit_chance = [20]
    user_damage = 6
    user_AC -= 1
    user_DEX +2
    user_SS += 5
    user_HP -= random.randint(2, 12)
max_hp = user_HP
print (f"you have STR {user_STR}, DEX {user_DEX}, AC {user_AC} and {user_HP} health.")
if user_SS > 0:
    print (f"you also have {user_SS} spell slots")
enemy = random.choice(enemy_names)
if enemy == "Boss":
    mon_HP += random.randint(10, 30)
    mon_AC += random.randint(0,5)
    mon_STR += random.randint(0,5)
    mon_DEX += random.randint(0,5)
    enemy = random.choice(boss_names)
if enemy in boss_names:
    print (f"a boss aproaches, expect an epic fight. The {enemy} has entered the battlefield")
print (f"an enemy aproaches. you spot a {enemy}")
def userTurn():
  print ("your turn! would you like to attack, dodge, use magic, or drink one of your healing potions")
  user_action = input("enter Attack, Dodge, Spell, or Heal")
  if user_action.lower() == "attack":
      print ("you attack!!")
      user_attack = random.randint(1,20)
      attack_damage = (random.randint(1,user_damage) + user_STR/2
      if user_attack in user_crit_chance:
              print ("you crit!")
              user_damage *= 2
              user_attack = 100
      if user_attack > mon_AC:
          print (f"You Hit! you deal {user_damage} damage to the {enemy}")
          mon_HP -= user_damage
      if user attack == 1:
          print ("darn, you injure yourself while attacking. take one damage.")
          user_HP -= 1
  elif user_action.lower() == "dodge":
      dodge = True
      print ("you dodge!")
  elif user_action.lower() == "spell":
    if user_SS > 0
      print ("choose a spell from Fireball, Cure wounds, magic missile, and thunderwave")
      spell_choice = input()
      if spell_choice.lower == "fireball":
          user_SS -= 1:
          attack_damage = random.randint(20,40)
          print ("you hit the {enemy} for {attack_damage} damage!")
          mon_HP -= attack_damage
      elif spell_choice.lower == "cure wounds":
          user_SS -= 1
          print ("you cast cure wounds! and regain 2d8 health")
          user_HP += random.randint(2,16)
          if user_HP > max_hp:
              user_HP = max_hp
mon_ini = 10 + ((mon_DEX/10))
player_ini = 10 + ((user_DEX/10))
if player_ini > mon_ini:
    print ("you go first!")
    Player_first = True
else:
    print ("the monster does first!")
    mon_first = True
    
