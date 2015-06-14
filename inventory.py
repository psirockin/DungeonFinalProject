import time
import sys
import math
from item import weapon
import tty
import termios
from skills import Weaponfaire
import skills

statskills = ["HP +5","Strength +2","Magic +2","Skill +2","Speed +2","Luck +4","Defense +2","Resist +2","Resist +10"]
faireskills = ["Swordfaire","Lancefaire","Axefaire","Bowfaire","Tomefaire"]

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def read_key(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()
#################################################################

r = _Getch()

# Mitsunari-san's inventory

def take_out(hero, k, level, pos, itemlocs, moving):
    hero.bag.append(hero.convoy.pop(k))
    if len(hero.bag) < hero.capacity and len(hero.convoy) != 0:
        printinv(hero, level, pos, itemlocs, moving, hero.convoy, "TAKE OUT")

def put_in(hero, k, level, pos, itemlocs, moving):
    hero.convoy.append(hero.bag.pop(k))
    if len(hero.convoy) < hero.convoymax and len(hero.bag) != 0:
        printinv(hero, level, pos, itemlocs, moving, hero.bag, "PUT IN")

def take_skill(hero, k):
    skill = hero.inactiveskills.pop(k)
    hero.skillset.append(skill)
    if skill in faireskills:
        Weaponfaire(hero, skill, 5)
    elif skill in statskills:
        if skill == "HP +5":
            print("Added 5 HP.")
            hero.stats[0] += 5
            hero.max[0] += 5
        elif skill == "Strength +2":
            hero.stats[1] += 2
            hero.max[1] += 2
        elif skill == "Magic +2":
            hero.stats[2] += 2
            hero.max[2] += 2
        elif skill == "Skill +2":
            hero.stats[3] += 2
            hero.max[3] += 2
        elif skill == "Speed +2":
            hero.stats[4] += 2
            hero.max[4] += 2
        elif skill == "Luck +4":
            hero.stats[5] += 4
            hero.max[5] += 2
        elif skill == "Defense +2":
            hero.stats[6] += 2
            hero.max[6] += 2
        elif skill == "Resist +2":
            hero.stats[7] += 2
            hero.max[7] += 2
        elif skill == "Resist +10":
            hero.stats[7] += 10
            hero.max[7] += 10
        elif skill == "All Stats +2":
                for i in range(1,8,1):
                    hero.stats[i] += 2
                    hero.max[i] += 2
    elif skill == "Shadowgift":
        hero.weapons.append("Dark Magic")
    hero.setstats()
    if len(hero.inactiveskills) != 0 and len(hero.skillset) < 5:
        printskills(hero, hero.inactiveskills, "TAKE OUT")

def put_skill(hero, k):
    skill = hero.skillset[k]
    if skill in faireskills:
        Weaponfaire(hero, skill, -5) 
    elif skill in statskills:
        if skill == "HP +5":
            hero.stats[0] -= 5
            hero.max[0] -= 5
        elif skill == "Strength +2":
            hero.stats[1] -= 2
            hero.max[1] -= 2
        elif skill == "Magic +2":
            hero.stats[2] -= 2
            hero.max[2] -= 2
        elif skill == "Skill +2":
            hero.stats[3] -= 2
            hero.max[3] -= 2
        elif skill == "Speed +2":
            hero.stats[4] -= 2
            hero.max[4] -= 2
        elif skill == "Luck +4":
            hero.stats[5] -= 4
            hero.max[5] -= 2
        elif skill == "Defense +2":
            hero.stats[6] -= 2
            hero.max[6] -= 2
        elif skill == "Resist +2":
            hero.stats[7] -= 2
            hero.max[7] -= 2
        elif skill == "Resist +10":
            hero.stats[7] -= 10
            hero.max[7] -= 10
        elif skill == "All Stats +2":
                for i in range(1,8,1):
                    hero.stats[i] -= 2
                    hero.max[i] -= 2
    elif skill == "Shadowgift":
        hero.weapons.remove("Dark Magic")
    hero.skillset.pop(k)
    hero.inactiveskills.append(skill)
    hero.setstats()
    if len(hero.skillset) != 0:
        printskills(hero, hero.skillset, "PUT IN")

def printinv(hero, level, pos, itemlocs, didyoumove, inv, command):
    sys.stdout.write("\x1b[2J\x1b[H")
    print("Select a number on screen to do stuff.")   
    for i in range(len(inv)):
        obj = inv[i]
        sys.stdout.write("{}: {} {}\n".format(i, obj.name, obj.dur))
    print("{}: Back\n".format(len(inv)))
    o = False
    while o == False:
        try:
            k = int(r.read_key())
            if k == len(inv):
                return
            elif k >= 0 and k < len(inv):
                o = True 
        except ValueError:
            continue
    if command == "BAG":
        dothis(hero, k, level, pos, itemlocs, didyoumove, inv)
    elif command == "TAKE OUT":
        take_out(hero, k, level, pos, itemlocs, didyoumove)
    elif command == "PUT IN":
        put_in(hero, k, level, pos, itemlocs, didyoumove)

def printskills(hero, inv, command):
    lowernames = []
    for i in range(len(inv)):
        lowernames.append(inv[i].lower())
    sys.stdout.write("\x1b[2J\x1b[H")
    print("Type the name of the skill to take out or put in.") 
    for i in range(len(inv)):
        sys.stdout.write("{}: {}\n".format(i, inv[i]))
    print("{}: Back\n".format(len(inv)))
    o = False
    while o == False:
        k = input().lower()
        if k == 'back':
            return
        elif k in lowernames:
            o = True 
        else:
            continue
    c = None
    for i in range(len(inv)):
        if lowernames[i] == k:
            c = i
    if command == "TAKE OUT":
        take_skill(hero, c)
    elif command == "PUT IN":
        put_skill(hero, c)

def dothis(hero, a, level, pos, itemlocs, moving, inv):
    o = False
    while o == False:
        try:
            a = int(a)
            if a == len(inv):
                return
            elif a >= 0 and a < len(inv):
                o = True 
        except ValueError:
            continue
    select = a
    interact(hero, select, level, pos, itemlocs, moving)

def unequip(hero, item):
    n = item.obj.school
    if n == "Magic":
        n = "Tome"
    n += "faire"
    Weaponfaire(hero, n, -5)
    hero.equip = None
    print("Unequipped {}.".format(item.name))
    hero.calc_things()
    if item.obj.boost != None:
        hero.statminus(item)

def equip(hero, item):
    if hero.equip == None and item.obj.school in hero.type.weapons:
        hero.equip = item
        print("Equipped {}.".format(item.name))
        n = item.obj.school
        if n == "Magic":
            n = "Tome"
        n += "faire"
        Weaponfaire(hero, n, 5)
        hero.calc_things()
        if item.obj.boost != None:
#           print(item.obj.boost)
            hero.statplus(item)
    else:
        print("You can't equip this!")
    time.sleep(1)

def change(hero, takeout, takein):
    if takeout != None and takein.obj.school in hero.type.weapons:
        unequip(hero, takeout)
        time.sleep(1)
    if takeout != takein:
        equip(hero, takein)

def drop(hero, i, level, pos, itemlocs):
    index = [-1,0,1]
    for a in range(3):
        for b in range(3):
            if (level[pos.x+index[a]][pos.y+index[b]] == '.' or level[pos.x+index[a]][pos.y+index[b]] == '#') and (level[pos.x+index[a]][pos.y+index[b]] != pos):
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

def enemydrop(i, level, pos, itemlocs):
    index = [-1,0,1]
    for a in range(3):
        for b in range(3):
            if level[pos.x+index[a]][pos.y+index[b]] == '.' or level[pos.x+index[a]][pos.y+index[b]] == '#':
                level[pos.x+index[a]][pos.y+index[b]] = i
                level[pos.x+index[a]][pos.y+index[b]] = '?'                
                i.level = level
                i.x = pos.x + index[a]
                i.y = pos.y + index[b]
                print("This is at {}, {}.".format(i.x,i.y))
                itemlocs.append(i)
                return i.name
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
            a = r.read_key()
            if a == '1':
                if len(hero.bag) >= hero.capacity:
                    print("Bag full.")
                    time.sleep(1)
                elif len(hero.convoy) == 0:
                    print("Convoy empty.")
                    time.sleep(1)
                else:
                    printskills(hero, level, hero.position, items, moving, hero.convoy, "TAKE OUT")
            elif a == '2':
                if len(hero.convoy) >= hero.convoymax:
                    print("Convoy full.")
                elif len(hero.bag) == 0:
                    print("Bag empty.")
                else:
                    printskills(hero, level, hero.position, items, moving, hero.bag, "PUT IN")    
            elif a == '3':
                return

def skillswap(hero, level, pos, items, moving):
        a = '0'
        while a != '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do?")
            print(" 1.Take out\n 2.Put in\n 3.Back")
            a = r.read_key()
            if a == '1':
                if len(hero.skillset) == 5:
                    print("Skills full.")
                    time.sleep(1)
                elif len(hero.inactiveskills) == 0:
                    print("No skills to take out.")
                    time.sleep(1)
                else:
                    printskills(hero, hero.inactiveskills, "TAKE OUT")
            elif a == '2':
                if len(hero.skillset) == 0:
                    print("No skills to put in.")
                else:
                    printskills(hero, hero.skillset, "PUT IN")    
            elif a == '3':
                return
 
def interact(hero, c, level, pos, itemlocs, moving):
        a = '3'
        obj = hero.bag[c]
        while a == '3':
            sys.stdout.write("\x1b[2J\x1b[H")
            print("What would you like to do with {}? Input number.".format(obj.name))
            print(" 1.Un/equip\n 2.Use\n 3.Info\n 4.Drop \n 5.Sell\n 6.Back")
            a = r.read_key()
            if a == '1':
                if not isinstance(obj.obj, weapon):
                    print("You can't equip that!")
                    time.sleep(2)
                else:
                    change(hero, hero.equip, obj)
                moving = False
                return
            elif a == '2':
                used = False
                if obj.obj.type == "C":
                    if hero.displvl >= 10 or hero.promoted == 1:
                        if obj.obj.name == "Master Seal" and hero.type.classes != None: 
                            moving = True
                            used = True
                            hero.promote()
                        elif obj.obj.name == "Second Seal":
                            moving = True
                            used = True
                            hero.reclass()
                    else:
                        print("You can't use this.")
                elif obj.obj.type == "H":
                    hero.heal(obj.obj.effect)
                    time.sleep(1)
                    moving = True
                    used = True
                elif obj.obj.effect != None and "Heal" in obj.obj.effect:
                    hero.heal(obj.obj.boost)
                    used = True
                elif obj.obj.type == "B": #I used the req parameter here because I don't wanna add another parameter.
                    hero.boost(obj.obj.req,obj.obj.effect)
                    time.sleep(1)
                    moving = True
                    used = True
                else:
                    moving = False
                if used:
                    obj.dur -= 1
                    update(hero)
                    time.sleep(1)
                else:
                    print("You can't use this.")
                    time.sleep(1)
            elif a == '3':
                print(obj.obj.desc)
                if isinstance(obj.obj, weapon):
                    print('Might: {} Accuracy: {}% Crit Rate: {}% Effective: {} Range: {}'.format(obj.attack, obj.accuracy, obj.critical, obj.obj.weakness, obj.obj.range))
                moving = False
                time.sleep(2)
            elif a == '4':
                if hero.equip != None and obj.obj == hero.equip.obj:
                    equip(hero, i)
                drop(hero, obj, level, pos, itemlocs)
                moving = True
            elif a == '5':
                sell(hero, obj)
            elif a == '6':
                printinv(hero, level, pos, itemlocs, moving, hero.bag, "BAG")

