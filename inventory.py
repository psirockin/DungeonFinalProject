import time
import sys
import math
from item import weapon
 
# Mitsunari-san's inventory
bag = []
 
def printinv():
    for i in range(len(bag)):
        obj = bag[i]
        sys.stdout.write("{}: {} {}\n".format(i+1, obj.obj.name, obj.dur))
    print("Select a number on screen to do stuff, or input and enter any other key to exit.")
 
def dothis(hero, a, level, pos, itemlocs, moving):
    try:
       a = int(a)
    except ValueError:
       return
    if a <= len(bag):
         select = a - 1
         interact(hero, select, level, pos, itemlocs, moving)
 
def equip(hero, item):
    if hero.equip != None and hero.equip == item:
        hero.equip = None
        print("Unequipped the {}.".format(item.obj.name))
    elif hero.equip == None and item.obj.subclass in hero.type.weapons:
        hero.equip = item
        print("Equipped the {}.".format(item.obj.name))
    else:
        print("You can't equip this!")
    time.sleep(1)

def drop(hero, i, level, pos, itemlocs):
    if hero.equip != None and i.obj == hero.equip.obj:
        equip(hero, i)
    index = [-1,0,1]
    for a in range(3):
        for b in range(3):
            if level[pos.x+index[a]][pos.y+index[b]] == '.' and a != 1 and b != 1:
                level[pos.x+index[a]][pos.y+index[b]] = i
                level[pos.x+index[a]][pos.y+index[b]] = '?'                
                i.level = level
                i.x = pos.x + index[a]
                i.y = pos.y + index[b]
#                print("This is at {}, {}.".format(i.x,i.y))
                itemlocs.append(i)
                bag.remove(i)
                return
    print("No dropping locations available.")

def sell(hero, i):
    if hero.equip != None and i.obj == hero.equip.obj:
        equip(hero, i)
    for a in range(len(bag) - 1, -1, -1):
        if i.obj == bag[a].obj:
            hero.money += int(i.obj.cost * .25)
            bag.pop(a)
            return

def update():
    for a in range(len(bag) - 1, -1, -1):
        if bag[a].dur <= 0:
            bag.pop(a)
 
def interact(hero, c, level, pos, itemlocs, moving):
        a = '3'
        obj = bag[c]
        while a == '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do with {}? Input number and enter.".format(obj.obj.name))
            print(" 1.Un/equip\n 2.Use\n 3.Info\n 4.Drop \n 5.Sell")
            a = input()
            if a == '1':
                if isinstance(obj.obj, weapon) == False:
                    print("You can't equip that!")
                    time.sleep(2)
                else:
                    equip(hero, obj)
                moving = False
                return
            elif a == '2':
                used = False
                if obj.obj.type == "C":
                    if hero.displvl >= 10:
                        if obj.obj.name == "Master Seal" and hero.type.classes != None: 
                            hero.promote()
                            moving = True
                            used = True
                        elif obj.obj.name == "Second Seal":
                            hero.reclass()
                            moving = True
                            used = True
                    else:
                        print("You can't use this.")
                elif obj.obj.type == "H":
                    hero.heal(obj.obj.effect)
                    moving = True
                    used = True
                else:
                    moving = False
                if used:
                    obj.dur -= 1
            elif a == '3':
                print(obj.obj.desc)
                moving = False
                time.sleep(2)
            elif a == '4':
                drop(hero, obj, level, pos, itemlocs)
                moving = True
            elif a == '5':
                sell(hero, obj)

