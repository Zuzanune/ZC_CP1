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
user_SS = r.randint(0,1)
player_crit_roll = [20]
inventory = []
healing_potions = 2
print (" A gruff man carrying a club walks up to you. \"I hear you are the new aventurer coming to the town to cull the lich. what is your name?\"")
nask = input()
print (f"""\"ah. ok {nask}. I am Lorin, the head guard of this town\"
        he rolls his club in his hand \"
        let me give you a quick sumary of our situation. the lich Veyzrath has taken over a small keep and is terrorising the civilians.
        thank you for coming to our humble town. i hope you fare better then the many before you.""")
print (f"what class of adventuer are you {nask}?")
clask = input("choose wizard, fighter, rouge, or barbarian")
if clask == "wizard":
    player_STR -= 2
    player_DEX += 1
    player_INT += 6
    player_CHA += 1
    player_HP += player_STR
elif clask == "fighter":
    


