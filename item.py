import collections
 
weapon = collections.namedtuple('weapon', 'name desc subclass attack accuracy critical effect boost cost type range dur')
item = collections.namedtuple('item','name desc req effect cost type dur')
 
class itemwrapper:
    def __init__(self, obj, level, x, y):
        self.obj = obj
        self.level = level
        self.x = x
        self.y = y
        self.dur = obj.dur
 
catalog = [
 [
    weapon("Fire","Basic fire tome","Magic",2,90,0,None,None,540,"M",2,45),
    weapon("Thunder","Basic thunder tome","Magic",3,80,5,None,None,630,"M",2,45),    
    weapon("Wind","Basic wind tome","Magic",1,100,0,None,None,450,"M",2,45),
    weapon("Flux","Basic dark tome","Magic",5,70,0,None,None,540,"M",2,45),
    weapon("Bronze Sword","Novice sword","Sword",3,100,0,None,None,350,"W",1,50),
    weapon("Rapier","Slender and regal.","Sword",5,90,10,None,None,1600,"W",1,35),
    weapon("Tree Branch","lol","Sword",1,100,0,None,None,100,"W",1,20),
    weapon("Dying Blaze","Strong but breaks easily.","Magic",10,75,0,None,None,600,"M",2,3),
    item("Vulnerary","Basic healing potion",None,10,300,"H",3)
],
[
    weapon("Elfire","Upgraded fire tome","Magic",5,85,0,None,None,980,"M",2,35),
    weapon("Elthunder","Upgraded thunder tome","Magic",6,75,5,None,None,1050,"M",2,35),
    weapon("Elwind","Upgraded wind tome","Magic",4,95,0,None,None,910,"M",2,35),
    weapon("Nosferatu","Heal half of the given damage","Magic",7,65,10,"Drain",None,980,"M",2,20),
    weapon("Iron Sword","Basic sword","Sword",5,95,0,None,None,520,"W",1,40),
    weapon("Roy's Blade","A junior lord's blade.","Sword",8,95,5,None,None,900,"W",1,25)
],
 [
    weapon("Arcfire","Rare fire tome","Magic",8,80,0,None,None,1440,"M",2,30),
    weapon("Arcthunder","Rare thunder tome","Magic",10,70,10,None,None,1620,"M",2,30),
    weapon("Arcwind","Rare wind tome","Magic",6,90,0,None,None,1320,"M",2,30),
    weapon("Celica's Gale","Attack twice!","Magic",4,80,0,"Brave",None,1720,"M",2,20),
    weapon("Ruin","High crit!","Magic",4,65,50,None,None,1380,"M",2,20),
    weapon("Steel Sword","Good sword","Sword",8,90,0,None,None,840,"W",1,30),
    weapon("Noble Rapier","Elegant but deadly.","Sword",8,85,10,None,None,2100,"W",1,25),
    weapon("Killing Edge","High crit!","Sword",9,90,30,None,None,1470,"W",1,30),
    weapon("Eirika's Blade","Attack twice!","Sword",6,95,10,"Brave",None,1220,"W",1,20),
    item("Concoction","Good healing potion",None,20,600,"H",3)
],
 [
    weapon("Bolganone","Advanced fire tome","Magic",12,75,0,None,None,2000,"M",2,25),
    weapon("Thoron","Advanced thunder tome","Magic",14,65,10,None,None,2200,"M",2,25),
    weapon("Rexcalibur","Advanced wind tome","Magic",10,85,0,None,None,1900,"M",2,25),
    weapon("Waste","Attack twice!","Magic",10,45,0,"Brave",2160,None,"M",2,30),
    weapon("Brave Sword","Attack twice!","Sword",10,45,0,"Brave",None,2160,"W",1,30),
    weapon("Silver Sword","Somewhat rare sword","Sword",9,80,0,None,None,2100,"W",1,30),
    item("Elixir","Great healing potion",None,99,900,"H",3),
    item("Master Seal","Use this to promote yourself. Level 10+ only.",10,None,10000,"C",1),
    item("Second Seal","Use this to reclass yourself. Level 10+ only.",10,None,10000,"C",1)
],
[
    weapon("Valflame","Powerful Fala magic, agonizing death by fire!","Magic",16,80,10,None,None,0,"M",2,25),
    weapon("Mjolnir","Flashy Tordo magic, electrifying death by thunder!","Magic",18,70,20,None,None,0,"M",2,25),
    weapon("Forseti","Holsety magic, swift death by the winds.","Magic",14,90,10,None,None,0,"M",2,25),
    weapon("Goetia","Otherworldly grimoire, haunting death by the arcane darkness!","Magic",19,75,10,None,None,0,"M",2,25),
    weapon("Sol Katti","A plainsman's blade.","Sword",8,100,50,None,None,0,"W",1,25),
    weapon("Sol","Chance to recover half HP.","Sword",12,85,5,"Sol",None,0,"W",1,30),
    weapon("Luna","Chance to half opponent's defenses during damage calculation.","Lance",14,80,5,"Luna",None,0,"W",1,30),
    weapon("Mercurius","SO. MUCH. POWER.","Sword",17,95,5,None,None,0,"W",1,25)
]
 
]
