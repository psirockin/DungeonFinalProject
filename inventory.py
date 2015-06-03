import time
import sys
import math
from item import weapon
import tty
import termios

def read_key():
    '''
    Read a single key from stdin
    '''
    try:
        fd = sys.stdin.fileno()
        tty_settings = termios.tcgetattr(fd)
        tty.setraw(fd)
 
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, tty_settings)
    return key

# Mitsunari-san's inventory

def take_out(hero, k, level, pos, itemlocs, moving):
    hero.bag.append(hero.convoy.pop(k))
    printinv(hero, level, pos, itemlocs, moving, hero.convoy, "TAKE OUT")

def put_in(hero, k, level, pos, itemlocs, moving):
    hero.convoy.append(hero.bag.pop(k)) #Try to make a while loop in order to not take things out one at a time
    printinv(hero, level, pos, itemlocs, moving, hero.bag, "PUT IN")

def printinv(hero, level, pos, itemlocs, didyoumove, inv, command):
    sys.stdout.write("\x1b[2J\x1b[H")
    print("Select a number on screen to do stuff.")   
    for i in range(len(inv)):
        obj = inv[i]
        sys.stdout.write("{}: {} {}\n".format(i, obj.name, obj.dur))
    print("{}: Back\n".format(len(inv)))
    k = int(read_key())
    if k == len(inv):
        return
    elif command == "BAG":
        dothis(hero, k, level, pos, itemlocs, didyoumove, inv)
    elif command == "TAKE OUT":
        take_out(hero, k, level, pos, itemlocs, didyoumove)
    elif command == "PUT IN":
        put_in(hero, k, level, pos, itemlocs, didyoumove)

def dothis(hero, a, level, pos, itemlocs, moving, inv):
    o = False
    while o == False:
        try:
            a = int(a)
            if a == len(inv):
                return
            elif a >= 0 and a <= len(inv):
                o = True 
        except ValueError:
                continue
    select = a
    interact(hero, select, level, pos, itemlocs, moving)

def unequip(hero, item):
    hero.equip = None
    print("Unequipped {}.".format(item.name))

def equip(hero, item):
    if hero.equip == None and item.obj.school in hero.type.weapons:
        hero.equip = item
        print("Equipped {}.".format(item.name))
    else:
        print("You can't equip this!")
    time.sleep(1)

def change(hero, takeout, takein):
    if takeout != None and takein.obj.school in hero.type.weapons:
        unequip(hero, takeout)
    equip(hero, takein)

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
#               print("This is at {}, {}.".format(i.x,i.y))
                itemlocs.append(i)
                hero.bag.remove(i)
                return
    print("No dropping locations available.")

def sell(hero, i):
    if hero.equip != None and i.obj == hero.equip.obj:
        equip(hero, i)
    for a in range(len(hero.bag) - 1, -1, -1):
        if i.obj == hero.bag[a].obj:
            hero.money += int(i.obj.cost * .25)
            hero.bag.pop(a)
            return

def update(hero):
    for a in range(len(hero.bag) - 1, -1, -1):
        if hero.bag[a].dur <= 0:
            hero.bag.pop(a)

def convoy(hero, level, pos, items, moving):
        a = '0'
        while a != '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do?")
            print(" 1.Take out\n 2.Put in\n 3.Back")
            a = read_key()
            if a == '1':
                if len(hero.bag) >= hero.capacity:
                    print("Bag full.")
                    time.sleep(1)
                elif len(hero.convoy) == 0:
                    print("Convoy empty.")
                    time.sleep(1)
                else:
                    printinv(hero, level, hero.position, items, moving, hero.convoy, "TAKE OUT")
            elif a == '2':
                if len(hero.convoy) >= hero.convoymax:
                    print("Convoy full.")
                elif len(hero.bag) == 0:
                    print("Bag empty.")
                else:
                    printinv(hero, level, hero.position, items, moving, hero.bag, "PUT IN")    
            elif a == '3':
                return
 
def interact(hero, c, level, pos, itemlocs, moving):
        a = '3'
        obj = hero.bag[c]
        while a == '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do with {}? Input number.".format(obj.name))
            print(" 1.Un/equip\n 2.Use\n 3.Info\n 4.Drop \n 5.Sell\n 6.Back")
            a = read_key()
            if a == '1':
                if isinstance(obj.obj, weapon) == False:
                    print("You can't equip that!")
                    time.sleep(2)
                else:
                    change(hero, hero.equip,obj)
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
                elif obj.obj.type == "B": #I used the req parameter here because I don't wanna add another parameter.
                    hero.boost(obj.obj.req,obj.obj.effect)
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
            elif a == '6':
                printinv(hero, level, pos, itemlocs, moving, hero.bag, "BAG")

