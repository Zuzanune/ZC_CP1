#ZC 1st Finals text adventure game
import random as r
import time as t
talking = [
    'Did you hear it last night? That cold wind from the old keep… I swear it carried whispers again.',
    'If the lich really has awoken, then the council better do something soon. My chickens haven\'t laid a normal egg in days.',
    'I miss when the scariest thing around here was old Marla\'s stew.',
    'They say the lich\'s eyes burn like ghost-fire. I don\'t plan to get close enough to find out.',
    'Business is terrible lately. Hard to sell bread when everyone\'s too frightened to eat.',
    'The blacksmith\'s boy swears he saw undead soldiers marching in the fog. Probably imagination… probably.',
    'If you\'re heading toward the keep, at least buy a charm or two. Can\'t hurt. Might save your soul.',
    'The well water tastes strange lately. Folks blame the lich for everything, but this time? I\'m starting to think they\'re right.',
    'The mayor says there\'s nothing to fear. That\'s how you know there\'s definitely something to fear.',
    'Strangers like you don\'t usually come through anymore. Too dangerous, they say. But maybe you\'re made of sterner stuff.',
    'We used to have festivals this time of year. Now we just lock our doors and pray till morning.',
    'My cousin tried to hunt near the old keep. Came back pale as bone and refuses to speak a word.',
    'Heroes always talk big until they see the necrotic glow on the horizon. Then they turn right back around.',
    'If you find yourself hearing bells at midnight… don\'t answer. They say it\'s the lich calling wandering souls.',
    'The apothecary\'s been selling out of courage potions. Shame they\'re just mint tea.']
descriptions = [
    """You step into Broken Stones, boots crunching on the uneven cobblestone fragments that give the village its name. 
A cool wind snakes between the leaning timber homes, carrying the smell of woodsmoke and damp earth. 
Villagers cast you quick, measuring glances—some wary, some hopeful—as if trying to decide whether you’re trouble or salvation.""",

    """The village of Broken Stones unfolds before you like an old, half-forgotten tale. 
Moss-covered stone shards jut from the ground like ancient teeth, and lanterns flicker along the crooked paths. 
You arrive quietly, and few take notice—just a nod here, a muttered greeting there—as though they assume you were always meant to find this place.""",

    """With confident strides you enter Broken Stones, a rugged settlement carved from ruin and resilience. 
The shattered stones that litter the streets glint faintly beneath the sun, remnants of some long-ago calamity. 
Locals pause their work as you pass, curiosity lighting their eyes—heroes don’t often arrive in a village like this.""",

    """You stumble into Broken Stones after what feels like hours of wandering. 
The village is a patchwork of crumbled stone, crooked huts, and stubborn shrubs clinging to life. 
A thin mist curls around your feet. 
For a moment you stand there uncertain, an outsider washed up in a place where even the buildings look lost."""
]
Monsters = { "goblin" : {"health" : 11, "AC" : 10, "damage" : 6, "undead" : False }, "skeleton" : {"health" : 15, "AC" : 14, "damage" : 6, "undead" : True},"zombie" : {"health" : 13, "AC" : 11, "damage" : 6, "undead" : True}, "ochre jelly" : {"health" : 25, "AC" : 9, "damage" : 10, "undead" : False },  "undead knight": {"health" : 50, "AC" : 18, "damage" : 12, "undead" : True}, "Veyzrath": {"health" : 100, "AC" : 15, "damage": 12, "undead" : True} }
Enemies = ["goblin","goblin", "skeleton", "skeleton", "ochre jelly","zombie","zombie"]
weapon_damage_die = {"club" : 4, "dagger" : 4, "shortsword" : 6, "longsword" : 8, "greatsword" : 6, "greataxe" : 12, "staff" : 4, "fists" : 1, "sword of light" : 6}
weapon_damage_die_amounts = {"club" : 1, "dagger" : 1, "shortsword" : 1, "longsword" : 1, "greatsword" : 2, "greataxe" : 1, "staff" : 1, "fists" : 1, "sword of light" : 3}
player_STR = r.randint(-1,2)
player_DEX = r.randint(-1,2)
player_INT = r.randint(-1,2)
player_CHA = r.randint(-1,2)
player_AC = 10
player_HP = 9
first_chest_stat = True
dining_longsword = True
empty_ambush = True
guard_encounter = True
TaSS = True
gold = r.randint(30,50)
player_SS = r.randint(0,1)
player_crit_roll = [20]
inventory = []
healing_potions = 2
print (" A gruff man carrying a club walks up to you. \"I hear you are the new aventurer coming to the town to cull the lich. what is your name?\"")
nask = input()
print (f"""\"{nask}. I am Lorin, the head guard of this town\"
        he rolls his club in his hand \"
        let me give you a quick sumary of our situation. the lich Veyzrath has taken over a small keep and is terrorising the civilians.
        thank you for coming to our humble town. i hope you fare better then the many before you.""")
