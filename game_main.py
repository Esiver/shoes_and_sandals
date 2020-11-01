import playerchar
import items
import monsterchar
import game_events
import world



#declare characters
playerone = playerchar.Player(100,[], "Forest",1)
monster1 = monsterchar.Monster('booby brown',22,2000,10)

w_stt = items.Weapon('Sword of a Thousand Truths', 29, 5)
shoes1 = items.Shoes('Silk Slippers',45,'silk',3.5,5)
playerone.inventory = [w_stt,shoes1]

print(world.wMap)

monsters = monsterchar.monsterMaker()


world.roomFill(world.wMap['Forest'].inv, monsters)
print("forest   ",world.wMap['Forest'].inv)


#playerone.inventory_check()

#q1 = world.Quest('steal gold',3,5,0,'gold pieces')
#q1.endQuest()

#
game = True
while game == True: #start game
    
    n = input("What will you do? \n >>> ")                          #enquire command from player
    if n.strip() == "travel":                                       # in case 'travel' command
        # tell where can travel - loop trough dir
        t = input("In what direction will you travel? \n >>> ")     # where will player then travel?
        if t.strip() in {'N', 'E', 'S', 'W'}:                       # only take compass directions
            print(n,' towards ',t+'est')                            # confirming message
            playerone.travel(t)                                     # start travel function with direction arg        
        else:                                                       # handle error
            print("invalid direction")                              # + message

    if n.strip() == "look":                                         # 
        print("you look around.")
        playerone.look()
        game = True
    if n.strip() == "venture":
        game_events.venture(playerone)
    if n.strip() == "quit":
        print('you have died.')
        game = False
    #else:
    #    print('......invalid command')