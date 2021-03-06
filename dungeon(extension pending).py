#! /usr/bin/env python3
 
import itemsys
import help
from inventory import bag, printinv, dothis
import collections
import copy
import random
import sys
import termios
import tty
import time
import item
 
#control variables
capacity = 5
MOVEABLE = ['.', '+', '#', '>', '<','?']
statread = ["HP","Strength","Magic","Skill","Speed","Luck","Defense","Resist"]
a = None
f = None
direction = None
Equip = None
SuitableLvl = 1
 
# Dimensions of the dungeon
X_DIM = 80
Y_DIM = 20
 
# Min and Max number of rooms per floor
NUM_ROOMS = (3, 5)
 
# Min and Max height and width of a room
ROOM_HEIGHT = (5, 8)
ROOM_WIDTH = (5, 20)
 
# Minimum separation between rooms
MIN_SEP = 2

# 10% an enemy will spawn for every move.
MONSTER_PROB = 0.1
 
Room = collections.namedtuple('Room', 'x y width height')
Point = collections.namedtuple('Point', 'x y')
 
items = []
 
monsters = []
 
MONSTERS = [
    ['Archer', 'a', [16, 5, 0, 3, 4, 0, 6, 0], [80, 20, 0, 30, 30, 0, 20, 10]],
    ['Fighter', 'f', [20, 5, 0, 1, 7, 0, 3, 0], [90, 50, 0, 30, 20, 0, 50, 5]],
    ['Mercenary', 'm', [16, 4, 0, 8, 10, 0, 5, 0], [80, 30, 0, 20, 20, 0, 30, 10]],
]

####################

class unit(object):
    def __init__(self, name):
        self.name = name
        self.equip = None
        self.HP = 10
        self.maxHP = 10
        self.strength = 10
        self.magic = 10
        self.skill = 10
        self.speed = 10
        self.luck = 10
        self.defense = 10
        self.resist = 10

    def howtoattack(self,target):
        if self.equip == None:
            return self.struggle(target)
        else:
            return self.attacking(self.equip, target, 0)

    def struggle(self,target):
        damage = 0
        critical = (random.randrange(100) <= self.skill / 2)
        accuracy = 100 + (self.skill * 3 + self.luck) / 2
        if accuracy < random.randrange(100):
            sys.stdout.write("Missed! ")
            return 0
        damage = self.strength - target.defense
        if damage <= 0:
                damage = 1
        if critical:
                damage *= 3
                print("CRITICAL! ")
        target.HP -= damage
        return damage

    def attacking(self, weapon, target, time):
        damage = 0
        critical = (random.randrange(100) <= self.equip.critical + self.skill / 2)
        accuracy = weapon.accuracy + (self.skill * 3 + self.luck) / 2
        ############ These are all skill checks
            

        ############
        if accuracy < random.randrange(100):
            sys.stdout.write("Missed! ")
            return 0
        if weapon.type == "W":
            damage = self.strength + weapon.attack - target.defense
            if damage <= 0:
                damage = 1
            if critical:
                print("CRITICAL!" )
                damage *= 3
            target.HP -= damage
            return damage
        elif weapon.type == "M":
            damage = self.magic + weapon.attack - target.resist
            if damage <= 0:
                damage = 1
            if critical:
                damage *= 3
            target.HP -= damage
            if weapon.effect == "Drain":
                self.heal(damage / 2)
            elif weapon.effect == "Brave" and time < 1:
                self.attacking(weapon, target, time + 1)
            return damage

    def heal(self,amount):
        realheal = amount
        self.HP += amount
        if self.HP >= self.maxHP:
            realheal -= self.maxHP - self.HP
            self.HP = self.maxHP
        sys.stdout.write("Recovered {} HP.".format(realheal))
####################
 
