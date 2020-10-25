
import world
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
    def __init__(self,health,bag,room, pos_x, pos_y):
        self.health = health
        self.bag = bag
        self.room = world.wMap[room]
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, direction):
        if direction not in world.wMap:
            print("you can not move that way")
            return
        self.room = world.wMap[direction]
        print("you are now entering {}".format(self.room))

    def position_update(self,x,y):
        self.pos_x = self.pos_x + x
        self.pos_y = self.pos_y + y
        print('You are now at: ({}:{})'.format(self.pos_x,self.pos_y))
        
    def position_set(self, x, y):
        self.pos_x = x
        self.pos_y = y
        
            
    def inventory_check(self):
        if not self.bag:
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

    

