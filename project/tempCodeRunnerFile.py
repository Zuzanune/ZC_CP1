def battle():
    enemy = r.choice(Enemies)
    enemy_HP = Enemies[enemy]["health"]
    enemy_max_hp = enemy_HP
    enemy_AC = Enemies[enemy]["AC"]
    enemy_damage = Enemies[enemy]["damage"]
    is_undead = Enemies[enemy]["undead"]
    print (f"you spot a {enemy} ahead!")
    ini = (r.randint(1,20) + player_DEX)
    if ini > (r.randint(1,20) + r.randint(-1,4)):