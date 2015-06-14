from item import catalog, weapon, itemwrapper
from itemsys import godmake
import sys
import termios
import time
import tty

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

def potential(hero):
    items = []
    potential = []
    for i in range(len(hero.bag)): #To filter out all the edited names to "match" the requirement
        if hero.bag[i].name == hero.bag[i].obj.name:
            items.append(hero.bag[i].name)
    for i in range(len(hero.convoy)):
        if hero.convoy[i].name == hero.convoy[i].obj.name:
            items.append(hero.convoy[i].name)

    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if isinstance(catalog[i][j], weapon) and len(catalog[i][j].materials) >= 2:
                matches = 0
                for k in range(len(catalog[i][j].materials)):
                    if catalog[i][j].materials[k] in items:
                        matches += 1
                if matches == len(catalog[i][j].materials):
                    potential.append(catalog[i][j])
    return potential

def fusion(hero, potential):
    print("Please select your target weapon.")
    for i in range(len(potential)):
        obj = potential[i]
        if len(potential[i].materials) == 2:
            print("{}. {} = {} + {}".format(i, obj.name, obj.materials[0], obj.materials[1]))
        elif len(potential[i].materials) == 3:
            print("{}. {} = {} + {} + {}".format(i, obj.name, obj.materials[0], obj.materials[1], obj.materials[2]))
    print("{}. Back".format(len(potential)))
    reasonable = False
    while reasonable == False:
        try:
            select = int(read_key())
            if select == len(potential):
                return
            elif select >= 0 and select < len(potential):
                reasonable = True
        except ValueError:
            print("What?")
            time.sleep(1)
            continue
    print("You will make {}. [Y/N]".format(potential[select].name))
    choose = 'Bleh'
    while choose != 'y' and choose != 'n':
        choose = read_key()
        choose.lower()
        if choose != 'y' and choose != 'n':
            print("Well?")
            time.sleep(1)
    if choose == 'y':
        consume(hero, potential[select])
        if len(hero.bag) >= hero.capacity:
            print("Sent to convoy.")
            hero.convoy.append(godmake(potential[select].name))           
        else:
            print("Placed in bag.")
            hero.bag.append(godmake(potential[select].name))
        time.sleep(1)
        return
    if choose == 'n':
        return

def consume(hero, item): #You are guaranteed to have the materials, so this should never fail
    for i in range(len(item.materials)):
#        print("Trying to remove {}.".format(item.materials[i]))  
        removed = False
        for j in range(len(hero.bag) - 1, -1, -1):
#            print("Looking at {}.".format(hero.bag[j].name))          
            if item.materials[i] == hero.bag[j].name and not removed:
                hero.bag.pop(j)
#                print("Removed {}.".format(item.materials[i]))
                removed = True
        for k in range(len(hero.convoy) - 1, -1, -1):
#            print("Looking at {}.".format(hero.convoy[k].name))
            if item.materials[i] == hero.convoy[k].name and not removed:
                hero.convoy.pop(k)
#                print("Removed {}.".format(item.materials[i]))
                removed = True

def search():
    print("Type in a weapon's name from the list to look up the ingredients.")
    time.sleep(1)
    everything = []
    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if isinstance(catalog[i][j], weapon) and len(catalog[i][j].materials) >= 2:
                everything.append(catalog[i][j].name)
    for i in range(int(len(everything) / 2)):
        s = everything[i*2] + ", "
        if i*2+1 < len(everything) and i*2 < len(everything):
            s += everything[i*2+1]
        print(s)
    k = input()
    for i in range(len(everything)):
        if k.lower() == everything[i].lower():
            return step2(everything[i])
    print("That's not a weapon.")
    time.sleep(1)

def step2(name):
    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if name == catalog[i][j].name:
                n = catalog[i][j]
                if len(n.materials) == 3:
                    print("To make {}, you need {}, {}, and {}.".format(n.name, n.materials[0], n.materials[1], n.materials[2]))
                    time.sleep(2)
                    return
                else:
                    print("To make {}, you need {} and {}.".format(n.name, n.materials[0], n.materials[1]))
                    time.sleep(2)
                    return

def alchemy(hero, npc):
    i = 0
    while i != '3':
        sys.stdout.write("\x1b[2J\x1b[H")
        print("{}: {}".format(npc.i.name, npc.i.welcome))
        print(" 1. Fuse a weapon.\n 2. Look up a formula.\n 3. Leave")   
        i = read_key()
        if i == '1' or i == '2':
            sys.stdout.write("\x1b[2J\x1b[H")
        if i == '1':
            p = potential(hero)
            if len(hero.bag) + len(hero.convoy) == 0:
                print("You don't even have anything!")
                sys.sleep(1)
            elif len(p) == 0:
                print("No potential matches!")
                sys.sleep(1)
            else:
                fusion(hero, p)
        elif i == '2':
            search()
        elif i == '3':
            print("Come again!")
            time.sleep(1)
            break
        else:
            continue