class Monster(unit):
    def __init__(self, unit, pos, what, base, growths, equip):
        super()
        self.pos = pos
        self.what = what
        self.stats = base
        self.equip = equip
        self.HP = self.stats[0]
        self.maxHP = self.stats[0]
        self.strength = self.stats[1]
        self.magic = self.stats[2]
        self.skill = self.stats[3]
        self.speed = self.stats[4]
        self.luck = self.stats[5]
        self.defense = self.stats[6]
        self.resist = self.stats[7]
        self.lvl = SuitableLvl * 2
        self.growth = growths
        self.old = '.' # monsters always spawn on a '.'
 
    def move(self, level, newpos):
        level[self.pos.x][self.pos.y] = self.old
        self.old = level[newpos.x][newpos.y]
        level[newpos.x][newpos.y] = 'm'
        self.pos = newpos
    
    def lvlchange(self): # 1 level higher or lower than base   
        r = random.randrange(3)
        if r == 1:
            self.lvl -= 1
        elif r == 2:
            self.lvl += 1

    def die(self, level):
        level[self.pos.x][self.pos.y] = self.old
            
    def grow(self, lvl): #These growth rates are automated.
        for i in range(lvl):
            g = random.randrange(100)
            if g <= self.growth[0]:
                self.HP += 1
            if g <= self.growth[1]:
                self.strength += 1
            if g <= self.growth[2]:
                self.magic += 1
            if g <= self.growth[3]:
                self.skill += 1
            if g <= self.growth[4]:
                self.speed += 1
            if g <= self.growth[5]:
                self.luck += 1
            if g <= self.growth[6]:
                self.defense += 1
            if g <= self.growth[7]:
                self.resist += 1
 
####################
 
class hero(unit):
    def __init__(self, unit, a, f):
        super()
        self.stats = [19,6,5,5,6,4,6,4]
        self.default = [80,55,50,50,50,55,40,30] #HP, Str, Mag, Skl, Spd, Lck, Def, Res
        self.name = name
        self.exp = 0
        self.level = 1
        self.bag = bag       
        self.skillset = []
 
    def expgain(self,exp):
        self.exp += exp
        while self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print("Level up!")
            self.grow()
 
    def grow(self):
        g = random.randrange(100)
        if g <= self.default[0]:
            self.HP += 1
        if g <= self.default[1]:
            self.strength += 1
        if g <= self.default[2]:
            self.magic += 1
        if g <= self.default[3]:
            self.skill += 1
        if g <= self.default[4]:
            self.speed += 1
        if g <= self.default[5]:
            self.luck += 1
        if g <= self.default[6]:
            self.defense += 1
        if g <= self.default[7]:
            self.resist += 1
 
    def assetmod(self,a):
        if a == 0:
            self.default[a] += 15
            self.default[6] += 5
            self.default[7] += 5
        elif a == 1:
            self.default[a] += 10
            self.default[3] += 5
            self.default[6] += 5
        elif a == 2:
            self.default[a] += 10
            self.default[4] += 5
            self.default[7] += 5
        elif a == 3:
            self.default[a] += 10
            self.default[1] += 5
            self.default[6] += 5
        elif a == 4:
            self.default[a] += 10
            self.default[3] += 5
            self.default[5] += 5
        elif a == 5:
            self.default[a] += 10
            self.default[1] += 5
            self.default[2] += 5
        elif a == 6:
            self.default[a] += 10
            self.default[5] += 5
            self.default[7] += 5
        elif a == 7:
            self.default[a] += 10
            self.default[2] += 5
            self.default[4] += 5
 
    def flawmod(self,a):
        if a == 0:
            self.default[a] -= 15
            self.default[6] -= 5
            self.default[7] -= 5
        elif a == 1:
            self.default[a] -= 10
            self.default[3] -= 5
            self.default[6] -= 5
        elif a == 2:
            self.default[a] -= 10
            self.default[4] -= 5
            self.default[7] -= 5
        elif a == 3:
            self.default[a] -= 10
            self.default[1] -= 5
            self.default[6] -= 5
        elif a == 4:
            self.default[a] -= 10
            self.default[3] -= 5
            self.default[5] -= 5
        elif a == 5:
            self.default[a] -= 10
            self.default[1] -= 5
            self.default[2] -= 5
        elif a == 6:
            self.default[a] -= 10
            self.default[5] -= 5
            self.default[7] -= 5
        elif a == 7:
            self.default[a] -= 10
            self.default[2] -= 5
            self.default[4] -= 5
 
    def adjust(self,a,f):
        if a == 0:
            self.stats[a] += 5
        elif a == 5:
            self.stats[a] += 4
        else:
            self.stats[a] += 2
        if f == 0:
            self.stats[f] -= 3
        elif f == 5:
            self.stats[f] -= 2
        else:
            self.stats[f] -= 1
        self.maxHP = self.stats[0]
        self.HP = self.stats[0]
        self.strength = self.stats[1]
        self.magic = self.stats[2]
        self.skill = self.stats[3]
        self.speed = self.stats[4]
        self.luck = self.stats[5]
        self.defense = self.stats[6]
        self.resist = self.stats[7]
 
    def set_position(self, newpos):
        self.position = newpos

