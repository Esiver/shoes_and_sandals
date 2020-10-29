import world
import game_events
class Player:
    def __init__(self,health,bag,room, depth):
        
        self.health = health
        self.bag = bag
        self.room = world.wMap[room]
        self.depth = depth

    def travel(self, direction): #perhaps add event_handler to allow for random events?
        if direction in self.room.links:
            new_room_name = self.room.links[direction]
            print('travelling from {} to {}'.format(self.room.name, new_room_name))
            self.room = world.wMap[new_room_name]
            print("you are now in ",self.room.name)
            return

    def venture(self):
        self.depth = self.depth +1
        print("you venture deeper into the {}".format(self.room.name))
        print("level: {}.".format(self.depth))
        
        game_events.check(self.depth,world.wMap[game_events.get_key(self.room)].dice)
        game_events.check(self.)
        r = input('what will you do in the {}?\n >>>'.format(self.room.name))
        if r.strip() == "venture":
            self.venture()    
        if r.strip() == "exit":
            print("you retreat from level {} the {}.".format(self.depth,self.room.name))
            self.depth = 0
        if r.strip() == "look":
            self.look()
    def look (self):
        print(self.room.desc)
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

    

