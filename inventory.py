import time
import sys
from item import weapon
 
 
command = '0'
puppetitem = None
 
# Mitsunari-san's inventory
bag = []
 
def printinv():
    for i in range(len(bag)):
        obj = bag[i]
        print(i+1," ",obj.obj.name)
    print("Select a number on screen to do stuff, or input and enter any other key to exit.")
 
def dothis(hero, a, level, pos, items):
    try:
       a = int(a)
    except ValueError:
       return
    if a <= len(bag):
         select = a - 1
         interact(hero, select, level, pos, items)
 
def equip(hero, item):
    hero.equip = item
    print("Equipped the {}.".format(item.name))
    time.sleep(2)

def heal(hero, item):
    hero.heal(item.effect)

def drop(hero, i, level, pos, items):
    index = [-1,0,1]
    for a in range(3):
        for b in range(3):
            if level[pos.x+index[a]][pos.y+index[b]] == '.' and a != 1 and b != 1:
                level[pos.x+index[a]][pos.y+index[b]] = i
                level[pos.x+index[a]][pos.y+index[b]] = '?'
                items.append(i)
                bag.remove(i)
                return
    print("No dropping locations available.")
 
def interact(hero, c, level, pos, items):
        a = '3'
        obj = bag[c]
        while a == '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do with {}? Input number and enter.".format(obj.obj.name))
            print("1.Equip\n 2.Use\n 3.Info\n 4.Drop")
            a = input()
            if a == '1':
                if isinstance(obj.obj, weapon) == False:
                    print("You can't equip that!")
                    time.sleep(2)
                else:
                    equip(hero, obj.obj)
                return
            elif a == '2':
                if obj.obj.type == "H":
                    heal(hero, obj.obj)
            elif a == '3':
                print(obj.obj.desc)
                time.sleep(2)
            elif a == '4':
                drop(obj, level, pos, items)

