import collections
 
weapon = collections.namedtuple('weapon', 'name desc school attack accuracy critical effect boost weakness cost type range dur shop hidden')
item = collections.namedtuple('item','name desc req effect cost type dur shop hidden')
 
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
    weapon("Tree Branch","lol","Sword",1,100,0,None,None,[None],100,"W",1,20,[None],[None]),
    weapon("Glass Sword","Strong but breaks easily.","Sword",11,85,0,None,None,[None],600,"W",1,3,[None],[None]),
    weapon("Superior Edge","Strong against swords.","Sword",11,80,0,"Swordbreaker",None,[None],1950,"W",1,10,[None],[None]),
    weapon("Leif's Blade","A Lensteri gold-exploiting blade.","Sword",4,95,30,"Despoil",None,[None],820,"W",1,20,[None],[None]),
    weapon("Roy's Blade","A Lycian junior lord's blade.","Sword",8,95,5,None,None,[None],900,"W",1,25,[None],[None]),
    weapon("Eliwood's Blade","A Lycian senior lord's blade.","Sword",10,85,5,None,None,[None],960,"W",1,20,[None],[None]),
    weapon("Eirika's Blade","Magvel's Brave Sword!","Sword",6,95,10,"Brave",None,[None],1220,"W",1,20,[None],[None]),
    weapon("Seliph's Blade","A Calaphian junior lord's blade. Spd and Res +2.","Sword",12,90,15,None,None,[None],1530,"W",1,15,[None],[None]),
    weapon("Alm's Blade","A Zofian fighter's blade.","Sword",15,75,10,None,None,[None],1630,"W",1,10,[None],[None]),
    weapon("Log","lol","Lance",1,90,0,None,None,[None],100,"W",1,20,[None],[None]),
    weapon("Glass Lance","Strong but breaks easily.","Lance",13,75,0,None,None,[None],600,"W",1,3,[None],[None]),
    weapon("Miniature Lance","Ranged lance. Nice critical, but low accuracy.","Lance",1,55,35,None,None,[None],650,"W",2,10,[None],[None]),
    weapon("Shockstick","Uses magic instead of strength to attack.","Lance",11,85,10,None,None,[None],1200,"M",2,20,[None],[None]),
    weapon("Superior Lance","Strong against lances.","Lance",13,70,0,"Lancebreaker",None,[None],2100,"W",1,10,[None],[None]),
    weapon("Finn's Lance","A Lensteri knight's lance. Def and Lck +2.","Lance",8,85,10,None,None,[None],950,"W",1,20,[None],[None]),
    weapon("Ephraim's Lance","Magvel prince's greatlance! Str and Spd +2.","Lance",11,80,10,None,None,[None],1220,"W",1,20,[None],[None]),
    weapon("Sigurd's Lance","A Calaphian duke's lance.","Lance",14,85,15,None,None,[None],1920,"W",1,15,[None],[None]),
    weapon("Ladle","lol","Axe",1,80,0,None,None,[None],100,"W",1,20,[None],[None]),
    weapon("Glass Axe","Powerful but breaks easily.","Axe",15,65,0,None,None,[None],600,"W",1,3,[None],[None]),
    weapon("Imposing Axe","Powerful, but that accuracy...","Axe",14,35,10,None,None,[None],830,"W",1,10,[None],[None]),
    weapon("Superior Axe","Strong against axes.","Axe",15,60,0,"Axebreaker",None,[None],2150,"W",1,10,[None],[None]),
    weapon("Orsin's Hatchet","Orsin's ranged axe. WHY IS IT NERFED?","Axe",4,85,5,None,[None],None,960,"W",2,20,[None],[None]),
    weapon("Hector's Axe","Wolf Beil? Str and Def +2.","Axe",15,75,15,None,None,[None],2010,"W",1,15,[None],[None]),
    weapon("Volant Axe","Ranged axe. Strong against wings.","Axe",8,55,0,None,None,["Wing"],1510,"W",2,10,[None],[None]),
    weapon("Slack Bow","lol","Bow",1,90,0,None,None,["Wing"],100,"W",2,20,[None],[None]),
    weapon("Glass Bow","Powerful but breaks easily.","Bow",13,75,0,None,None,["Wing"],600,"W",2,3,[None],[None]),
    weapon("Underdog Bow","Grants Underdog skill when equipped.","Bow",9,75,5,"Underdog",None,["Wing"],950,"W",2,15,[None],[None]),
    weapon("Superior Bow","Strong against bows.","Bow",13,70,0,"Bowbreaker",None,["Wing"],2160,"W",2,10,[None],[None]),
    weapon("Wolt's Bow","A faithful soldier's bow. Use this to recover 20HP.","Bow",10,85,5,None,None,["Wing"],950,"W",2,25,[None],[None]),
    weapon("Innes' Bow","Innes' bow will rarely miss!","Bow",13,115,10,None,None,["Wing"],1710,"W",2,15,[None],[None]),
    weapon("Dying Blaze","Powerful but breaks easily.","Magic",10,75,0,None,None,[None],600,"M",2,3,[None],[None]),
    weapon("Micaiah's Pyre","A Daein magician's tome. Def and Res +2.","Magic",13,85,5,None,None,[None],2130,"M",2,15,[None],[None]),
    weapon("Superior Jolt","Strong against magic.","Magic",14,60,15,"Tomebreaker",None,[None],2320,"M",2,10,[None],[None]),
    weapon("Katarina's Bolt","A tactician's tome. Good crit.","Magic",11,75,30,None,None,[None],1920,"M",2,20,[None],[None]),
    weapon("Wilderwind","Great crit but low durability.","Magic",2,70,35,None,None,["Wing"],760,"M",2,5,[None],[None]),
    weapon("Aversa's Night","A stronger Nosferatu.","Dark Magic",15,75,0,"Drain",None,[None],2340,"M",2,10,[None],[None]),
    weapon("Celica's Gale","Zofia's Waste!","Magic",4,80,0,"Brave",None,["Wing"],1720,"M",2,20,[None],[None]),
    item("Seraph Robe","Max HP +5.",0,5,2500,"B",1,[None],[255]), #HP, Str, Mag, Skl, Spd, Lck, Def, Res
    item("Energy Drop","Str +2.",1,2,2500,"B",1,[None],[255]), 
    item("Spirit Dust","Mag +2.",2,2,2500,"B",1,[None],[255]),
    item("Secret Book","Skl +2.",3,2,2500,"B",1,[None],[255]),
    item("Speedwing","Spd +2.",4,2,2500,"B",1,[None],[255]),
    item("Goddess Icon","Lck +2.",5,2,2500,"B",1,[None],[255]),
    item("Dracoshield","Def +2.",6,2,2500,"B",1,[None],[255]),
    item("Talisman","Res +2.",7,2,2500,"B",1,[None],[255])
],
 [
    weapon("Fire","Basic fire tome.","Magic",2,90,0,None,None,[None],540,"M",2,45,[0,1,5,10],[None]),
    weapon("Thunder","Basic thunder tome.","Magic",3,80,5,None,None,[None],630,"M",2,45,[1,3,5,10],[None]),    
    weapon("Wind","Basic wind tome.","Magic",1,100,0,None,None,["Wing"],450,"M",2,45,[1,4,5,10],[None]),
    weapon("Flux","Basic dark tome.","Dark Magic",5,70,0,None,None,[None],540,"M",2,45,[1,7,19],[None]),    
    weapon("Bronze Sword","Novice sword.","Sword",3,100,0,None,None,[None],350,"W",1,50,[0],[None]),
    weapon("Rapier","Slender and regal.","Sword",5,90,10,None,None,["Horse","Armor"],1600,"W",1,35,[13],[4,10,12]),
    weapon("Bronze Lance","Novice lance.","Lance",3,90,0,None,None,[None],350,"W",1,50,[0],[None]),
    weapon("Bronze Axe","Novice Axe.","Axe",4,80,0,None,None,[None],400,"W",1,50,[0],[None]),
    weapon("Bronze Bow","Novice Bow.","Bow",3,90,0,None,None,["Wing"],350,"W",2,50,[0],[None]),
    item("Vulnerary","Basic healing potion.",None,10,300,"H",3,[0,5],[None])
],
[
    weapon("Elfire","Upgraded fire tome.","Magic",5,85,0,None,None,[None],980,"M",2,35,[11,19],[3,9]),
    weapon("Elthunder","Upgraded thunder tome.","Magic",6,75,5,None,None,[None],1050,"M",2,35,[11,19],[2,4,6]),
    weapon("Elwind","Upgraded wind tome.","Magic",4,95,0,None,None,["Wing"],910,"M",2,35,[11,19],[4,5,6]),
    weapon("Nosferatu","Heal half of the given damage","Dark Magic",7,65,10,"Drain",None,[None],980,"M",2,20,[11,19],[5,7]),
    weapon("Iron Sword","Basic sword.","Sword",5,95,0,None,None,[None],520,"W",1,40,[2,4,6,10,14],[0,1]),    
    weapon("Iron Lance","Basic lance.","Lance",6,85,0,None,None,[None],560,"W",1,40,[2,3,9,16],[0,1]),    
    weapon("Iron Axe","Basic axe.","Axe",7,75,0,None,None,[None],600,"W",1,40,[2,4,9,17],[0,1]),
    weapon("Iron Bow","Basic bow.","Bow",6,85,0,None,None,["Wing"],560,"W",2,40,[2,3,6,10,20],[0,1]),
    weapon("Javelin","Basic ranged lance.","Lance",2,80,0,None,None,[None],700,"W",2,25,[5,6,9,12,16,24],[None]),
    weapon("Armorslayer","Strong against armor.","Sword",8,80,0,None,None,["Armor"],1450,"W",1,25,[30],[6,11,18,21,24]),
    weapon("Wyrmslayer","Strong against wyverns.","Sword",8,80,0,None,None,["Dragon"],1500,"W",1,25,[30],[0,2,3,13,15,16,17,18,19]),
    weapon("Beast Killer","Strong against horses.","Lance",9,70,0,None,None,["Horse"],1650,"W",1,25,[28],[1,5,7,13,14,16,17,18,19,21,23]),
    weapon("Hammer","Strong against armor.","Axe",10,60,0,None,None,["Armor"],1850,"W",1,25,[27],[0,4,5,6,13,14,15,16,17,18,19,21,24]),
    weapon("Hand Axe","Basic ranged axe.","Axe",3,70,0,None,None,[None],750,"W",2,25,[5,6,9,13,17,24],[None])
],
 [
    weapon("Arcfire","Uncommon fire tome.","Magic",8,80,0,None,None,[None],1440,"M",2,30,[15,21,24],[10,14]),
    weapon("Arcthunder","Uncommon thunder tome.","Magic",10,70,10,None,None,[None],1620,"M",2,30,[21,24],[8,10,13,16]),
    weapon("Arcwind","Uncommon wind tome.","Magic",6,90,0,None,None,["Wing"],1320,"M",2,30,[21,24],[11,13,20]),   
    weapon("Ruin","High crit!","Dark Magic",4,65,50,None,None,[None],1380,"M",2,20,[21,22],[8,12,17]),
    weapon("Steel Sword","Good sword.","Sword",8,90,0,None,None,[None],840,"W",1,30,[7,8,13,14],[2,3,4,5,6]),
    weapon("Steel Lance","Good lance.","Lance",9,80,0,None,None,[None],910,"W",1,35,[7,8,12,16],[2,3,4,5,6]),
    weapon("Steel Axe","Good axe.","Axe",11,70,0,None,None,[None],980,"W",1,35,[7,8,13,17],[2,3,4,5,6]),
    weapon("Steel Bow","Good bow.","Bow",9,80,0,None,None,["Wing"],910,"W",2,35,[7,8,12,20],[2,3,4,5,6]),
    weapon("Levin Sword","Thunder magic sword. Can attack from a distance.","Sword",10,80,0,None,None,[None],1600,"M",2,25,[31],[10,13,14,17,18,21,23]),
    weapon("Bolt Axe","Thunder magic axe. Can attack from a distance.","Axe",14,70,5,None,None,[None],1920,"M",2,30,[None],[None]),
    weapon("Noble Rapier","Elegant but deadly.","Sword",8,85,10,None,None,["Horse","Armor"],2100,"W",1,25,[31],[15,24]),
    weapon("Killing Edge","High crit!","Sword",9,90,30,None,None,[None],1470,"W",1,30,[14,22],[10,12,13,15,16,17,18,19,21,24]),
    weapon("Killer Lance","High crit!","Lance",10,80,30,None,None,[None],1680,"W",1,30,[16,23],[10,12,13,14,15,17,18,19,21,24]),    
    weapon("Killer Axe","High crit!","Axe",12,70,30,None,None,[None],1860,"W",1,30,[17,23],[10,12,13,14,15,16,18,19,21,24]),
    weapon("Killer Bow","High crit!","Bow",10,80,30,None,None,["Wing"],1680,"W",2,30,[20,22],[10,12,13,14,15,16,17,18,19,21,24]),
    weapon("Longbow","Can attack from a range of 3.","Bow",9,70,0,None,None,["Wing"],2150,"W",3,25,[31],[24,25]),
    weapon("Short Spear","Good ranged lance.","Lance",5,75,0,None,None,[None],1600,"W",2,25,[31],[8,10,12,13]),
    weapon("Short Axe","Good ranged axe.","Axe",7,65,0,None,None,[None],1750,"W",2,25,[31],[8,11,12,13]),
    item("Concoction","Good healing potion.",None,20,600,"H",3,[5,6,24],[None])
],
 [
    weapon("Bolganone","Rare fire tome.","Magic",12,75,0,None,None,[None],2000,"M",2,25,[25,30],[16,17,21,22,24]),
    weapon("Thoron","Rare thunder tome.","Magic",14,65,10,None,None,[None],2200,"M",2,25,[25,28],[14,15,21,24]),
    weapon("Rexcalibur","Rare wind tome.","Magic",10,85,0,None,None,["Wing"],1900,"M",2,25,[25,29],[15,20,21]),    
    weapon("Silver Sword","Somewhat rare sword.","Sword",9,80,0,None,[None],None,1410,"W",1,30,[13,14,15,22,30],[7,8,9,10,11,16,17,20]),
    weapon("Silver Lance","Somewhat rare lance.","Lance",13,75,0,None,[None],None,1560,"W",1,30,[12,15,16,23,28],[7,8,9,10,11,17,20]),
    weapon("Silver Axe","Somewhat rare axe.","Axe",15,65,0,None,None,[None],1740,"W",1,30,[13,15,17,23,27],[7,8,9,10,11,16,20]),
    weapon("Silver Bow","Somewhat rare bow.","Bow",13,75,0,None,None,["Wing"],1560,"W",2,30,[12,15,20,22,29],[7,8,9,10,11,16,17,20]),
    weapon("Tomahawk","Somewhat rare ranged axe.","Axe",10,60,0,None,[None],None,2550,"W",2,25,[25],[15,23]),
    weapon("Spear","Somewhat rare ranged lance.","Lance",8,70,0,None,[None],None,2400,"W",2,25,[25],[22,24]),
    item("Elixir","Great healing potion.",None,99,900,"H",3,[14,25,31],[None]),
    item("Master Seal","Use this to promote yourself. Level 10+ only.",10,None,10000,"C",1,[10,16,18],[None]),
    item("Second Seal","Use this to reclass yourself. Level 10+ only.",10,None,10000,"C",1,[13,14,17,21],[None])
],
 [
    weapon("Waste","Attack twice!","Dark Magic",10,45,0,"Brave",None,[None],2160,"M",2,30,[25,29],[21,23]),
    weapon("Brave Sword","Attack twice!","Sword",9,80,0,"Brave",None,[None],2100,"W",1,30,[26,30],[14,16,17,20,21,22,23,24,25]),
    weapon("Brave Lance","Attack twice!","Lance",10,70,0,"Brave",None,[None],2220,"W",1,30,[26,28],[14,16,17,20,21,22,23,24,25]),
    weapon("Brave Axe","Attack twice!","Axe",12,60,0,"Brave",None,[None],2400,"W",1,30,[26,27],[14,16,17,20,21,22,23,24,25]),
    weapon("Brave Bow","Attack twice!","Bow",10,70,0,"Brave",None,["Wing"],2220,"W",2,30,[26,29],[14,16,17,20,21,22,23,24,25]),
    weapon("Sol","Chance to recover half HP.","Sword",12,85,5,"Sol",None,[None],0,"W",1,30,[None],[None]),
    weapon("Luna","Chance to half opponent's defenses during damage calculation.","Lance",14,80,5,"Luna",None,[None],0,"W",1,30,[None],[None]),
    weapon("Astra","Chance to attack opponent five times with half damage.","Bow",14,75,5,"Astra",None,["Wing"],0,"W",2,30,[None],[None])
],
 [
    weapon("Valflame","Fala's fire magic. Mgc +5.","Magic",16,80,10,None,None,[None],0,"M",2,25,[None],[None]),
    weapon("Mjolnir","Tordo's thunder magic. Skl +5.","Magic",18,70,20,None,None,[None],0,"M",2,25,[None],[None]),
    weapon("Forseti","Holsety's wind magic. Spd +5.","Magic",14,90,10,None,None,["Wing"],0,"M",2,25,[None],[None]),
    weapon("Excalibur","Merric's wind tome. High crit.","Magic",13,100,30,None,None,["Wing"],0,"M",2,25,[None],[None]),
    weapon("Book of Naga","Naga's lost light magic, strong against dragons. Def and Res +5.","Magic",15,80,15,None,None,["Dragon"],0,"M",2,25,[None],[None]),
    weapon("Goetia","Otherworldly grimoire, haunting death by the arcane darkness!","Dark Magic",19,75,10,None,None,[None],0,"M",2,25,[None],[None]),
    weapon("Sol Katti","A plainsman's blade. Res +5.","Sword",8,100,50,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Tyrfing","Baldur's divine sword. Res +5.","Sword",15,85,10,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Balmung","Odo's assassin blade. Spd +5.","Sword",13,90,10,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Mystletainn","Hezul's demon sword. Skl +5.","Sword",14,85,15,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Ragnell","Ike's ranged blade. Def +5.","Sword",15,70,0,None,None,[None],0,"W",2,25,[None],[None]),
    weapon("Mercurius","Archanea's sword. Powerful.","Sword",17,95,5,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Gradivus","Archanea's javelin. Use this to recover all HP.","Lance",19,85,5,None,None,[None],0,"W",2,25,[None],[None]),
    weapon("Gungnir","Dain's draconic lance. Str +5.","Lance",16,70,10,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Hauteclere","Minerva's axe. Use this to recover all HP.","Axe",21,70,5,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Helswath","Neir's treasured ranged axe. Def +5.","Axe",18,60,10,None,None,[None],0,"W",2,25,[None],[None]),
    weapon("Armads","Hector's thunder axe. Def +5.","Axe",17,80,10,None,None,[None],0,"W",1,25,[None],[None]),
    weapon("Parthia","Archanea's bow. Res +5.","Bow",19,95,5,None,None,[None],0,"W",2,25,[None],[None]),
    weapon("Nidhogg","Frelia's serpent bow. Lck +10.","Bow",16,75,10,None,None,["Wing"],0,"W",2,25,[None],[None]),
    weapon("Double Bow","Powerful longbow of unknown origin. Str +5.","Bow",13,70,10,None,None,["Wing"],0,"W",3,25,[None],[None])
]
 
]
