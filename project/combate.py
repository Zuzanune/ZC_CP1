import random
enemy_names = ["Goblin", "red sludge", "skeleton", "zombie", "kobald", "wrath", "Boss"]
boss_names = ["Death Lord", "Red Dragon", "Champion", "Demon Lord", "Bone Mass", "Goblin boss"]
while True:
    difficulty = 10
    user_HP = random.randint(20, 40)
    user_AC = 10
    healing_potions = 3
    user_STR = random.randint(8, 12)
    user_DEX = random.randint(8, 12)
    user_SS = random.randint(0, 1)
    print("Ho there adventurer! what might be your name?")
    user_name = input("> ")
    print("What class might you be?")
    uclass = input("Choose fighter, rogue, or wizard:  ").lower()
    if uclass == "fighter":
        user_crit_chance = [19, 20]
        user_damage = 20
        user_AC += 2
        user_HP += 15
        user_STR += 5
    elif uclass == "rogue":
        user_crit_chance = [15,16,17,18, 19, 20]
        user_damage = 15
        user_AC += 1
        user_HP += 5
        user_DEX += 5
        user_SS += 2
        user_AC += int((user_DEX - 10) / 2)
    else:
        user_crit_chance = [20]
        user_damage = 6
        user_AC -= 1
        user_DEX += 2
        user_SS += 7
        user_HP -= random.randint(2, 12)
    max_HP = user_HP
    max_SS = user_SS
    while True:
        mon_HP = random.randint(1, difficulty * 2)
        mon_AC = random.randint(8 + int(difficulty / 10), 10 + int(difficulty / 10))
        mon_STR = random.randint(8, 17)
        mon_DEX = random.randint(7, 15)
        enemy = random.choice(enemy_names)
        mon_DD = 6 + difficulty/10
        if enemy == "Boss":
            mon_HP += random.randint(10, 50)
            mon_AC += random.randint(0, 5)
            mon_STR += random.randint(0, 5)
            mon_DEX += random.randint(0, 5)
            mon_DD = 12 + difficulty/10
            enemy = random.choice(boss_names)
            print(f"A boss approaches — expect an epic fight! The {enemy} has entered the battlefield!")
        else:
            print(f"An enemy approaches — you spot a {enemy}!\n")
        def userTurn():
            global user_HP, user_SS, mon_HP, healing_potions
            print(f"\nYou have {user_HP} HP left.")
            if user_SS > 0:
                print(f"You also have {user_SS} spell slots left.")
            print("Your turn! Would you like to Attack, Spell, or Heal?")
            user_action = input("> ").lower()
            if user_action == "attack":
                print("You attack!!")
                user_attack = random.randint(1, 20)
                attack_damage = random.randint(1, user_damage) + (user_STR / 2)
                if user_attack in user_crit_chance:
                    print("You crit!")
                    attack_damage *= 2
                if user_attack == 1:
                    print("Darn, you injure yourself while attacking. Take 1 damage.")
                    user_HP -= 1
                elif user_attack > mon_AC:
                    print(f"You hit! You deal {int(attack_damage)} damage to the {enemy}.")
                    mon_HP -= int(attack_damage)
                else:
                    print("You missed!")
            elif user_action == "spell":
                if user_SS <= 0:
                    print("You don't have any spell slots left!")
                    return
                print("Choose a spell: Fireball(2), Cure Wounds(1), Magic Missile(1), or Thunderwave(0–1)")
                spell_choice = input("> ").lower()
                if spell_choice == "fireball" and user_SS >= 2:
                    user_SS -= 2
                    attack_damage = random.randint(8, 46)
                    print(f"You hurl a fireball! The {enemy} takes {attack_damage} damage!")
                    mon_HP -= attack_damage
                elif spell_choice == "cure wounds" and user_SS >= 1:
                    user_SS -= 1
                    heal = random.randint(2, 16)
                    user_HP += heal
                    if user_HP > max_HP:
                        user_HP = max_HP
                    print(f"You cast Cure Wounds and regain {heal} HP! ({user_HP}/{max_HP})")
                elif spell_choice == "magic missile" and user_SS >= 1:
                    user_SS -= 1
                    damage = random.randint(4, 24)
                    mon_HP -= damage
                    print(f"Magic missiles strike the {enemy} for {damage} damage!")
                elif spell_choice == "thunderwave":
                    user_SS -= random.randint(0, 1)
                    damage = random.randint(2, 12)
                    mon_HP -= damage
                    print(f"You cast Thunderwave! The {enemy} takes {damage} damage!")
                else:
                    print("You don't have enough spell slots or mistyped the spell.")
            elif user_action == "heal":
                if healing_potions <= 0:
                    print("You have no healing potions left!")
                    return
                healing_potions -= 1
                heal = random.randint(3, 18)
                user_HP += heal
                if user_HP > max_HP:
                    user_HP = max_HP
                print(f"You drink a potion and heal {heal} HP. You now have {user_HP}/{max_HP} HP.")
            else:
                print("Invalid action.")
        def monTurn():
            global user_HP, mon_HP
            if mon_HP <= 0:
                return
            print(f"\nThe {enemy} attacks!")
            mon_attack = random.randint(1, 20)+ mon_STR
            if mon_attack > user_AC:
                damage = random.randint(1, int(mon_DD))
                user_HP -= damage
                print(f"The {enemy} hits you for {damage} damage!")
            else:
                print(f"The {enemy} misses!")
        mon_ini = 10 + (mon_DEX / 10)
        player_ini = 10 + (user_DEX / 10)

        if player_ini > mon_ini:
            turn = "player"
        else:
            turn = "Monster"
        while user_HP > 0 and mon_HP > 0:
            if turn == "player":
                userTurn()
                turn = "Monster"
            else:
                monTurn()
                turn = "player"
            if user_HP <= 0 or mon_HP <= 0:
                break
        if user_HP <= 0:
            print("\nYou have fallen in battle... Game over.")
            break
        else:
            print(f"\nYou defeated the {enemy}! Victory!")
            difficulty += 10
            user_HP = max_HP
            user_SS = max_SS
            healing_potions = 3
            print(f"\nDifficulty has increased to {difficulty}!")
            cont = input("Continue to the next battle? (y/n): ").lower()
            if cont != "y":
                break
    again = input("Would you like to start a new adventure? (y/n): ").lower()
    if again != "y":
        break
