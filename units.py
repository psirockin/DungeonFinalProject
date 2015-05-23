# These are for player only, all only base growths

import collections

unit = collections.namedtuple('unit', 'name ability base classes')

data = [
[
unit("Tactician", ["Sword", "Magic"], [40, 15, 15, 15, 15, 0, 10, 10],["Grandmaster"]),
unit("Cavalier", ["Sword", "Lance"], [45, 20, 0, 20, 20, 0, 10, 5],["Great Knight","Paladin"]),
unit("Mercenary", ["Sword"], [45, 20, 0, 25, 20, 0, 10, 5],["Hero","Bow Knight"]),
unit("Myrmidon", ["Sword"], [40,20,0,25,25,0,5,5],["Swordmaster","Assassin"]),
unit("Archer",["Bow"],[45,15,0,30,15,0,10,5],["Sniper","Bow Knight"]),
unit("Thief",["Sword"],[35,15,5,25,25,0,5,5],["Assassin","Trickster"])
]
,
[
unit("Grandmaster", ["Sword", "Magic"], [40, 15, 15, 15, 15, 0, 10, 10],None),
unit("Paladin", ["Sword", "Lance"], [45, 20, 0, 20, 20, 10, 10],None),
unit("Hero", ["Sword", "Axe"], [45, 20, 0, 25, 20, 0, 10, 5],None),
unit("Swordmaster",["Sword"],[40,20,0,25,25,0,5,10],None),
unit("Sniper",["Bow"],[45,15,0,30,15,0,15,5],None),
unit("Bow Knight",["Bow","Sword"],[50,20,0,25,20,0,5,5],None),
unit("Assassin",["Sword","Bow"],[40,20,0,30,25,0,5,5],None),
unit("Trickster",["Sword","Staff"],[35,10,15,25,20,0,5,10],None) #Note: Do I want to put staff in here?
]
]