###############

def enemypos(dir):
    if dir == "N":
        p = Point(char.position.x, char.position.y-2)
    elif dir == "E":
        p = Point(char.position.x+2, char.position.y)
    elif dir == "W":
        p = Point(char.position.x-2, char.position.y)
    elif dir == "S":
        p = Point(char.position.x, char.position.y+2)
    return p 

def random_door(level, room):
    '''
    Picks a random side for a door in and out of a room.
    '''
    deltax = deltay = 0
 
    # Pick random side on room
    side = random.randint(0, 3)
    if side == 0 or side == 2:
        deltay = random.randint(1, room.height-1)
    elif side == 1 or side == 3:
        deltax = random.randint(1, room.width-1)
 
    if side == 1:
        deltay = room.height
    elif side == 2:
        deltax = room.width
 
    return Point(room.x + deltax, room.y + deltay)
 
def dxdy(p):
    '''
    Yield the locations around the position to the left, right, above, and
    below.
    '''
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        yield Point(p.x+dx, p.y+dy)
 
def fill_room(level, room):
    '''
    Fill in a new room in the level, drawing borders around the room and
    periods inside the room. Returns a copy of the level with the new room
    added if the room did not collide with an existing room. Returns None if
    there was a collision.
    '''
    new_level = copy.deepcopy(level)
 
    # Populate new_level with room
    for j in range(room.height+1):
        for i in range(room.width+1):
            # Check if there's already a room here
            if level[room.x+i][room.y+j] != None:
                return None
 
            if j == 0 or j == room.height:
                new_level[room.x+i][room.y+j] = '-'
            elif i == 0 or i == room.width:
                new_level[room.x+i][room.y+j] = '|'
            else:
                new_level[room.x+i][room.y+j] = '.'
 
    # Ensure MIN_SEP space exists to left and right
    for j in range(room.height+1):
        if level[room.x-MIN_SEP][room.y+j] != None:
            return None
        if level[room.x+room.width+MIN_SEP][room.y+j] != None:
            return None
 
    # Ensure MIN_SEP space exists above and below
    for i in range(room.width+1):
        if level[room.x+i][room.y-MIN_SEP] != None:
            return None
        if level[room.x+i][room.y+room.height+MIN_SEP] != None:
            return None
 
    return new_level
 
 
def dist(p0, p1):
    '''
    Compute the euclidean distance between two points
    '''
    return ((p0.x - p1.x)**2 + (p0.y - p1.y)**2)**0.5
 
 
def create_path(level, p0, p1):
    '''
    Connect two points on the map with a path.
    '''
    # Compute all possible directions from here
    points = []
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        p = Point(p0.x+dx, p0.y+dy)
        if p == p1:
            return True
 
        if p.x >= X_DIM or p.x < 0:
            continue
        if p.y >= Y_DIM or p.y < 0:
            continue
        if level[p.x][p.y] not in [None, '#']:
            continue
 
        points.append(p)
 
    # Sort points according to distance from p1
    points.sort(key=lambda i: dist(i, p1))
 
    for p in points:
        old, level[p.x][p.y] = level[p.x][p.y], '$'
        if create_path(level, p, p1):
            level[p.x][p.y] = '#'
            return True
        level[p.x][p.y] = old
 
    return False
 
def generate(level, item):
    points = []
    for j in range(1, len(level)):
        for i in range(1, len(level[0])):
            if level[j][i] == ".":
                points.append(Point(j, i))
    if len(points) == 0:
        return False
    p = random.choice(points)
    level[p.x][p.y] = item
    return p
 
