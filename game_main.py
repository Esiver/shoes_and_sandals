import playerchar
import items



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


