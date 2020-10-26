
import world


class Player:
    def __init__(self,health,bag,room, pos_x, pos_y):
        self.health = health
        self.bag = bag
        self.room = world.wMap[room]
        self.pos_x = pos_x
        self.pos_y = pos_y

    def travel(self, direction): #perhaps add event_handler to allow for random events?
        if direction in self.room.links:
            new_room_name = self.room.links[direction]
            print('moving to', new_room_name)
            self.room = world.wMap[new_room_name]
        elif direction not in self.room.links:
            print("You can not go in that direction")

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

    

