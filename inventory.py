import time
import sys
import math
from item import weapon
 
# Mitsunari-san's inventory
bag = []
 
def printinv():
    for i in range(len(bag)):
        obj = bag[i]
        sys.stdout.write("{} {} {}\n".format(i+1, obj.obj.name, obj.dur))
    print("Select a number on screen to do stuff, or input and enter any other key to exit.")
 
def dothis(hero, a, level, pos, items, moving):
    try:
       a = int(a)
    except ValueError:
       return
    if a <= len(bag):
         select = a - 1
         interact(hero, select, level, pos, items, moving)
 
def equip(hero, item):
    if hero.equip != None and hero.equip == item:
        hero.equip = None
        print("Unequipped the {}.".format(item.name))
    else:
        hero.equip = item
        print("Equipped the {}.".format(item.name))
    time.sleep(1)

def drop(hero, i, level, pos, items):
    if i == hero.equip:
        print("Unequip this first.")
        return
    index = [-1,0,1]
    for a in range(3):
        for b in range(3):
            if level[pos.x+index[a]][pos.y+index[b]] == '.' and a != 1 and b != 1:
                level[pos.x+index[a]][pos.y+index[b]] = i
                level[pos.x+index[a]][pos.y+index[b]] = '?'
                items.append(i)
                bag.remove(i)
                i.level = level
                i.x = pos.x
                i.y = pos.y
                return
    print("No dropping locations available.")

def sell(hero, i):
    if i == hero.equip:
        print("Unequip this first.")
        return

def update():
    for a in range(len(bag) - 1, -1, -1):
        if bag[a].dur <= 0:
            sys.stdout.write("{} is no more!".format(bag[a].obj.name))
            bag.pop(a)
 
def interact(hero, c, level, pos, items, moving):
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
                    equip(hero, obj.obj)
                moving = False
                return
            elif a == '2':
                used = False
                if obj.obj.type == "C":
                    if hero.displvl >= 10:
                        if obj.obj.name == "Master Seal": 
                            hero.promote()
                        else:
                            hero.reclass()
                        moving = True
                        used = True
                    else:
                        print("You can't use this yet.")
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
                drop(hero, obj, level, pos, items)
                moving = True
            elif a == '5':
                sell(hero, obj)

