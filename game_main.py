import playerchar
import items
import monsterchar
import game_events

playerone = playerchar.Player()

playerone.inventory_check()

w_stt = items.Weapon('Sword of a Thousand Truths', 29, 5)
shoes1 = items.Shoes('Silk Slippers',45,'silk',3.5,5)
playerone.inventory = [w_stt,shoes1]

playerone.inventory_check()
playerone.position_check()

playerone.position_update(4,2,1)
playerone.position_check()

playerone.position_set(1,1,1)

playerone.position_update(1,1,1)
playerone.position_check()

q1 = playerchar.Quest('steal gold',3,5,0,'gold pieces')
q1.endQuest()

playerone.position_update(0,0,1)

monster1 = monsterchar.Monster(2,2,3,'booby brown',22,2000,10)

game_events.checker(monster1,playerone)

while True:
    n = input("what is your command?")
    if (n.strip() == "exit"):
        print('you have died.')
        break
    elif n.strip() == "go" or "move" or "walk":
        g = input("please input coordinates x,y,z")
        break


