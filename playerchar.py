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
    pos_x = 0
    pos_y = 0
    pos_z = 0
    
    def position_check(self):
        print('Current coordinates: ({}:{}:{})'.format(self.pos_x,self.pos_y,self.pos_z))
    def position_update(self,x,y,z):
        self.pos_x = self.pos_x + x
        self.pos_y = self.pos_y + y
        self.pos_z = self.pos_z + z
        print('You are now at: ({}:{}:{})'.format(self.pos_x,self.pos_y,self.pos_z))
    def position_set(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z
    
        
    def inventory_check(self):
        if not self.inventory:
            print('inventory empty')
        else:
            print('your inventory contains:')
            for i in self.inventory:
                print('- ' + i.name)

class Monster:
    def __init__(self, health, dmg, pos_x, pos_y, pos_z):
        self.health = health
        self.dmg = dmg
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z

    

