import world
import game_events
class Player:
    def __init__(self,health,dmg,bag,room, depth,speed):
        self.health = health
        self.bag = bag
        self.room = world.wMap[room]
        self.depth = depth
        self.dmg = dmg
        self.speed = speed

    def travel(self, direction): #perhaps add event_handler to allow for random events?
        if direction in self.room.links:
            new_room_name = self.room.links[direction]
            print('travelling from {} to {}'.format(self.room.name, new_room_name))
            self.room = world.wMap[new_room_name]
            print("you are now in ",self.room.name)
            self.look()
            return

    def equip(self, item):                                                                  # Equip function
        import items        
        print("I want to equip", item)      
        for i, value in enumerate(self.bag):                                                # Create tuple of bag to browse through
            print("Looking at...",self.bag[i].__class__.__name__,value.name)                # remind player what items in bag

            if value.name.lower() == item:                                                  # IF player input ("item") is same as current iterated object in tuple
                print("Found",value.name)                                                   # ... we have a great success!
                if self.bag[i].__class__.__name__ == 'Shoes':                               # ... and if that object class name is "Shoes"
                    print("You kneel down to strap on", value.name)                         # we wear shoe.
                    self.speed = value.speed                                                # and change player stat speed
                    print(self.speed)       
                elif self.bag[i].__class__.__name__ == 'Weapon':                            # else, if weapon
                    print("You wield {}. It lies heavy in your hand".format(value.name))    # We grasp for weapon.
                    self.dmg = value.dmg                                                    # and change player stat dmg
    
    def statPrint(self):                                                                    # Check player stats
        print("You examine yourself.")
        print("attack:",self.dmg)
        print("health:",self.health)
    
    def look (self):
        print(self.room.desc)
    
    def inventory_check(self):
        if not self.bag:
            print('inventory empty')
        else:
            print('your inventory contains:')
            for i in self.bag:
                print('- ' + i.name)
            b = input("what will you do with that?")
            if "equip" in b:
                e = input("what will you equip? ")
                print("----")
                self.equip(e)
            else:
                print("Cant find that.")
                return




