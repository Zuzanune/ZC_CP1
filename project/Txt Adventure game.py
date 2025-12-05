#ZC 1st Finals text adventure game
import random as r
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
Monsters = { "Goblin" : {"health" : 11, "AC" : 10, "Damage" : 6}, "skeleton" : {"health" : 15, "AC" : 14, "damage" : 6, "undead" : True},"zombie" : {"health" : 13, "AC" : 11, "damage" : 6, "undead" : True}, "ochre jelly" : {"health" : 25, "AC" : 9, "Damage" : 10},  "undead knight": {"health" : 50, "AC" : 18, "damage" : 12, "undead" : True}, "Veyzrath": {"health" : 75, "AC" : 15, "damage": 8, "exdamage" : 20, "undead" : True} }
Enemies = ["goblin","goblin", "skeleton", "skeleton", "ochre jelly","zombie","zombie"]
weapon_damage_die = {"club" : 4, "dagger" : 4, "shortsword" : 6, "longsword" : 8, "greatsword" : 6, "greataxe" : 12, "staff" : 4, "fists" : 1, "sword of light" : 6}
weapon_damage_die_amounts = {"club" : 1, "dagger" : 1, "shortsword" : 1, "longsword" : 1, "greatsword" : 2, "greataxe" : 1, "staff" : 1, "fists" : 1, "sword of light" : 3}
player_STR = r.randint(-1,2)
player_DEX = r.randint(-1,2)
player_INT = r.randint(-1,2)
player_CHA = r.randint(-1,2)
player_AC = 10
player_HP = 9
gold = r.randint(30,50)
user_SS = r.randint(0,1)
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
if player_SS < 0:
    player_SS = 0
if player_STR >= player_DEX:
    primary_ability = player_STR
else:
    primary_ability = player_DEX
print (f"\"nice to meet you, {nask}. I hope you will free our small town from the horrible Veyzrath\"")
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
def village():
    print (r.choice(descriptions))
    while True:
        
        print ("you have 4 choices. you can go to dungeon, shop, talk, or rest")
        villchoice = input("(select dungeon, shop, talk, or rest):  ")
        if villchoice == "shop":
            shop_list = {"healing potion" : 10, "chain mail" : 35, "greatsword" : 25, "key" : 20}
            options = ["healing potion", "chain mail", "greatsword", "key"]
            print ("the shop has healing potions, sets of chainmail, a greatsword, and a strange key")
            print ("""the shopkeeper, a gruff looking woman with her hand on a dagger, looks at you expenctantly.
               \"so, are you just here to look, or are you going to buy something\"""")
            shopchoice = input("type healing potion, chain mail, greatsword, or key").strip().lower()
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
                elif shopchoice == "chainmail":
                    player_AC == 15 + player_DEX







    


