import playerchar
import items
import monsterchar
import game_events
import world




playerone = playerchar.Player(100,[], "Forest",1,1)

playerone.inventory_check()

w_stt = items.Weapon('Sword of a Thousand Truths', 29, 5)
shoes1 = items.Shoes('Silk Slippers',45,'silk',3.5,5)
playerone.inventory = [w_stt,shoes1]

q1 = world.Quest('steal gold',3,5,0,'gold pieces')
q1.endQuest()

#playerone.position_update(0,0,1)

monster1 = monsterchar.Monster(2,2,3,'booby brown',22,2000,10)

game_events.checker(monster1,playerone)



while True:
    n = input("what is your command? ")
    if n.strip() in {'N', 'E', 'S', 'W'}:
        print(n)
        playerone.travel(n)
    elif n.strip() == "exit":
        print('you have died.')
        break
    else:
        print('invalid command')
    
    

    