def add_to_floor(level, room, item):
    '''
    Add staircase to random location within the room
    '''
    points = []
 
    for j in range(1, room.height):
        for i in range(1, room.width):
            if level[room.x+i][room.y+j] == ".":
                points.append(Point(room.x+i, room.y+j))
    if len(points) == 0:
        return False
    p = random.choice(points)
    level[p.x][p.y] = item
    return p
 
def make_item(level, p):
    i = item.itemwrapper(itemsys.generate_item(), level, p.x, p.y)
    items.append(i)
 
def add_item(level, room, item):
    level[pos.x][pos.y] = item
    return True
 
def make_level():
    '''
    Create a X_DIM by Y_DIM 2-D list filled with a random assortment of rooms.
    '''
    level = []
    for i in range(X_DIM):
        level.append([None] * Y_DIM)
 
    monsters = []
    rooms = []
 
    # Randomly N generate room in level
    for i in range(random.randint(*NUM_ROOMS)):
        # Keep looking, there should be *somewhere* to put this room...
        while True:
            # Generate random room
            x = random.randint(MIN_SEP, X_DIM)
            y = random.randint(MIN_SEP, Y_DIM)
            height = random.randint(*ROOM_HEIGHT)
            width = random.randint(*ROOM_WIDTH)
 
            # Check map boundary
            if x + width + MIN_SEP >= X_DIM:
                continue
            if y + height + MIN_SEP >= Y_DIM:
                continue
 
            room = Room(x, y, width, height)
            new_level = fill_room(level, room)
 
            if not new_level:
                continue
 
            level = new_level
            rooms.append(room)
            for i in range(1):
                post = add_to_floor(level, room, '?')
                make_item(level, post)
            break
 
    # Connect the rooms with random paths
    for i in range(len(rooms)-1):
        # Pick two random doors
        door0 = random_door(level, rooms[i])
        door1 = random_door(level, rooms[i+1])
 
        level[door0.x][door0.y] = '+'
        level[door1.x][door1.y] = '+'
 
        # Actually connect them
        if not create_path(level, door0, door1):
            # TODO: Could happen... what should we do?
            pass
 
    # Pick random room for stairs leading up and down
    up, down = random.sample(rooms, 2)
    add_to_floor(level, up, '<')
    add_to_floor(level, down, '>')
    return level
 
 
def find_staircase(level, staircase):
    '''
    Scan the level to determine where a particular staircase is
    '''
    for j in range(Y_DIM):
        for i in range(X_DIM):
            if level[i][j] == staircase:
                return Point(i, j)
    return None
 
 
def print_level(level):
    '''
    Print the level using spaces when a tile isn't set
    '''
    for j in range(Y_DIM):
        for i in range(X_DIM):
            if level[i][j] == None:
                sys.stdout.write(' ')
            elif level[i][j] == 'm':
                for m in monsters:
                    if m.pos.x == i and m.pos.y == j:
                        sys.stdout.write(m.what)
                        break
            else:
                sys.stdout.write(level[i][j])
        sys.stdout.write('\n')
 
 
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
 
 
if __name__ == '__main__':
    # Initialize the first level
    current = 0
 
    print("Please enter your name.")
    n = input()
    print("Please enter your asset(1-8).")
    print(statread)
    a = int(input())
    a -= 1
    print("Please enter your flaw(1-8).")
    print(statread)
    f = int(input())
    f -= 1
    tchar = unit(n)
    char = hero(tchar,a,f)
    char.assetmod(a)
    char.flawmod(f)
    char.adjust(a,f)    
 
    levels = []
    levels.append(make_level())
 
    char.set_position(find_staircase(levels[current], '<'))
    
## Initial Inventory ##
    
    #item1 = itemsys.make_item("Vulnerary")
    #bag.append(item1)
    
