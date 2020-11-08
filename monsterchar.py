class Monster:
    def __init__(self,name,dmg,health,speed,inv):
        self.name = name
        self.dmg = dmg
        self.health = health
        self.speed = speed
        self.hostile = True
        
        #self.inv = []
        self.basehealth = health
        self.alive = True
    
    def mencounter(self):
        print('you have encountered {}, prepare for battle!'.format(self.name))
        print('{} has {} hp and does {} dmg'.format(self.name, self.health, self.dmg))

def monsterMaker():
    print("generating foes")
    name_list = ["arrra","eerfff","uueeer","koorrr"] #kunne være sejt bare at importere en .txt med dette.
    monster_list = []
    for i in range(3):
        monster_list.append(Monster(name_list[i],i*5,i*24,i*3,[]))
        print(monster_list[i].name)
        print(monster_list[i].dmg)
        print(monster_list[i].health)
    return monster_list



