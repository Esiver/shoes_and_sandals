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



