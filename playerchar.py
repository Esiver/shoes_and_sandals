import numpy as np

class Quest:
    def startQuest(self,name,reward,goal,what):
        print('You started a quest: {}'.format(name))
        print('You must collect {} {}'.format(goal,what))
        print('Upon completion you will be rewarded {} gold pieces'.format(self.reward))
    def endQuest(self):
        print('You have successfully collected {} {} and are rewarded {} gold coins. \n Completed quest {}'.format(self.goal,self.what,self.reward,self.name))

    def __init__(self, name,reward,goal,progress,what):
        self.name = name
        self.reward = reward
        self.goal = goal
        self.progress = progress
        self.what = what
        self.startQuest(name,reward,goal,what)

class Player:
    health = 10
    inventory = []
    position_x = 0
    position_y = 0
    position_z = 0
    
    def position_check(self):
        print('Current coordinates: ({}:{}:{})'.format(self.position_x,self.position_y,self.position_z))
    def position_update(self,x,y,z):
        self.position_x = self.position_x + x
        self.position_y = self.position_y + y
        self.position_z = self.position_z + z
    def position_set(self, x, y, z):
        self.position_x = x
        self.position_y = y
        self.position_z = z
    
        


    def inventory_check(self):
        if not self.inventory:
            print('inventory empty')
        else:
            print('your inventory contains:')
            for i in self.inventory:
                print('- ' + i.name)

class Monster:
    def __init__(self, health, dmg, position_x, position_y, position_z):
        self.health = health
        self.dmg = dmg
        self.position_x = position_x
        self.position_y = position_y
        self.position_z = position_z

    

