import sys
import time
import inventory
from inventory import _Getch
import random
from item import catalog, itemwrapper
import tty
import termios

r = _Getch()

def shop(hero, npc, level):       
    i = 0
    addlist = []
    if hero.coins > 0:
        print('{} [Y/N]'.format(shopquotes[npc.i.level][7]))
        choose = 'Bleh'
        while choose != 'y' and choose != 'n':
            choose = r.read_key()
            choose.lower()
            if choose != 'y' and choose != 'n':
                print("Well?")
                time.sleep(1)
            elif choose == 'y':
                hero.coins -= 1
                addlist = revealhidden(level)
    while i != '3':
        sys.stdout.write("\x1b[2J\x1b[H")
        print("{}: {}\n".format(npc.i.name,npc.i.welcome)) 
        print(" 1. Buy\n 2. Sell\n 3. Leave")
        print(shopquotes[npc.i.level][0])
        i = r.read_key()
        if i == '1':
            buy(hero,npc,level,addlist)
        elif i == '2':
            sell(hero,npc)
        elif i == '3':
            print(shopquotes[npc.i.level][6])
            time.sleep(1)
            break

def revealhidden(level):
    firstlist = []
    secondlist = []
    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if level in catalog[i][j].hidden or 255 in catalog[i][j].hidden:
                firstlist.append(catalog[i][j]) #Loads the list of potential merchant items
    for k in range(3): #Determining items for final list
        secondlist.append(firstlist.pop(random.randrange(len(firstlist))))
    return secondlist

def buy(hero,npc,level,addlist):    
    if len(hero.bag) >= 5:
            print("Bag is too full.")
            time.sleep(1)
            return
    canbuy = [] 
    for i in range(len(catalog)):
        for j in range(len(catalog[i])):
            if level in catalog[i][j].shop:
                canbuy.append(catalog[i][j])
    if len(addlist) != 0:
        for i in range(len(addlist)):
            canbuy.append(addlist[i])
    while len(hero.bag) < 5:
        sys.stdout.write("\x1b[2J\x1b[H")                  
        print("Pick an item from 0-{}.".format(len(canbuy) - 1))
        for j in range(len(canbuy)):
            print('{}: {} {}G'.format(j, canbuy[j].name, canbuy[j].cost))
        print('{}: Back'.format(len(canbuy)))
        reasonable = False
        while reasonable == False:
            try:
                select = int(r.read_key())
                if select == len(canbuy):
                    return
                if select >= 0 and select < len(canbuy):
                    reasonable = True
            except ValueError:
                print("What?")
                time.sleep(1)
                continue
        cost = str(canbuy[select].cost)
        print('{} [Y/N]'.format(buildquote(shopquotes[npc.i.level][1], [canbuy[select].name, cost])))
        choose = 'Bleh'
        while choose != 'y' and choose != 'n':
            choose = r.read_key()
            choose.lower()
            if choose != 'y' and choose != 'n':
                print("Well?")
                time.sleep(1)
        if choose == 'n':
            return
        elif choose == 'y':
            if canbuy[select].cost > hero.money:
                print(shopquotes[npc.i.level][6])
            else:
                print(buildquote(shopquotes[npc.i.level][4],[canbuy[select].name]))
                amt = canbuy[select].cost
                if "Bargain" in hero.skillset:
                    print("I'll give you a discount!")
                    amt /= 2
                    amt = int(amt)
                hero.money -= amt
                hero.bag.append(itemwrapper(canbuy[select], None, None, None))
        time.sleep(1)
    return

def sell(hero,npc):
    if len(hero.bag) == 0:
        print("Bag is empty!")
        time.sleep(1)
        return
    select = 255
    while len(hero.bag) != 0:
        sys.stdout.write("\x1b[2J\x1b[H")
        print(shopquotes[npc.i.level][2])
        print("Pick an item from 0-{}.".format(len(hero.bag) - 1))
        for i in range(len(hero.bag)):
            print('{}: {}'.format(i,hero.bag[i].name))
        print('{}: Back'.format(len(hero.bag)))
        reasonable = False
        while reasonable == False:
            try:
                select = int(r.read_key())
                if select == len(hero.bag):
                    return
                if select >= 0 and select <= len(hero.bag):
                    reasonable = True
            except ValueError:
                print("What?")
                time.sleep(1)
                continue
        sell = int ((hero.bag[select].dur / hero.bag[select].obj.dur) * hero.bag[select].obj.cost * .5)
        printsum = str(sell) + "G"
        print('{} [Y/N]'.format(buildquote(shopquotes[npc.i.level][3], [printsum])))
        choose = 'Bleh'
        while choose != 'y' and choose != 'n':
            choose = r.read_key()
            choose.lower()
            if choose != 'y' and choose != 'n':
                print("Well?")
                time.sleep(1)
        if choose == 'n':
            return
        elif choose == 'y':
            if hero.equip != None and hero.bag[select].obj == hero.equip.obj:
                inventory.unequip(hero, hero.bag[select])
            print(buildquote(shopquotes[npc.i.level][4],[printsum]))
            hero.money += sell
            hero.bag.pop(select)
        time.sleep(1)
    return

def buildquote(quote, words):
    current = 0
    final = ""
    for i in range(len(quote)):
        if quote[i] == '*':
            final += words[current]
            current += 1
        else:
            final += quote[i]
    return final

shopquotes = [
["なにを差し上げる?","*の値段は...*Gぐらいだよ。買う？","なにを売る？","これ、*を上げられる。","じゃあ、どうぞ！*だよ！","残念。Gが足りないよ。","じゃあ、またどうぞ！","円玉が持ってきたかな？払う？"],
["What can I help ya with?","*'ll be worth *G. Gonna buy?","What ya sellin'?","I'll give ya *G.","Here ya go! *!","Sorry, ya don't have 'nuff money.","Come again, y'hear?","You gonna use that coin?"],
["Need a... hand? -holds out hand-","Aye, this is worth *G. How about it?","Item for gold? That's gold.","This is worth *G.","Here, *!","Huh? What's that? You need more money.","Come again!","I see that you got a coin. You using it?"]]
