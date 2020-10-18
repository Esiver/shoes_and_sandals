class Weapon:
    def __init__(self, name, dmg, cost):
        self.name = name
        self.dmg = dmg
        self.cost = cost

    def introduce_self(self):
        print('You found weapon: ' + self.name)
        print('{} has an attack value of {}'.format(self.name,self.dmg))
        print('You estimate {} to be worth {} gold coins.'.format(self.name,self.cost))
    
class Shoes:
    def __init__(self,name,size,material,speed,cost):
        self.name = name
        self.size = size
        self.material = material
        self.speed = speed
    
    def introduce_self(self):
        print('You found shoes: ' + self.name)
        print('{} are sized {}'.format(self.name,self.size))
        print('You estimate {} to be worth {} gold coins.'.format(self.name,self.cost))

    def describe_self(self):
        print('')



playerone = Player()

playerone.inventory_check()

w_stt = Weapon('Sword of a Thousand Truths', 29, 5)
shoes1 = Shoes('Silk Slippers',45,'silk',3.5,5)
playerone.inventory = [w_stt,shoes1]

playerone.inventory_check()
playerone.position_check()

playerone.position_update(4,2)
playerone.position_check()

q1 = Quest('steal gold',3,5,0,'gold pieces')
q1.endQuest()
