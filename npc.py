import collections
import shopping
import blacksmith
import tty
import time
import sys
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

npc = collections.namedtuple('npc', 'name job welcome floor level')

npcindex = []

class npcwrapper:
    def __init__(self, i, x, y):
        self.i = i
        self.level = i.floor
        self.x = x
        self.y = y

npcbase = [
npc("誠","Shopkeeper","あ、いらっしゃい！ここで買ったり売ったりしてできますよ！",[0,3,6,9,12,15,18,21,24,27,30],0),
npc("Bryan","Shopkeeper","'Sup! Welcome to my shop!",[1,4,7,10,13,16,19,22,25,28,31],1),
npc("Aku","Shopkeeper","Oh, welcome. What are you looking for?",[2,5,8,11,14,17,20,23,26,29],2),
npc("Jadine","Healer","If you are injured, 300G will heal you right up.",[0,4,8,12,16,20,24,28,32,36],0),
#npc("Tora","Alchemist","Gather items to make better items.",[255],0),
npc("Wolf","Blacksmith","Welcome! I'll enchant your weapons for a fair price!",[255],0)
]

def loadnpc():
    for i in range(len(npcbase)):
        npcindex.append(npcbase[i].floor)
#    print(npcindex) #debug

def checknpc(floor):
    npcs = []
    for i in range(len(npcbase)):
        for j in range(len(npcbase[i].floor)):
            if floor == npcbase[i].floor[j] or npcbase[i].floor[j] == 255:
                npcs.append(npcbase[i])
#    for i in range(len(npcs)):
#        print("{} should be in this level.".format(npcs[i].name)) #debug
    return npcs

def healer(hero, npc):
    sys.stdout.write("{}: {} [Y/N]".format(npc.i.name,npc.i.welcome))
    sys.stdout.flush()
    choose = 'Bleh'
    while choose != 'y' and choose != 'n':
        choose = read_key()
        choose.lower()
        if choose != 'y' and choose != 'n':
            print("Well?")
            time.sleep(1)
        if choose == 'n':
            print("Come back if you need healing!")
            time.sleep(1)
            return
        elif choose == 'y':
            if hero.HP == hero.maxHP:
                print("Oh, but you don't need healing.")
                time.sleep(1)
                return
            elif hero.money < 300:
                print("Unfortunately, you do not have enough money.")
                time.sleep(1)
                return
            else:
                hero.money -= 300
                print("Here you go! All better!")
                hero.HP = hero.maxHP
                time.sleep(1)
                return

def dothings(hero, npc, level):
    if npc.i.job == "Shopkeeper":
        shopping.shop(hero, npc, level)
    elif npc.i.job == "Healer":
        healer(hero, npc)
    elif npc.i.job == "Blacksmith" and len(hero.bag) != 0:
        blacksmith.forge(hero, npc)
