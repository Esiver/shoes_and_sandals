import numpy as np

class Room:
    def __init__(self,name,desc,links,dice,depth,inv):
        self.name = name
        self.desc = desc
        self.links = links
        self.dice = dice #later implement randomizing effect
        self.depth = depth
        self.inv = []
    def describe(self):
        print(self.desc)
    def up(self):
        self.depth +1
        print("you venture further into the {}, current level: {}".format(self.name,self.depth))
    
#Generate room inv
def roomFill(room,fill):
    print("generating rooms")
    for x in range(len(fill)):
        room.append(fill[x])
        print(fill[x])
    # 1. append hvadsomhelst OK
    # 2. append monster OK
    # 3. append genstand OK
    # 4. generer monstre OK
    # 5. loop append alle monstre
    
    
    


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

world = {}

wMap = {}
wMap['Forest'] = Room("forest of lies", "You are in a forest. You can tell it lies.", {'N' : "Cave"},2,0,[0,0,"Jens"])
wMap["Cave"] = Room("Cave of Truths", "You are in a cave. You can tell it tells truths", {'S':"Forest"},4,0,[0,0,"Jens"])

