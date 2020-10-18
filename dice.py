from numpy import random

def encounter(monster):
    print('you have encountered {}'.format(monster))

def roll():
    dice_roll = random.randint(20)
    return dice_roll
dr = roll()
print(dr)

def check(player_posis, monster_posis):
    if player_posis == monster_posis:
        print('you have encountered oponent')