# These are for player only, all only base growths

import collections

unit = collections.namedtuple('unit', 'name weapons base classes basestats')
#The final parameter is used to calculate promo/reclass bonuses.
#HP, strength, magic, skill, speed, luck, defense, resist
data = [
[
unit("Tactician", ["Sword", "Magic"], [40, 15, 15, 15, 15, 0, 10, 10],["Grandmaster"],[16,4,3,5,5,0,5,3]),
unit("Cavalier", ["Sword", "Lance"], [45, 20, 0, 20, 20, 0, 10, 5],["Great Knight","Paladin"],[18,6,0,5,6,7,0]),
unit("Mercenary", ["Sword"], [45, 20, 0, 25, 20, 0, 10, 5],["Hero","Bow Knight"],[18,5,0,8,7,0,5,0]),
unit("Myrmidon", ["Sword"], [40,20,0,25,25,0,5,5],["Swordmaster","Assassin"],[16,4,1,9,10,0,4,1]),
unit("Archer",["Bow"],[45,15,0,30,15,0,10,5],["Sniper","Bow Knight"],[16,5,0,8,6,0,5,0]),
unit("Thief",["Sword"],[35,15,5,25,25,0,5,5],["Assassin","Trickster"],[16,3,0,6,8,0,2,0])
]
,
[
unit("Grandmaster", ["Sword", "Magic"], [40, 15, 15, 15, 15, 0, 10, 10],None,[20,7,6,7,7,0,7,5]),
unit("Paladin", ["Sword", "Lance"], [45, 20, 0, 20, 20, 10, 10],None,[25,9,1,7,8,0,10,6]),
unit("Great Knight",["Sword","Lance","Axe"],[50,25,0,15,15,0,15,5],None,[26,11,0,6,5,0,14,1]),
unit("Hero", ["Sword", "Axe"], [45, 20, 0, 25, 20, 0, 10, 5],None,[22,8,1,11,10,0,8,3]),
unit("Swordmaster",["Sword"],[40,20,0,25,25,0,5,10],None,[20,7,2,11,13,0,6,4]),
unit("Sniper",["Bow"],[45,15,0,30,15,0,15,5],None,[20,7,1,12,9,0,10,3]),
unit("Bow Knight",["Bow","Sword"],[50,20,0,25,20,0,5,5],None,[24,8,0,10,10,0,6,2]),
unit("Assassin",["Sword","Bow"],[40,20,0,30,25,0,5,5],None,[21,8,0,13,12,0,5,1]),
unit("Trickster",["Sword","Staff"],[35,10,15,25,20,0,5,10],None,[19,4,4,10,11,0,3,5]) #Note: Do I want to put staff in here?
]
]
