# These are for player only, all only base growths

import collections

unit = collections.namedtuple('unit', 'name weakness weapons base classes basestats maximum')
#The final parameter is used to calculate promo/reclass bonuses.
#HP, strength, magic, skill, speed, luck, defense, resist
data = [
[
unit("Tactician",[None],["Sword", "Magic"],[40,15,15,15,15,0,10,10],["Grandmaster"],[16,4,3,5,5,0,5,3],[60,25,25,25,25,30,25,25]),
unit("Cavalier",["Horse"],["Sword", "Lance"],[45,20,0,20,20,0,10,5],["Great Knight","Paladin"],[18,6,0,5,6,0,7,0],[60,26,20,25,25,30,26,26]),
unit("Mercenary",[None],["Sword"], [45,20,0,25,20,0,10,5],["Hero","Bow Knight"],[18,5,0,8,7,0,5,0],[60,26,20,28,26,30,25,23]),
unit("Myrmidon",[None],["Sword"], [40,20,0,25,25,0,5,5],["Swordmaster","Assassin"],[16,4,1,9,10,0,4,1],[60,24,22,27,28,30,22,24]),
unit("Archer",[None],["Bow"],[45,15,0,30,15,0,10,5],["Sniper","Bow Knight"],[16,5,0,8,6,0,5,0],[60,26,20,29,25,30,25,21]),
unit("Thief",[None],["Sword"],[35,15,5,25,25,0,5,5],["Assassin","Trickster"],[16,3,0,6,8,0,2,0],[60,22,20,30,28,30,21,20]),
unit("Mage",[None],["Magic"],[35,0,20,20,20,0,5,10],["Sage","Dark Knight"],[16,0,4,3,4,0,2,3],[60,20,28,27,26,30,21,25]),
unit("Wyvern Rider",["Dragon","Wing"],["Axe"],[45,30,0,15,15,0,10,5],["Wyvern Lord","Griffon Rider"],[19,7,0,6,5,0,8,0],[60,28,20,24,24,30,28,20]),
unit("Knight",["Armor"],["Lance"],[50,25,0,15,10,0,15,5],["General","Great Knight"],[18,8,0,4,2,0,11,0],[60,30,20,26,23,30,0,30,22]),
unit("Dark Mage",[None],["Magic","Dark Magic"],[50,5,15,15,15,0,10,10],["Sorcerer","Dark Knight"],[18,1,3,2,3,0,4,4],[60,20,27,25,25,30,25,27]),
unit("Fighter",[None],["Axe"],[45,25,0,20,15,0,10,5],["Hero","Warrior"],[20,8,0,5,5,0,4,0],[60,29,20,26,25,30,25,23])
]
,
[
unit("Grandmaster",[None],["Sword","Magic"], [40,15,15,15,15,0,10,10],None,[20,7,6,7,7,0,7,5],[80,40,40,40,40,45,40,40]),
unit("Paladin",["Horse"],["Sword","Lance"], [45,20,0,20,20,0,10,10],None,[25,9,1,7,8,0,10,6],[80,42,30,40,40,45,42,42]),
unit("Great Knight",["Horse","Armor"],["Sword","Lance","Axe"],[50,25,0,15,15,0,15,5],None,[26,11,0,6,5,0,14,1],[80,48,20,34,37,45,48,30]),
unit("Hero",[None],["Sword","Axe"], [45, 20, 0, 25, 20, 0, 10, 5],None,[22,8,1,11,10,0,8,3],[80,50,30,41,35,45,50,35]),
unit("Swordmaster",[None],["Sword"],[40,20,0,25,25,0,5,10],None,[20,7,2,11,13,0,6,4],[80,38,34,44,46,45,33,38]),
unit("Sniper",[None],["Bow"],[45,15,0,30,15,0,15,5],None,[20,7,1,12,9,0,10,3],[80,42,30,46,42,45,40,36]),
unit("Bow Knight",["Horse"],["Bow","Sword"],[50,20,0,25,20,0,5,5],None,[24,8,0,10,10,0,6,2],[80,40,30,43,41,45,35,30]),
unit("Assassin",[None],["Sword","Bow"],[40,20,0,30,25,0,5,5],None,[21,8,0,13,12,0,5,1],[80,40,30,48,46,45,31,30]),
unit("Trickster",[None],["Sword","Staff"],[35,10,15,25,20,0,5,10],None,[19,4,4,10,11,0,3,5],[80,35,38,45,43,45,30,40]), 
#Note: Do I want to put staff in here?
unit("Sage",[None],["Magic","Staff"],[35,0,20,20,20,0,5,10],None,[20,1,7,5,7,0,4,5],[80,30,46,43,42,45,31,40]),
unit("Dark Knight",[None],["Magic","Sword"],[50,15,15,15,15,0,10,5],None,[25,4,5,6,5,0,9,5],[80,38,41,40,40,45,42,38]),
unit("Sorcerer",[None],["Magic","Dark Magic"],[45,0,20,15,15,0,10,10],None,[23,2,6,4,4,0,7,7],[80,30,44,38,40,45,41,44]),
unit("Wyvern Lord",["Dragon","Wing"],["Axe","Lance"],[45,30,0,15,15,0,10,5],None,[24,11,0,8,7,0,11,3],[80,46,30,38,38,45,46,30]),
unit("Griffon Rider",["Wing","Horse"],["Axe"],[45,25,0,20,20,0,5,5],None,[22,9,0,10,9,0,8,3],[80,40,30,43,41,45,40,30]),
unit("General",["Armor"],["Lance","Axe"],[50,25,0,15,10,0,15,10],None,[28,12,0,7,4,0,15,3],[80,50,30,41,35,45,50,35])
]
]

def setclass(theclass):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if theclass == data[i][j].name:
                return data[i][j]

def ispromote(theclass):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if theclass == data[i][j].name:
                return i

def getbase(theclass):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if theclass == data[i][j].name:
                return data[i][j].basestats

def getmax(theclass):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if theclass == data[i][j].name:
                return data[i][j].maximum

#Debug tool
def paramcheck():
    bug = False
    for i in range(len(data)):
        for j in range(len(data)):
            if len((data[i][j]).base) != 8 or len((data[i][j]).basestats) != 8 or len((data[i][j]).maximum) != 8:
                print("Something is not right with {}.".format(data[i][j].name))
                bug = True
    if not bug:
        print("Test passed.")
