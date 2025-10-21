#ZC, 1st, Functions Notes
x = int(input("enter a number:  "))
y = int(input("enter a number:  "))
namefull = input("what is your full name:  ")
def add(x,y):
   print (f"{x} + {y}  = {x+y}")
   return x + y 
def initials(name):
   names = name.split(" ")
   initials = ""
   for name in names:
      initials += name[0]
   return initials
#print (initials(namefull))
player_health = 100
monster_health = 100
def damage(amount, turn):
   if turn == "player":
      return monster_health-amount, player_health  
   else:
      return monster_health, player_health - amount
   
monster_health, player_health = damage(10, "player")
print (f"Monster Health: {monster_health}")
print (f"Player Health: {player_health}")
damage(10,"player")