print (f"what class of adventuer are you {nask}?")
clask = input("choose wizard, fighter, rouge, or barbarian:  ").lower().strip()
if clask == "wizard":
    player_STR -= 2
    player_DEX += 1
    player_INT += 6
    player_CHA += 1
    player_HP += 3
    player_HP += player_STR
    inventory.append("staff")
elif clask == "fighter":
    player_STR += 4
    player_DEX += 2
    player_CHA += 2
    player_AC += 2
    player_HP += 10
    player_HP += player_STR
    inventory.append("shortsword")
    inventory.append("longsword")
elif clask == "rouge":
    player_STR -= 1
    player_DEX += 6
    player_INT += 1
    player_CHA += 3
    player_HP += 7
    player_HP += player_STR
    inventory.append("dagger")
    inventory.append("dagger")
elif clask == "barbarian":
    player_STR += 6
    player_DEX -= 1
    player_INT -= 3
    player_CHA += 3
    player_HP += 20
    inventory.append("greataxe")
    player_AC += round(player_STR/2, 1)
player_AC += player_DEX
player_SS = player_INT
max_HP = player_HP
if player_SS < 0:
    player_SS = 0
if player_STR >= player_DEX:
    primary_ability = player_STR
else:
    primary_ability = player_DEX
print (f"\"nice to meet you, {nask}. I hope you will free our small town from the horrible Veyzrath\" \n{t.sleep(0.5)} i want to give you a idea of the dungeon shape. if you just continue forward, you will reach veyzraths throne hall \n,{t.sleep(1)} but i would recomend gaining experience by defeating his minions and searching for loot.")
print (f"""your stats are as follows:
            your adventurers name is {nask}
            their class is {clask}
            they have {player_STR} STR
            they have {player_DEX} DEX
            they have {player_INT} INT
            they have {player_CHA} CHA
            they have {player_HP} health
            their armor class is {player_AC}
            they have {player_SS} spell slots""")
print ("inventory:")
for x in inventory:
    print (x)
print (f"{gold} GP")
t.sleep(0.3)
def village():
    print (r.choice(descriptions))
    global player_HP, max_HP, gold, healing_potions, inventory
    while True:
        
        print ("you have 4 choices. you can go to dungeon, shop, talk, or rest")
        villchoice = input("(select dungeon, shop, talk, or rest):  ")
        if villchoice == "shop":
            shop_list = {"healing potion" : 10, "chain mail" : 35, "greatsword" : 25}
            options = ["healing potion", "chain mail", "greatsword", "key"]
            print ("the shop has healing potions, sets of chainmail, and a greatsword")
            print ("""the shopkeeper, a gruff looking woman with her hand on a dagger, looks at you expenctantly.
               \"so, are you just here to look, or are you going to buy something\"
                   our healing potions are 10, our chainmail is 35, we have a greatsword for 25""")
            shopchoice = input("type healing potion, chain mail, or greatsword \n").strip().lower()
            if shopchoice not in options:
                print (f" i dont think we sell {shopchoice}")
                continue
            else:
                cost = shop_list.get(shopchoice)
                if gold < cost:
                    print ("sorry, dont think you got enough gold for that")
                    continue
                if shopchoice == "healing potion":
                    healing_potions += 1
                    gold -= shop_list.get(shopchoice)
                    print ("you purchace a healing potion")
                elif shopchoice == "chain mail":
                    print ("you purchase the chainmail. it has been automaticly equiped")
                    player_AC == 15 + player_DEX
                    gold -= shop_list.get(shopchoice)
                elif shopchoice == "greatsword":
                    inventory.append("greatsword")
                    gold -= shop_list.get(shopchoice)
                elif shopchoice == "key":
                    inventory.append("key")
                    gold -= shop_list.get(shopchoice)
        elif villchoice == "talk":
            print(f"you ask around about any strange matters and eventually a passerby speaks up :\"{r.choice(talking)}\" ")
        elif villchoice == "rest":
            print ("you find a nice inn to spend the night")
            player_HP = max_HP
        else:
            print ("you set off toward the keep in the distance")
            entry()
def r_monster():
    chance = 4
    guess = r.randint(1,4)
    if guess == chance:
        return True
    else:
        return False
