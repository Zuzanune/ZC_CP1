#ZC 1st Finals text adventure game
#tell user backround information to read about story(generic fantasy story,)
#Psudocode:
#Import random
#weapon damage die = {"club" : 4, "dagger" : 4, "shortsword" : 6, "longsword" : 8, "greatsword" 6, "greataxe" : 12, "staff" 4, "fists" 1, "sword of light" 6}
#weapon damage die amounts = {"club" : 1, "dagger" : 1, "shortsword" : 1, "longsword" : 1, "greatsword" 2, "greataxe" : 1, "staff" 1, "fists" 1, "sword of light" 3}
#Player STR = random.randint(-1,2)
#Player DEX = random.randint(-1,2)
#Player INT = random.randint(-1,2)
#Player CHA = random.randint(-1,2)
#Player AC = 10
#player crit roll = [20]
#Inventory = []
#Ask player which class to play
#If class == “wizard”:
#	Player STR -= 2
#	Player DEX += 1
#	Player INT += 4
#	Player CHA += 1
#   inventory.append("staff")
#Elif class == “fighter”:
#   Player STR += 4
#   player DEX += 1
#   Player CHA += 2
#   player AC += 2
#   player crit roll = [18,19,20]
#   inventory.append("shield")
#   inventory.append("shortsword")
#elif class == "rouge":
#   player STR -= 1
#   Player DEX += 6
#   player INT += 1
#   player CHA += 3
#   inventory.append("dagger")
#   player crit roll = [16,17,18,19,20]
#elif class == "barbarian":
#   player STR += 6
#   Player DEX -= 1
#   player INT -= 3
#   player CHA += 3
#   inventory.append("greataxe")
#   player crit roll = [19,20]
#Player AC += DEX