#######################

    sys.stdout.write("\x1b[2J\x1b[H")
    while True:
        wait = False

        # Clear the terminal
        sys.stdout.write("\x1b[2J\x1b[H")

        if char.HP <= 0:
            print("Game over!")
            break        
        
        level = levels[current]
 
        # Swap in an '@' character in the position of the character, print the
        # level, and then swap back
        old, level[char.position.x][char.position.y] = level[char.position.x][char.position.y], 'Д' #changed @ with Д
        print_level(level)
        level[char.position.x][char.position.y] = old
 
        sys.stdout.write('{} HP:{}/{}  Lvl:{}  EXP:{}/100'.format(char.name,char.HP, char.maxHP, char.level, char.exp))
        sys.stdout.write(' Str:{} Mag:{} Def:{} Res:{} Skl:{} Spd:{} Lck:{}'.format(char.strength, char.magic, char.defense, char.resist, char.skill, char.speed, char.luck))
        sys.stdout.write('\n')
        if char.equip != None:
            sys.stdout.write('Equipped: {}'.format(char.equip.name))
        else:
            sys.stdout.write('Equipped: Nothing!')
        sys.stdout.write('\n')
 
        if level[char.position.x][char.position.y] == '?':
            for a in range(len(items)):
                if items[a].x == char.position.x and items[a].y == char.position.y:
                    i = items[a]
            if len(bag) < capacity:
                bag.append(i)
                level[char.position.x][char.position.y] = '.'
                print(i.obj.name," obtained")
                items.remove(i)
            else:
                print("Bag full")
 
        key = read_key()
 
        if key == 'q':
            break
        elif key == 'a': #old keys in this order: h,j,k,l
            newpos = Point(char.position.x-1, char.position.y)
            direction = "W"
        elif key == 's':
            newpos = Point(char.position.x, char.position.y+1)
            direction = "S"
        elif key == 'w':
            newpos = Point(char.position.x, char.position.y-1)
            direction = "N"
        elif key == 'd':
            newpos = Point(char.position.x+1, char.position.y)
            direction = "E"
#        elif key == 'e':
#            if char.equip != None and char.equip.range == 2:
#                target = enemypos(direction)
#                if target in MONSTERS:
#                    char.attack(char.equip)
        elif key == 'h':
            direction = "NULL"
            help.display()
        elif key == 'i':
            if len(bag) == 0:
                continue
            else:
                direction = "NULL"
                sys.stdout.write("\x1b[2J\x1b[H")
                printinv()
                k = input()
                dothis(char, k, level, char.position, items)
                print_level(level)
        else:
            continue

        if random.random() < MONSTER_PROB:
                p = generate(level,'m')
                if p:
                    m1 = MONSTERS[random.randrange(len(MONSTERS))]
                    m = unit.Monster(p,m1[0],m1[1],m1[2],m1[3])
                    m.lvlchange()
                    m.grow(m.lvl)
                    monsters.append(m)
 
        if level[newpos.x][newpos.y] == '>':
            # Moving down a level
            if current == len(levels) - 1:
                levels.append(make_level())
            #clear monsters
            monsters = []
            current += 1
            newpos = find_staircase(levels[current], '<')
        elif level[newpos.x][newpos.y] == '<':
            # Moving up a level
            if current > 0:
                #clear monsters
                monsters = []
                current -= 1
                newpos = find_staircase(levels[current], '>')

        elif level[newpos.x][newpos.y] == '?':
            newitem = True

        elif level[newpos.x][newpos.y] == 'm':
            # Walked into a monster, attack!
            for m in monsters:
               if m.pos == newpos:
                    d = char.howtoattack(m)
                    sys.stdout.write('{} has dealt {} damage to {}.\n'.format(char.name, d, m.name))
            newpos = char.position

        elif level[newpos.x][newpos.y] not in MOVEABLE:
            # Hit a wall, should stay put
            newpos = char.position
 
        char.set_position(newpos)
       
        # Update the monsters
        for m in monsters:
            if m.HP <= 0:
                m.die(level)
                monsters.remove(m)
                sys.stdout.write('{} has killed a {}.\n'.format(char.name, m.name))
                wait = True
                continue

            d0 = dist(newpos, m.pos)
            if d0 < 15:
                # Move the monster towards the player
                for p in dxdy(m.pos):
                    d1 = dist(newpos, p)
                    if newpos == p:
                        # Monster moves into player, attack!
                        d = m.howtoattack(char)
                        sys.stdout.write('{} took {} damage from {}.\n'.format(char.name,d, m.name))
                        wait = True
                    elif level[p.x][p.y] in MOVEABLE and d1 < d0:
                        m.move(level, p)
                        break
        if wait:
            sys.stdout.flush()
            time.sleep(1)
