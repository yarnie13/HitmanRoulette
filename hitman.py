import random
maps = ['World of Tomorrow', 'Club 27', 'Freedom Fighters', 'Situs Inversus', 'Hokkaido', 'Nightcall', 'The Finish Line', 'A Silver Tongue', 'Another Life' ,'A Better Pill', 'The Ark Society', 'Golden Handshake', 'The Last Resort']
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
        if target == 'Joradn Cross':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol', "From Jordan Cross's Chair"]
            method = random.choice(methods)
        elif target == 'Ken Morgan':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol', "Falling Chandelier", "Assassinate with the Ram", "Exploding Watch", "Drowning in the Water Basin"]
            method = random.choice(methods)
        print('Location: ', map)
        print('Target: ', target)
        print('Eliminiate by: ', method)
    elif map == "Freedom Fighters":
        targets = ["Sean Rose", "Erza Berg", 'Penelope Graves', 'Maya Parvati']
        if target == 'Sean Rose':
            methods = ["Silent Assassin", "Silent Assassin Suit Only", "Suit Only", 'Sniper Assassin', 'Sniper Assassin Suit Only', 'Drowning', 'Accident', 'Striaght Shot (Headshot)', 'Poison', 'Piano Man', 'SMG', 'AR', 'Shotgun', 'Pistol']
