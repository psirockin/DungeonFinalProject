import collections
 
weapon = collections.namedtuple('weapon', 'name desc school attack accuracy critical effect boost cost type range dur shop')
item = collections.namedtuple('item','name desc req effect cost type dur shop')
 
class itemwrapper:
    def __init__(self, obj, level, x, y):
        self.obj = obj
        self.level = level
        self.name = self.obj.name #To make forging a thing
        self.x = x
        self.y = y
        self.dur = obj.dur
        if self.obj.type == "W" or self.obj.type == "M":
            self.isweapon = True
            self.attack = self.obj.attack
            self.accuracy = self.obj.accuracy
            self.critical = self.obj.critical
            self.forgestats = [0,0,0] #Attack, accuracy and crit. These values will never exceed 5.

catalog = [
 [
    weapon("Fire","Basic fire tome.","Magic",2,90,0,None,None,540,"M",2,45,True),
    weapon("Thunder","Basic thunder tome.","Magic",3,80,5,None,None,630,"M",2,45,True),    
    weapon("Wind","Basic wind tome.","Magic",1,100,0,None,None,450,"M",2,45,True),
    weapon("Flux","Basic dark tome.","Dark Magic",5,70,0,None,None,540,"M",2,45,True),
    weapon("Dying Blaze","Strong but breaks easily.","Magic",10,75,0,None,None,600,"M",2,3,False),
    weapon("Bronze Sword","Novice sword.","Sword",3,100,0,None,None,350,"W",1,50,True),
    weapon("Rapier","Slender and regal.","Sword",5,90,10,None,None,1600,"W",1,35,False),
    weapon("Tree Branch","lol","Sword",1,100,0,None,None,100,"W",1,20,False),
    weapon("Glass Sword","Strong but breaks easily.","Sword",11,85,0,None,None,600,"W",1,3,False),
    weapon("Bronze Lance","Novice lance.","Lance",3,90,0,None,None,350,"W",1,50,True),
    weapon("Log","lol","Lance",1,90,0,None,None,100,"W",1,20,False),
    weapon("Glass Lance","Strong but breaks easily.","Lance",13,75,0,None,None,600,"W",1,3,False),    
    item("Vulnerary","Basic healing potion.",None,10,300,"H",3,True)
],
[
    weapon("Elfire","Upgraded fire tome.","Magic",5,85,0,None,None,980,"M",2,35,True),
    weapon("Elthunder","Upgraded thunder tome.","Magic",6,75,5,None,None,1050,"M",2,35,True),
    weapon("Elwind","Upgraded wind tome.","Magic",4,95,0,None,None,910,"M",2,35,True),
    weapon("Nosferatu","Heal half of the given damage","Dark Magic",7,65,10,"Drain",None,980,"M",2,20,True),
    weapon("Iron Sword","Basic sword.","Sword",5,95,0,None,None,520,"W",1,40,True),
    weapon("Roy's Blade","A junior lord's blade.","Sword",8,95,5,None,None,900,"W",1,25,False),
    weapon("Iron Lance","Basic lance.","Lance",6,85,0,None,None,560,"W",1,40,True),
    weapon("Javelin","Basic ranged lance.","Lance",2,80,0,None,None,700,"W",2,25,True)
],
 [
    weapon("Arcfire","Uncommon fire tome.","Magic",8,80,0,None,None,1440,"M",2,30,True),
    weapon("Arcthunder","Uncommon thunder tome.","Magic",10,70,10,None,None,1620,"M",2,30,True),
    weapon("Arcwind","Uncommon wind tome.","Magic",6,90,0,None,None,1320,"M",2,30,True),
    weapon("Celica's Gale","Attack twice!","Magic",4,80,0,"Brave",None,1720,"M",2,20,False),
    weapon("Ruin","High crit!","Dark Magic",4,65,50,None,None,1380,"M",2,20,True),
    weapon("Steel Sword","Good sword.","Sword",8,90,0,None,None,840,"W",1,30,True),
    weapon("Noble Rapier","Elegant but deadly.","Sword",8,85,10,None,None,2100,"W",1,25,False),
    weapon("Killing Edge","High crit!","Sword",9,90,30,None,None,1470,"W",1,30,True),
    weapon("Eirika's Blade","Attack twice!","Sword",6,95,10,"Brave",None,1220,"W",1,20,False),
    weapon("Levin Sword","Thunder magic sword. Can attack from a distance.","Sword",10,80,0,None,None,1600,"M",2,25,True),
    weapon("Steel Lance","Good lance.","Lance",9,80,0,None,None,910,"W",1,35,True),
    weapon("Short Spear","Good ranged lance.","Lance",5,75,0,None,None,1600,"W",2,25,True),
    weapon("Killer Lance","High crit!","Lance",10,80,30,None,None,1680,"W",1,30,True),
    item("Concoction","Good healing potion.",None,20,600,"H",3,True)
],
 [
    weapon("Bolganone","Rare fire tome.","Magic",12,75,0,None,None,2000,"M",2,25,True),
    weapon("Thoron","Rare thunder tome.","Magic",14,65,10,None,None,2200,"M",2,25,True),
    weapon("Rexcalibur","Rare wind tome.","Magic",10,85,0,None,None,1900,"M",2,25,True),    
    weapon("Silver Sword","Somewhat rare sword.","Sword",9,80,0,None,None,1410,"W",1,30,True),
    weapon("Silver Lance","Somewhat rare lance.","Lance",13,75,0,None,None,1560,"W",1,30,True),
    weapon("Spear","Somewhat rare ranged lance.","Lance",8,70,0,None,None,2400,"W",2,25,True),
    item("Elixir","Great healing potion.",None,99,900,"H",3,True),
    item("Master Seal","Use this to promote yourself. Level 10+ only.",10,None,10000,"C",1,True),
    item("Second Seal","Use this to reclass yourself. Level 10+ only.",10,None,10000,"C",1,True)
],
 [
    weapon("Waste","Attack twice!","Dark Magic",10,45,0,"Brave",2160,None,"M",2,30,True),
    weapon("Brave Sword","Attack twice!","Sword",9,80,0,"Brave",None,2100,"W",1,30,True),
    weapon("Brave Lance","Attack twice!","Lance",10,70,0,"Brave",None,2220,"W",1,30,True),
    weapon("Sol","Chance to recover half HP.","Sword",12,85,5,"Sol",None,0,"W",1,30,False),
    weapon("Luna","Chance to half opponent's defenses during damage calculation.","Lance",14,80,5,"Luna",None,0,"W",1,30,False),
    weapon("Astra","Chance to attack opponent five times with half damage.","Bow",14,75,5,"Astra",None,0,"W",2,30,False)
],
 [
    weapon("Valflame","Powerful Fala magic, agonizing death by fire!","Magic",16,80,10,None,None,0,"M",2,25,False),
    weapon("Mjolnir","Flashy Tordo magic, electrifying death by thunder!","Magic",18,70,20,None,None,0,"M",2,25,False),
    weapon("Forseti","Holsety magic, swift death by the winds.","Magic",14,90,10,None,None,0,"M",2,25,False),
    weapon("Goetia","Otherworldly grimoire, haunting death by the arcane darkness!","Dark Magic",19,75,10,None,None,0,"M",2,25,False),
    weapon("Sol Katti","A plainsman's blade.","Sword",8,100,50,None,None,0,"W",1,25,False),    
    weapon("Mercurius","SO. MUCH. POWER.","Sword",17,95,5,None,None,0,"W",1,25,False),
    weapon("Gradivus","Powerful Javelin. Upon using it, you recover all HP.","Lance",19,85,5,None,None,0,"W",2,25,False),
    weapon("Gungnir","Legendary Dain lance. Command the draconic power!","Lance",16,70,10,None,None,0,"W",1,25,False)
]
 
]
