import playerchar
import items
import monsterchar
import game_events
import world

#declare characters
playerone = playerchar.Player(100,1,[], "Forest",1,11)
monster1 = monsterchar.Monster('booby brown',22,2000,10,[])

w_stt = items.Weapon('Sword of a Thousand Truths', 29, 5)
shoes1 = items.Shoes('Silk Slippers',45,'silk',3.5,5)
playerone.bag = [w_stt,shoes1]

monsters = monsterchar.monsterMaker(2,1,1)

#for site in world.wMap:
#    for lvl in site:
#        world.roomFill(world.wMap[lvl].inv, monsters)
world.roomFill(world.wMap['Forest'].inv, monsters)
print(world.wMap['Forest'].inv)

#game = True
#while game == True: #start game
#    playerone.look()
#    n = input("What will you do? \n >>> ")                          #enquire command from player
#    if n.strip() == "travel":                                       # in case 'travel' command
#        # tell where can travel - loop trough dir
#        t = input("In what direction will you travel? \n >>> ")     # where will player then travel?
#        if t.strip() in {'N', 'E', 'S', 'W'}:                       # only take compass directions
#            print(n,' towards ',t+'est')                            # confirming message
#            playerone.travel(t)                                     # start travel function with direction arg        
#        else:                                                       # handle error
#            print("invalid direction")                              # + message
#
#    if n.strip() == "look":                                         # orientation
#        print("you look around.")
#        playerone.look()
#    if n.strip() == "venture":                                      # travel z-level, deeper into each room.
#        game_events.venture(playerone)
#    if n.strip() == "bag":                                          # inventory
#        print("you check your bags...")
#        playerone.inventory_check()
#    if n.strip() == "stats":                                        # player stats
#        playerone.statPrint()
#    if n.strip() == "quit":                                         # exit game
#        print('you have died.')
#        game = False

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GMessage_351=tk.Message(root)
        GMessage_351["bg"] = "#ff0c0c"
        ft = tkFont.Font(family='Times',size=10)
        GMessage_351["font"] = ft
        GMessage_351["fg"] = "#333333"
        GMessage_351["justify"] = "center"
        GMessage_351["text"] = "Message"
        GMessage_351.place(x=50,y=330,width=171,height=100)

        Button_South=tk.Button(root)
        Button_South["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_South["font"] = ft
        Button_South["fg"] = "#000000"
        Button_South["justify"] = "center"
        Button_South["text"] = "South"
        Button_South.place(x=430,y=400,width=70,height=25)
        Button_South["command"] = self.Button_South_command

        Button_North=tk.Button(root)
        Button_North["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_North["font"] = ft
        Button_North["fg"] = "#000000"
        Button_North["justify"] = "center"
        Button_North["text"] = "North"
        Button_North.place(x=430,y=340,width=70,height=25)
        Button_North["command"] = self.Button_North_command

        Button_West=tk.Button(root)
        Button_West["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_West["font"] = ft
        Button_West["fg"] = "#000000"
        Button_West["justify"] = "center"
        Button_West["text"] = "West"
        Button_West.place(x=360,y=370,width=70,height=25)
        Button_West["command"] = self.Button_West_command

        Button_East=tk.Button(root)
        Button_East["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_East["font"] = ft
        Button_East["fg"] = "#000000"
        Button_East["justify"] = "center"
        Button_East["text"] = "East"
        Button_East.place(x=500,y=370,width=70,height=25)
        Button_East["command"] = self.Button_East_command

        Button_Venture=tk.Button(root)
        Button_Venture["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        Button_Venture["font"] = ft
        Button_Venture["fg"] = "#000000"
        Button_Venture["justify"] = "center"
        Button_Venture["text"] = "Venture Deeper"
        Button_Venture.place(x=260,y=370,width=70,height=25)
        Button_Venture["command"] = self.Button_Venture_command

        Button_Inv=tk.Button(root)
        Button_Inv["bg"] = "#efefef"
        Button_Inv["font"] = ft
        Button_Inv["fg"] = "#000000"
        Button_Inv["justify"] = "center"
        Button_Inv["text"] = "Inventory"
        Button_Inv.place(x=260,y=420,width=70,height=25)
        ft = tkFont.Font(family='Times',size=10)
        Button_Inv["command"] = self.Button_Inv_command
        
        Button_Exit=tk.Button(root)
        Button_Exit["bg"] = "Red"
        Button_Exit["font"] = ft
        Button_Exit["fg"] = "#000000"
        Button_Exit["justify"] = "center"
        Button_Exit["text"] = "Exit"
        Button_Exit.place(x=50,y=50,width=50,height=50)
        ft = tkFont.Font(family='Times',size=10)
        Button_Exit["command"] = self.Button_Exit_command

    def Button_South_command(self):
        print("command")
        playerone.travel('S')

    def Button_North_command(self):
        print("command")
        playerone.travel('N')

    def Button_West_command(self):
        print("command")
        playerone.travel('W')

    def Button_East_command(self):
        print("command")
        playerone.travel('E')

    def Button_Venture_command(self):
        print("venture")
        game_events.venture(playerone)
    
    def Button_Inv_command(self):
        print("inventory")
        self.Window_Inv()
        playerone.inventory_check()

    def Button_Exit_command(self):
        print("goodbye, traveller")
        root.destroy()

    def Window_Inv(self):
        invWindow = tk.Tk()
        invWindow.title("Inventory")
        invWindow.geometry("200x400") 
        label = Label(invWindow, text ="This is a new window").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
