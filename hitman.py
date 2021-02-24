import random
maps = ['World of Tomorrow', 'Club 27', 'Freedom Fighters', 'Situs Inversus', 'Nightcall', 'The Finish Line', 'A Silver Tongue', 'Another Life' ,'A Better Pill', 'The Ark Society', 'Golden Handshake', 'The Last Resort', 'On Top of The World', 'Death in the Family', 'Apex Predator', 'End of an Era', 'The Farewell']
a = 1
while a == 1:
    map = random.choice(maps)
    if map == 'World of Tomorrow':
        targets = ['Silvio Caruso' ,'Francesca De Santis']
        target = random.choice(targets)
        if target == 'Silvio Caruso':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol', 'Explosive Golf Ball']
            method = random.choice(methods)
        elif target == 'Francesca De Santis':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
            method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminate by: ', method)
        input()
    elif map == 'Club 27':
        targets = ['Jordan Cross', 'Ken Morgan']
        target = random.choice(targets)
        if target == 'Joradn Cross':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol', "From Jordan Cross's Chair"]
        elif target == 'Ken Morgan':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol', "Falling Chandelier", "Assassinate with the Ram", "Exploding Watch", "Drowning in the Water Basin"]
            method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminiate by: ', method)
        input()
    elif map == "Freedom Fighters":
        targets = ["Sean Rose", "Erza Berg", 'Penelope Graves', 'Maya Parvati']
        target = random.choice(targets)
        if target == 'Sean Rose':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        elif target == 'Erza Berg':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        elif target == 'Penelope Graves':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        elif target == 'Maya Parvati':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminate by: ', method)
        input()
    elif map == 'Situs Inversus':
        targets = ['Erich Soders', 'Yuki Yamazaki']
        target = random.choice(targets)
        if target == 'Erich Soders':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        elif target == 'Yuki Yamazaki':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminate by: ', method)
        input()
    elif map == 'Nightcall':
        target = 'Alma Reynard'
        methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
        method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminate by: ', method)
        input()