def battle(boss):
    global player_HP, max_HP, gold, healing_potions, inventory, player_AC, player_CHA, player_AC, player_DEX, player_SS, primary_ability, player_STR
    enemy = r.choice(Enemies)
    enemy_HP = Monsters[enemy]["health"]
    enemy_AC = Monsters[enemy]["AC"]
    enemy_damage = Monsters[enemy]["damage"]
    is_undead = Monsters[enemy]["undead"]
    if boss:
        enemy = "Veyzrath"
        enemy_HP = Monsters[enemy]["health"]
        enemy_AC = Monsters[enemy]["AC"]
        enemy_damage = Monsters[enemy]["damage"]
        is_undead = Monsters[enemy]["undead"]
    print (f"you spot a {enemy} ahead!")
    ini = (r.randint(1,20) + player_DEX)
    if ini > (r.randint(1,20) + r.randint(-1,4)):

        Turn = 1
    else:
        Turn = 2
    while True:
        run = False
        if Turn == 1:
            print ("it is your turn!")
            print (f"""your stats are as follows:
            you have {player_HP} health
            you have {player_SS} spell slots""")
            print ("your inventory is as follows")
            for x in inventory:
                print (x)
            while True:
                print ("you have 3 options. you can attack, cast spell, or drink a healing potion(attack, spell, heal)")
                battle_choice = input().strip().lower()
                if battle_choice not in ["attack", "spell", "heal"]:
                    print ("that is not a valid command")
                    continue
                else:
                    break
            if battle_choice == "attack":
                while True:
                    print ("what weapon are you attacking with")
                    w_choice = input().lower().strip()
                    if w_choice not in inventory:
                        print ("that is not a valid weapon")
                        continue
                    break
                weapon_d = weapon_damage_die[w_choice]
                weapon_dd = weapon_damage_die_amounts[w_choice]
                attack_roll = (r.randint(1,20) + primary_ability)
                if attack_roll == (20 + primary_ability) or (is_undead and w_choice == "sword of light"):
                    print ("you crit!")
                    bonus = 2
                else:
                    bonus = 1
                if attack_roll >= enemy_AC or bonus == 2:
                    damage = r.randint(1, weapon_d)
                    for x in range(weapon_dd-1):
                        damage += r.randint(1, weapon_d)
                    damage *= bonus
                    damage += primary_ability
                    print (f"you hit! you deal {damage} damage to the enemy")
                    enemy_HP -= damage
            if battle_choice == "spell":
                if player_SS <= 0:
                    print("You don't have any spell slots left!")
                print("Choose a spell: Fireball(2), Cure Wounds(1), Magic Missile(1), or Thunderwave(0–1)")
                spell_choice = input("> ").lower()
                if spell_choice == "fireball" and player_SS >= 2:
                    player_SS -= 2
                    attack_damage = r.randint(8, 30)
                    print(f"You hurl a fireball! The {enemy} takes {attack_damage} damage!")
                    
                elif spell_choice == "cure wounds" and player_SS >= 1:
                    player_SS -= 1
                    heal = r.randint(2, 16)
                    player_HP += heal
                    if player_HP > max_HP:
                        player_HP = max_HP
                    print(f"You cast Cure Wounds and regain {heal} HP! ({player_HP}/{max_HP})")
                elif spell_choice == "magic missile" and player_SS >= 1:
                    player_SS -= 1
                    damage = r.randint(4, 24)
                    enemy_HP -= damage
                    print(f"Magic missiles strike the {enemy} for {damage} damage!")
                elif spell_choice == "thunderwave":
                    player_SS -= r.randint(0, 1)
                    damage = r.randint(2, 12)
                    enemy_HP -= damage
                    print(f"You cast Thunderwave! The {enemy} takes {damage} damage!")
                else:
                    print("You don't have enough spell slots or failed to cast the spell")
            if battle_choice == "heal":
                healing_potions -= 1
                health_regain = r.randint(4,16)
                player_HP += health_regain
                if player_HP > max_HP:
                    player_HP = max_HP
                print (f"you guzzle down a healing potion and regain {health_regain} health")
            Turn = 2
        if not run and enemy_HP < 0:
            print ("you have defeated the monster! you level up!")
            stat_in = input("choose STR, DEX, HP, Spell Slots, or AC\n").lower()
            if stat_in == "str":
                stat_in = r.randint(1,3)
                print (f"you have increased your strength by {stat_in}")
                if enemy == "death knight":
                    stat_in = r.randint (2, 6)
                player_STR += stat_in
            elif stat_in == "dex":
                stat_in = r.randint(1,3)
                if enemy == "death knight":
                    stat_in = r.randint (2, 6)
                print (f"you have increased your dexterity by {stat_in}")
                player_DEX += stat_in
            elif stat_in == "hp":
                stat_in = r.randint(1,10)
                if enemy == "death knight":
                    stat_in = r.randint (2, 6)
                print  (f"you have increased your health by {stat_in}")
                player_HP += stat_in
            elif stat_in == "ac":
                print ("you have increased your Armor Class by 1")
                player_AC += 1
            elif stat_in == "spell slots" or stat_in == "ss":
                print ("you have increased your spell slots by one")
                player_SS += 1
            max_HP = player_HP
            if player_SS < 0:
                player_SS = 0
            if player_STR >= player_DEX:
                primary_ability = player_STR
            else:
                primary_ability = player_DEX
                
            break   
        if Turn == 2:
            if enemy_HP in [1,2,3,4] and r.randint(1,4) == 4:
                print ("the monster runs away, clutching its wounds")
                run = True
                break
            print(f"The {enemy} attacks!")
            mon_attack = r.randint(1, 20)+ r.randint(1,5)
            if mon_attack >= player_AC:
                damage = r.randint(1, enemy_damage)
                player_HP -= damage
                print(f"The {enemy} hits you for {damage} damage!")
            else:
                print(f"The {enemy} misses!")
            Turn = 1
        
    if player_HP < 0:
        print ("you have been slain.")
        for x in range(10):
            print ("\n")
            SystemExit()
