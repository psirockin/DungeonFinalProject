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

def checkint():
    try:
        z = int(read_key())
    except ValueError:
        z = 0
    return z

def forge(hero, npc):
    i = 0
    while i != '3':
        sys.stdout.write("\x1b[2J\x1b[H")
        print("{}: {}".format(npc.i.name, npc.i.welcome))
        print(" 1. Rename my weapon(for free).\n 2. Make my weapon stronger.\n 3. Leave")   
        i = read_key()
        if i == '1' or i == '2':
            sys.stdout.write("\x1b[2J\x1b[H")
        if i == '1':
            rename(hero)
        elif i == '2':
            enchant(hero)
        elif i == '3':
            print("Come again!")
            time.sleep(1)
            break
        else:
            continue

def rename(hero):
    print("Pick a weapon to be renamed.")
    for i in range(len(hero.bag)):
        print('{}: {}'.format(i, hero.bag[i].name))
    print('{}: Back'.format(len(hero.bag)))
    reasonable = False
    while reasonable == False:
        try:
            select = int(read_key())
#           print('{} wields a {}.'.format(select, hero.bag[select].name))
            if select == len(hero.bag):
                return
            elif select >= 0 and select < len(hero.bag):
                if (hero.bag[select].obj.type == "W" or hero.bag[select].obj.type == "M") and hero.bag[select].obj.cost != 0:
                    reasonable = True #Because you cannot edit legendary weapons
                else:
                    print("You can't rename that.")
                    time.sleep(1)
        except ValueError:
            print("What?")
            time.sleep(1)
            continue    
    print("Please enter its new name.")
    name = input()
    print("{}'s new name will be {}. [Y/N]".format(hero.bag[select].name, name))
    choose = 'Bleh'
    while choose != 'y' and choose != 'n':
        choose = read_key()
        choose.lower()
        if choose != 'y' and choose != 'n':
            print("Well?")
            time.sleep(1)
    if choose == 'y':
        hero.bag[select].name = name
        return
    if choose == 'n':
        return

def checksum(current, amount): #check for forge points, which should not exceed 5 in each stat
    return current + amount <= 5 and amount >= 0

def enchant(hero):
    points = 0
    print("Pick a weapon to enchant. Remember, each stat point is worth half the original weapon price.")
    for i in range(len(hero.bag)):
        print('{}: {}'.format(i, hero.bag[i].name))
    print('{}: Back'.format(len(hero.bag)))
    reasonable = False
    while reasonable == False:
        try:
            select = int(read_key())
#           print('{} wields a {}.'.format(select, hero.bag[select].name))
            if select == len(hero.bag):
                return 
            elif select >= 0 and select <= len(hero.bag):
                if (hero.bag[select].obj.type == "W" or hero.bag[select].obj.type == "M") and hero.bag[select].obj.cost != 0:
                    reasonable = True
                else:
                    print("You cannot enchant that.")
                    time.sleep(1)
        except ValueError:
            print("What?")
            time.sleep(1)
            continue      
    print("How much points of attack would you like to raise? The maximum points is 5, and right now you have {} in attack.".format(hero.bag[select].forgestats[0]))
    atk = 255
    while not checksum(hero.bag[select].forgestats[0], atk):
        atk = checkint()
    points += atk
    print("How much points of accuracy would you like to raise? The maximum points is 5, and right now you have {} in accuracy.".format(hero.bag[select].forgestats[1]))
    acu = 255
    while not checksum(hero.bag[select].forgestats[1], acu):
        acu = checkint()
    points += acu        
    print("How much points of critical would you like to raise? The maximum points is 5, and right now you have {} in critical.".format(hero.bag[select].forgestats[2]))
    crt = 255    
    while not checksum(hero.bag[select].forgestats[2], crt):
        crt = checkint()
    points += crt
    gold = int(points * .5 * hero.equip.obj.cost)
    print("So {} points in attack, {} points in accuracy, and {} points in critical. That will be {}. [Y/N]".format(atk,acu,crt,gold))
    choose = 'Bleh'
    while choose != 'y' and choose != 'n':
        choose = read_key()
        choose.lower()
        if choose != 'y' and choose != 'n':
            print("Well?")
            time.sleep(1)
        if choose == 'n':
            return
        elif choose == 'y':
            if gold > hero.money:
                print("Not enough money to enchant!")
            else:
                hero.money -= gold
                print("{}'s attack has raised by {}, accuracy raised by {}, and critical raised by {}.".format(hero.bag[select].name,atk,acu*5,crt*3))
                hero.bag[select].forgestats[0] += atk
                hero.bag[select].forgestats[1] += acu
                hero.bag[select].forgestats[2] += crt
                hero.bag[select].attack += atk
                hero.bag[select].accuracy += acu * 5
                hero.bag[select].critical += crt * 3
        time.sleep(1)
    return
