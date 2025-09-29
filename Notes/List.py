# ZC 1st List Notes
import random
dice_sets = ["Green", "Forest green", "Green w/ red","junk", "Blue","black w/ gold","blue w/ gold", "Turquise","mooooore junk :)", "Blue w/ purple", "Red", "Red w/ blue", "gold", "black", "white", "white w/ black", "junky text here: ;)"]
print (f" this is the color of mty favorite dice set: {dice_sets[6]}")
dice_sets[1] = "Deep green"
dice_sets.pop()
dice_sets.pop(3)
dice_sets.pop(7)
print (dice_sets)
print (f"i own many dice, i usually have {len(dice_sets)} dice_sets at home.")
print ('but that is not all the dice i own')
dice_sets.extend(["yellow", "brown", "blue w/ yellow", "drab green", "red w/ gold"])
print (dice_sets)
print (f"a random dice set in my bag is {random.choice(dice_sets)}")
