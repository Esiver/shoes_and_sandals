

def get_key(val):
    import world
    for key, value in world.wMap.items(): 
         if val == value: 
             return key 
    return "key doesn't exist"

def venture(you):
        
        you.depth = you.depth +1
        print("you venture deeper into the {}".format(you.room.name))
        print("level: {}.".format(you.depth))
        print("VENTURE FUCNTION", you)
        try:
            import world
            check(you ,world.wMap[get_key(you.room)].inv[you.depth])
        except IndexError:
            print("you see nothing here.")
            pass
        r = input('what will you do in the {} (level {})?\n >>>'.format(you.room.name,you.depth))
        if r.strip() == "venture":
            venture(you)    
        if r.strip() == "exit":
            print("you retreat from level {} the {}.".format(you.depth,you.room.name))
            you.depth = 0
        if r.strip() == "look":
            you.look()

def loot():
    print("you loot the area.")

def check(you,tile):
    print("CHECK FUNCTION", tile)
    if tile != 0:
        print("You encounter {}.".format(tile.name))
        if tile.hostile == True:
            print("They're hostile.")
            encounter(you,tile)
        else: 
            print("They're friendly.")
        
    else:
        print("There is no one here.")

def encounter(you,tile):
    turnCount = 0
    if tile.hostile == True:
        battle(you,tile,turnCount)

def battle(you,tile,turnCount):
    while (tile.health > 0):
        turnCount += 1
        print("turn:", turnCount)
        #load(tile, )
        print("---------")
        tile.health = tile.health - you.dmg
        print(tile.health)
        print(you.health)
        d = input("how will you advance the battle? (run OR attack) \n")
        if d == "run":
            if you.speed > tile.speed:
                print("you successfully run away from", tile.name)
                tile.health = tile.basehealth
                return
            else:
                print("you are not fast enough to run away")
        
    if (tile.health <= 0):
        print("{} has died.".format(tile.name))
        tile.alive = False
        return
    #battle(you,tile,)