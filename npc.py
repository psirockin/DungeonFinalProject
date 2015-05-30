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
npc("誠","Shopkeeper","あ、いらっしゃい！ここは初心者のショップだよ！",[0],0),
npc("Jin","Shopkeeper","'Sup! Welcome to my shop! Y'can find decent goods here.",[6],1),
npc("Aku","Shopkeeper","Oh, welcome. I have some slightly better goods.",[13],2),
npc("Jadine","Healer","If you are injured, 300G will heal you right up.",[0,4,8,12,16,20,24,28,32,36],0),
#npc("Christopher","Alchemist","Gather items to make better items.",[255],0),
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
    sys.stdout.write("\x1b[2J\x1b[H")
    print("{}: {} [Y/N]".format(npc.i.name,npc.i.welcome))
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
        shopping.shop(hero, npc)
    elif npc.i.job == "Healer":
        healer(hero, npc)
    elif npc.i.job == "Blacksmith" and len(hero.bag) != 0:
        blacksmith.forge(hero, npc)
