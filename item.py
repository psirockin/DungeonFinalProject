import collections
 
weapon = collections.namedtuple('weapon', 'name desc attack accuracy critical effect cost type range')
item = collections.namedtuple('item','name desc effect cost type')
 
class itemwrapper:
    def __init__(self, obj, level, x, y):
        self.obj = obj
        self.level = level
        self.x = x
        self.y = y
 
catalog = [
 [
    weapon("Fire","Basic fire tome",2,90,0,None,540,"M",2),
    weapon("Thunder","Basic thunder tome",3,80,5,None,630,"M",2),    
    weapon("Wind","Basic wind tome",1,100,0,None,450,"M",2),
    weapon("Flux","Basic dark tome",5,70,0,None,540,"M",2),
    weapon("Bronze Sword","Novice sword",3,100,0,None,350,"W",1),
    weapon("Rapier","Slender and regal.",5,90,10,None,1600,"W",1),
    weapon("Tree Branch","lol",1,100,0,None,100,"W",1),
    item("Vulnerary","Basic healing potion",10,300,"H")
],
[
    weapon("Elfire","Upgraded fire tome",5,85,0,None,980,"M",2),
    weapon("Elthunder","Upgraded thunder tome",6,75,5,None,1050,"M",2),
    weapon("Elwind","Upgraded wind tome",4,95,0,None,910,"M",2),
    weapon("Nosferatu","Heal half of the given damage",7,65,10,None,980,"M",2),
    weapon("Iron Sword","Basic sword",5,95,0,None,520,"W",1),
    weapon("Roy's Blade","A junior lord's blade.",8,95,5,None,900,"W",1)
],
 [
    weapon("Arcfire","Rare fire tome",8,80,0,None,1440,"M",2),
    weapon("Arcthunder","Rare thunder tome",10,70,10,None,1620,"M",2),
    weapon("Arcwind","Rare wind tome",6,90,0,None,1320,"M",2),
    weapon("Ruin","High crit!",4,65,50,None,1380,"M",2),
    weapon("Steel Sword","Good sword",8,90,0,None,840,"W",1),
    weapon("Noble Rapier","Elegant but deadly.",8,85,10,None,2100,"W",1),
    weapon("Killing Edge","High crit!",9,90,30,None,1470,"W",1),
    weapon("Eirika's Blade","Attack twice!",6,95,10,None,1220,"W",1),
    item("Concoction","Good healing potion",20,600,"H")
],
 [
    weapon("Bolganone","Advanced fire tome",12,75,0,None,2000,"M",2),
    weapon("Thoron","Advanced thunder tome",14,65,10,None,2200,"M",2),
    weapon("Rexcalibur","Advanced wind tome",10,85,0,None,1900,"M",2),
    weapon("Waste","Attack twice!",10,45,0,None,2160,"M",2),
    weapon("Brave Sword","Attack twice!",10,45,0,None,2160,"W",1),
    weapon("Silver Sword","Attack twice!",9,80,0,None,2100,"W",1),
    item("Elixir","Great healing potion",99,900,"H")
],
[
    weapon("Valflame","Call upon Agni's fire!",16,80,10,None,0,"M",2),
    weapon("Mjolnir","Fear the strike of Thor!",18,70,20,None,0,"M",2),
    weapon("Forseti","Settle your justice by the wind!",14,90,10,None,0,"M",2),
    weapon("Goetia","Somewhat forbidden sorcery; powerful!",19,75,10,None,0,"M",2),
    weapon("Sol Katti","A plainsman's blade.",8,100,50,None,0,"W",1),
    weapon("Sol","Chance to recover half HP.",12,85,5,None,0,"W",1),
    weapon("Mercurius","SO MUCH POWER.",17,95,5,None,0,"W",1)
]
 
]