def entry():
    global first_chest_stat, healing_potions
    print ("""you walk from the crisp air and bright light of the outside into a dimly lit room covered by dust and spiderwebs. 
           There is a door to your left, and a door in front of you. 
           Behind you is a stairway leading to the surface.""")
    if r_monster() == True:
        battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("which direction? left, forward, or back:  ")
            if move_direction == "left":
                dining()
            elif move_direction == "forward":
                hall()
            elif move_direction == "back":
                village()
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            if examine_roll > 17 and first_chest_stat:
                print ("you find a chest hidden in a bundle of spiderwebs! inside is two healing potions")
                healing_potions += 2
                first_chest_stat = False
            else:
                print ("you dont find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes however")
def dining():
    global dining_longsword, healing_potions
    print (""" you step into a large room with a fancy wooden table. some old bread still sits on a tray at the center
           to your right is a door, to your left is a passage, and in front of you is a wooden door""")
    if r_monster() == True:
        battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("which direction?  right, or forward:  ")
            if move_direction == "right":
                entry()
            elif move_direction == "forward":
                empty()
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            if examine_roll > 12 and dining_longsword:
                print ("hanging on the wall is a longsword and whetstone as decoration. you take it down and sharpen the blade")
                healing_potions += 2
                dining_longsword = False
                inventory.append("longsword")
            else:
                print ("you dont find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes however")
def hall():
    print (""" you step into a grand hall. three doors lead away from the hall
           one door is forward
           one passage is to your left
           one door is behind you""")
    
    if r_monster() == True:
        battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("which direction? left, forward, or back")
            if move_direction == "left":
                training()
            elif move_direction == "back":
                entry()
            elif move_direction == "forward":
                guard()
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            print ("you dont find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes however")
def empty():
    global healing_potions
    print ("""you step into a dark room filled with spiderwebs. there is only one door behind you.""")
    if empty_ambush:
        battle(False)
        battle(False)
    else:
        if r_monster() == True:
            battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("the only way is back:  ")
            if move_direction == "back":
                dining()
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            if examine_roll > 8:
                print ("you find a single healing potion, problanly left by those monsters for an emergency")
            else:
                print ("you cant find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes however")
def training():
    global TaSS
    print ("you walk into a decripted training yard. there is one door to your right")
    if r_monster() == True:
        battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("the only way is right:  ")
            if move_direction == "right":
                hall()
            else:
                print ('that is not a valid direction')
                continue
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            if examine_roll > 8 and TaSS:
                print ("you find a shortsword in a closet")
                inventory.append("shortsword")
            else:
                print ("you do not find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes")
def guard():
    global healing_potions
    print ("you walk into a guard chamber. there is one door forward and one back")
    if r_monster() == True:
        battle(False)
    while True:
        room_option = input("move, examine, or yell?  ").strip().lower()
        if room_option == "move":
            move_direction = input("you can go forward, or back:  ")
            if move_direction == "back":
                hall()
            elif move_direction == "forward":
                throne()
            else:
                print ('that is not a valid direction')
                continue
        elif room_option == "examine":
            examine_roll = (r.randint(1,20) + player_INT)
            if examine_roll > 8:
                print ("you find a single healing potion")
                healing_potions += 1
            else:
                print ("you cant find anything")
        elif room_option == "yell":
            print ("you yell very loudly for some reason")
            if r_monster() == True:
                battle(False)
            else:
                print ("nothing comes")
def throne():
    print ("""you walk into a large room. a figure stands in the center. clothed in black robes" \
    " the figure raises a skeletal hand towards you." \
    " it seems you have reached your destination...""")
    battle(True)
    print ("you strike the final blow. veyzraths crumples to the ground before vanishing in a puff of mist")
    print ("you have defeated the mighty veyzrath and saved the village!")

village()