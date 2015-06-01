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
#[0-C0&C1, 1-C2, 2-P1, 3-C4, 4-C5&C6, 5-P2&P3, 6-C7&C8, 7-C9, 8-P4, 9-C10, 10-C11&C12, 11-C13, 12-C14, 13-C15&C16,
# 14-P5&P6, 15-C17, 16-P8&P9, 17-P10&P11, 18-P12&P13, 19-P14, 20-P15, 21-P16&P17, 22-C19, 23-C20
# 24-C21&C22, 25-C23&C24, 26-C25, 27-P18, 28-P19, 29-P20, 30-P21, 31-P22&P23]
catalog = [
[   
    weapon("Tree Branch","lol","Sword",1,100,0,None,None,100,"W",1,20,[None]),
    weapon("Glass Sword","Strong but breaks easily.","Sword",11,85,0,None,None,600,"W",1,3,[None]),
    weapon("Superior Edge","Strong against swords.","Sword",11,80,0,"Swordbreaker",None,1950,"W",1,10,[None]),
    weapon("Leif's Blade","A Lensteri gold-exploiting blade.","Sword",4,95,30,"Despoil",None,820,"W",1,20,[None]),
    weapon("Roy's Blade","A Lycian junior lord's blade.","Sword",8,95,5,None,None,900,"W",1,25,[None]),
    weapon("Eliwood's Blade","A Lycian senior lord's blade.","Sword",10,85,5,None,None,960,"W",1,20,[None]),
    weapon("Eirika's Blade","Magvel's Brave Sword!","Sword",6,95,10,"Brave",None,1220,"W",1,20,[None]),
    weapon("Seliph's Blade","A Calaphian junior lord's blade. Spd and Res +2.","Sword",12,90,15,None,None,1530,"W",1,15,[None]),
    weapon("Alm's Blade","A Zofian fighter's blade.","Sword",15,75,10,None,None,1630,"W",1,10,[None]),
    weapon("Log","lol","Lance",1,90,0,None,None,100,"W",1,20,[None]),
    weapon("Glass Lance","Strong but breaks easily.","Lance",13,75,0,None,None,600,"W",1,3,[None]),
    weapon("Miniature Lance","Ranged lance. Nice critical, but low accuracy.","Lance",1,55,35,None,None,650,"W",2,10,[None]),
    weapon("Shockstick","Uses magic instead of strength to attack.","Lance",11,85,10,None,None,1200,"M",2,20,[None]),
    weapon("Superior Lance","Strong against lances.","Lance",13,70,0,"Lancebreaker",None,2100,"W",1,10,[None]),
    weapon("Finn's Lance","A Lensteri knight's lance. Def and Lck +2.","Lance",8,85,10,None,None,950,"W",1,20,[None]),
    weapon("Ephraim's Lance","Magvel prince's greatlance! Str and Spd +2.","Lance",11,80,10,None,None,1220,"W",1,20,[None]),
    weapon("Sigurd's Lance","A Calaphian duke's lance.","Lance",14,85,15,None,None,1920,"W",1,15,[None]),
    weapon("Ladle","lol","Axe",1,80,0,None,None,100,"W",1,20,[None]),
    weapon("Glass Axe","Powerful but breaks easily.","Axe",15,65,0,None,None,600,"W",1,3,[None]),
    weapon("Imposing Axe","Powerful, but that accuracy...","Axe",14,35,10,None,None,830,"W",1,10,[None]),
    weapon("Superior Axe","Strong against axes.","Axe",15,60,0,"Axebreaker",None,2150,"W",1,10,[None]),
    weapon("Orsin's Hatchet","Orsin's ranged axe. WHY IS IT NERFED?","Axe",4,85,5,None,None,960,"W",2,20,[None]),
    weapon("Hector's Axe","Wolf Beil? Str and Def +2.","Axe",15,75,15,None,None,2010,"W",1,15,[None]),
    weapon("Slack Bow","lol","Bow",1,90,0,None,None,100,"W",2,20,[None]),
    weapon("Glass Bow","Powerful but breaks easily.","Bow",13,75,0,None,None,600,"W",2,3,[None]),
    weapon("Underdog Bow","Grants Underdog skill when equipped.","Bow",9,75,5,"Underdog",None,950,"W",2,15,[None]),
    weapon("Superior Bow","Strong against bows.","Bow",13,70,0,"Bowbreaker",None,2160,"W",2,10,[None]),
    weapon("Wolt's Bow","A faithful soldier's bow. Use this to recover 20HP.","Bow",10,85,5,None,None,950,"W",2,25,[None]),
    weapon("Innes' Bow","Innes' bow will rarely miss!","Bow",13,115,10,None,None,1710,"W",2,15,[None]),
    weapon("Dying Blaze","Powerful but breaks easily.","Magic",10,75,0,None,None,600,"M",2,3,[None]),
    weapon("Micaiah's Pyre","A Daein magician's tome. Def and Res +2.","Magic",13,85,5,None,None,2130,"M",2,15,[None]),
    weapon("Superior Jolt","Strong against magic.","Magic",14,60,15,"Tomebreaker",None,2320,"M",2,10,[None]),
    weapon("Katarina's Bolt","A tactician's tome. Good crit.","Magic",11,75,30,None,None,1920,"M",2,20,[None]),
    weapon("Wilderwind","Great crit but low durability.","Magic",2,70,35,None,None,760,"M",2,5,[None]),
    weapon("Aversa's Night","A stronger Nosferatu.","Dark Magic",15,75,0,"Drain",None,2340,"M",2,10,[None]),
    weapon("Celica's Gale","Zofia's Waste!","Magic",4,80,0,"Brave",None,1720,"M",2,20,[None])
],
 [
    weapon("Fire","Basic fire tome.","Magic",2,90,0,None,None,540,"M",2,45,[0,1,5,10]),
    weapon("Thunder","Basic thunder tome.","Magic",3,80,5,None,None,630,"M",2,45,[1,3,5,10]),    
    weapon("Wind","Basic wind tome.","Magic",1,100,0,None,None,450,"M",2,45,[1,4,5,10]),
    weapon("Flux","Basic dark tome.","Dark Magic",5,70,0,None,None,540,"M",2,45,[1,7,19]),    
    weapon("Bronze Sword","Novice sword.","Sword",3,100,0,None,None,350,"W",1,50,[0]),
    weapon("Rapier","Slender and regal.","Sword",5,90,10,None,None,1600,"W",1,35,[]),
    weapon("Bronze Lance","Novice lance.","Lance",3,90,0,None,None,350,"W",1,50,[0]),
    weapon("Bronze Axe","Novice Axe.","Axe",4,80,0,None,None,400,"W",1,50,[0]),
    weapon("Bronze Bow","Novice Bow.","Bow",3,90,0,None,None,350,"W",2,50,[0]),
    item("Vulnerary","Basic healing potion.",None,10,300,"H",3,[0,5])
],
[
    weapon("Elfire","Upgraded fire tome.","Magic",5,85,0,None,None,980,"M",2,35,[11,19]),
    weapon("Elthunder","Upgraded thunder tome.","Magic",6,75,5,None,None,1050,"M",2,35,[11,19]),
    weapon("Elwind","Upgraded wind tome.","Magic",4,95,0,None,None,910,"M",2,35,[11,19]),
    weapon("Nosferatu","Heal half of the given damage","Dark Magic",7,65,10,"Drain",None,980,"M",2,20,[11,19]),
    weapon("Iron Sword","Basic sword.","Sword",5,95,0,None,None,520,"W",1,40,[2,4,6,10,14]),    
    weapon("Iron Lance","Basic lance.","Lance",6,85,0,None,None,560,"W",1,40,[2,3,9,16]),    
    weapon("Iron Axe","Basic axe.","Axe",7,75,0,None,None,600,"W",1,40,[2,4,9,17]),
    weapon("Iron Bow","Basic bow.","Bow",6,85,0,None,None,560,"W",2,40,[2,3,6,10,20]),
    weapon("Javelin","Basic ranged lance.","Lance",2,80,0,None,None,700,"W",2,25,[5,6,9,12,16,24]),
    weapon("Hand Axe","Basic ranged axe.","Axe",3,70,0,None,None,750,"W",2,25,[5,6,9,13,17,24])
],
 [
    weapon("Arcfire","Uncommon fire tome.","Magic",8,80,0,None,None,1440,"M",2,30,[15,21,24]),
    weapon("Arcthunder","Uncommon thunder tome.","Magic",10,70,10,None,None,1620,"M",2,30,[21,24]),
    weapon("Arcwind","Uncommon wind tome.","Magic",6,90,0,None,None,1320,"M",2,30,[21,24]),   
    weapon("Ruin","High crit!","Dark Magic",4,65,50,None,None,1380,"M",2,20,[21,22]),
    weapon("Steel Sword","Good sword.","Sword",8,90,0,None,None,840,"W",1,30,[7,8,13,14]),
    weapon("Steel Lance","Good lance.","Lance",9,80,0,None,None,910,"W",1,35,[7,8,12,16]),
    weapon("Steel Axe","Good axe.","Axe",11,70,0,None,None,980,"W",1,35,[7,8,13,17]),
    weapon("Steel Bow","Good bow.","Bow",9,80,0,None,None,910,"W",2,35,[7,8,12,20]),
    weapon("Levin Sword","Thunder magic sword. Can attack from a distance.","Sword",10,80,0,None,None,1600,"M",2,25,[31]),
    weapon("Bolt Axe","Thunder magic axe. Can attack from a distance.","Axe",14,70,5,None,None,1920,"M",2,30,[]),
    weapon("Noble Rapier","Elegant but deadly.","Sword",8,85,10,None,None,2100,"W",1,25,[31]),
    weapon("Killing Edge","High crit!","Sword",9,90,30,None,None,1470,"W",1,30,[14,22]),
    weapon("Killer Lance","High crit!","Lance",10,80,30,None,None,1680,"W",1,30,[16,23]),    
    weapon("Killer Axe","High crit!","Axe",12,70,30,None,None,1860,"W",1,30,[17,23]),
    weapon("Killer Bow","High crit!","Bow",10,80,30,None,None,1680,"W",2,30,[20,22]),
    weapon("Longbow","Can attack from a range of 3.","Bow",9,70,0,None,None,2150,"W",3,25,[31]),
    weapon("Short Spear","Good ranged lance.","Lance",5,75,0,None,None,1600,"W",2,25,[31]),
    weapon("Short Axe","Good ranged axe.","Axe",7,65,0,None,None,1750,"W",2,25,[31]),
    item("Concoction","Good healing potion.",None,20,600,"H",3,[5,6,24])
],
 [
    weapon("Bolganone","Rare fire tome.","Magic",12,75,0,None,None,2000,"M",2,25,[25,30]),
    weapon("Thoron","Rare thunder tome.","Magic",14,65,10,None,None,2200,"M",2,25,[25,28]),
    weapon("Rexcalibur","Rare wind tome.","Magic",10,85,0,None,None,1900,"M",2,25,[25,29]),    
    weapon("Silver Sword","Somewhat rare sword.","Sword",9,80,0,None,None,1410,"W",1,30,[13,14,15,22,30]),
    weapon("Silver Lance","Somewhat rare lance.","Lance",13,75,0,None,None,1560,"W",1,30,[12,15,16,23,28]),
    weapon("Silver Axe","Somewhat rare axe.","Axe",15,65,0,None,None,1740,"W",1,30,[13,15,17,23,27]),
    weapon("Silver Bow","Somewhat rare bow.","Bow",13,75,0,None,None,1560,"W",2,30,[12,15,20,22,29]),
    weapon("Tomahawk","Somewhat rare ranged axe.","Axe",10,60,0,None,None,2550,"W",2,25,[]),
    weapon("Spear","Somewhat rare ranged lance.","Lance",8,70,0,None,None,2400,"W",2,25,[]),
    item("Elixir","Great healing potion.",None,99,900,"H",3,[14,25,31]),
    item("Master Seal","Use this to promote yourself. Level 10+ only.",10,None,10000,"C",1,[10,16,18]),
    item("Second Seal","Use this to reclass yourself. Level 10+ only.",10,None,10000,"C",1,[13,14,17,21])
],
 [
    weapon("Waste","Attack twice!","Dark Magic",10,45,0,"Brave",2160,None,"M",2,30,[25,29]),
    weapon("Brave Sword","Attack twice!","Sword",9,80,0,"Brave",None,2100,"W",1,30,[26,30]),
    weapon("Brave Lance","Attack twice!","Lance",10,70,0,"Brave",None,2220,"W",1,30,[26,28]),
    weapon("Brave Axe","Attack twice!","Axe",12,60,0,"Brave",None,2400,"W",1,30,[26,27]),
    weapon("Brave Bow","Attack twice!","Bow",10,70,0,"Brave",None,2220,"W",2,30,[26,29]),
    weapon("Sol","Chance to recover half HP.","Sword",12,85,5,"Sol",None,0,"W",1,30,[]),
    weapon("Luna","Chance to half opponent's defenses during damage calculation.","Lance",14,80,5,"Luna",None,0,"W",1,30,[]),
    weapon("Astra","Chance to attack opponent five times with half damage.","Bow",14,75,5,"Astra",None,0,"W",2,30,[])
],
 [
    weapon("Valflame","Fala's fire magic. Mgc +5.","Magic",16,80,10,None,None,0,"M",2,25,[None]),
    weapon("Mjolnir","Tordo's thunder magic. Skl +5.","Magic",18,70,20,None,None,0,"M",2,25,[None]),
    weapon("Forseti","Holsety's wind magic. Spd +5.","Magic",14,90,10,None,None,0,"M",2,25,[None]),
    weapon("Book of Naga","Naga's lost light magic. Def and Res +5.","Magic",15,80,15,None,None,0,"M",2,25,[None]),
    weapon("Goetia","Otherworldly grimoire, haunting death by the arcane darkness!","Dark Magic",19,75,10,None,None,0,"M",2,25,[None]),
    weapon("Sol Katti","A plainsman's blade. Res +5.","Sword",8,100,50,None,None,0,"W",1,25,[None]),
    weapon("Tyrfing","Baldur's divine sword. Res +5.","Sword",15,85,10,None,None,0,"W",1,25,[None]),
    weapon("Balmung","Odo's assassin blade. Spd +5.","Sword",13,90,10,None,None,0,"W",1,25,[None]),
    weapon("Mystletainn","Hezul's demon sword. Skl +5.","Sword",14,85,15,None,None,0,"W",1,25,[None]),
    weapon("Ragnell","Ike's ranged blade. Def +5.","Sword",15,70,0,None,None,0,"W",2,25,[None]),
    weapon("Mercurius","Archanea's sword. Powerful.","Sword",17,95,5,None,None,0,"W",1,25,[None]),
    weapon("Gradivus","Archanea's javelin. Use this to recover all HP.","Lance",19,85,5,None,None,0,"W",2,25,[None]),
    weapon("Gungnir","Dain's draconic lance. Str +5.","Lance",16,70,10,None,None,0,"W",1,25,[None]),
    weapon("Hauteclere","Minerva's axe. Use this to recover all HP.","Axe",21,70,5,None,None,0,"W",1,25,[None]),
    weapon("Helswath","Neir's treasured ranged axe. Def +5.","Axe",18,60,10,None,None,0,"W",2,25,[None]),
    weapon("Armads","Hector's thunder axe. Def +5.","Axe",17,80,10,None,None,0,"W",1,25,[None]),
    weapon("Parthia","Archanea's bow. Res +5.","Bow",19,95,5,None,None,0,"W",2,25,[None]),
    weapon("Nidhogg","Frelia's serpent bow. Lck +10.","Bow",16,75,10,None,None,0,"W",2,25,[None]),
    weapon("Double Bow","Powerful longbow of unknown origin. Str +5.","Bow",13,70,10,None,None,0,"W",3,25,[None])
]
 
]
