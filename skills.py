import random
import sys
# If you do not have a weapon, you do not get to use any attack  Sorry.

pavise = ["Lance","Sword","Axe"]
aegis = ["Bow","Magic"]
notskill = ["HP","Strength","Magic","Skill","Speed","Luck","Defense","Resist","Brave","Drain"]
faireskills = ["Swordfaire","Lancefaire","Axefaire","Bowfaire","Tomefaire"]
breakerskills = ["Swordbreaker","Lancebreaker","Axebreaker","Bowbreaker","Tomebreaker"]
battleskills = ["Lethality","Aether","Astra","Luna","Ignis","Vengeance","Sol"]
internalskills = ["HP +5","Str +2","Mag +2","Skl +2","Spd +2","Lck +2","Def +2","Res +2","All Stats +2"]

def nihilcheck(hero, target): #checks if enemy has Nihil
    sk = setupskills(target)
    if len(sk) != 0 and 'Nihil' in target.skillset:
        return Nihil(target)
    return False

def setupskills(hero):
    allskills = hero.skillset
    if hero.equip != None and hero.equip.obj.effect != None:
        for i in range(len(hero.equip.obj.effect)):
                if hero.equip.obj.effect not in notskill:
                    allskills.append(hero.equip.obj.effect)
    return allskills

def dmgmod(hero, target, dmg):
    sk = setupskills(target)
    act = (target.skill >= random.randrange(100))
    half = False
    if act:
        c = hero.equip.obj.school
        if "Pavise" in sk and c in pavise:
            print("Pavise activated!")
            half = True
        elif "Aegis" in sk and c in aegis:
            print("Aegis activated!")
            half = True
    if half:
        dmg /= 2 
    return dmg

def statskillcheck(hero):
    sk = setupskills(hero)
    if len(sk) != 0:
        for i in range(len(sk)):
            skill = sk[i]
            if skill == "HP +5":
                hero.stats[0] += 5
                hero.max[0] += 5
            if skill == "Strength +2":
                hero.stats[1] += 2
                hero.max[1] += 2
            if skill == "Magic +2":
                hero.stats[2] += 2
                hero.max[2] += 2
            if skill == "Skill +2":
                hero.stats[3] += 2
                hero.max[3] += 2
            if skill == "Speed +2":
                hero.stats[4] += 2
                hero.max[4] += 2
            if skill == "Luck +4":
                hero.stats[5] += 4
                hero.max[5] += 2
            if skill == "Defense +2":
                hero.stats[6] += 2
                hero.max[6] += 2
            if skill == "Resist +2":
                hero.stats[7] += 2
                hero.max[7] += 2
            if skill == "All Stats +2":
                for i in range(1,8,1):
                    hero.stats[i] += 2
                    hero.max[i] += 2
    hero.setstats()

def battleskillcheck(hero, target, damage, nihil):
        sk = setupskills(hero)
        active = random.randrange(100)
        if len(sk) != 0 and not nihil:
            for i in range(len(sk)):
                if sk[i]:
                    skill = sk[i]
                    if skill == "Lethality" and int(hero.skill/4) >= active: #Arranging order by priority, must be hard-coded
                        return Lethality(hero, target)
                    elif skill == "Aether" and int(hero.skill/2) >= active:
                        return Aether(hero, target, damage)
                    elif skill == "Astra" and int(hero.skill/2) >= active:
                        return Astra(hero, target, damage)
                    elif skill == "Sol" and hero.skill >= active:
                        return Sol(hero, target, damage)
                    elif skill == "Luna" and hero.skill >= active:
                        return Luna(hero, target, damage)
                    elif skill == "Ignis" and hero.skill >= active:
                        return Ignis(hero, target, damage)
                    elif skill == "Vengeance" and hero.skill * 2 >= active:
                        return Vengeance(hero, target, damage)
        return hero.attacking(target, damage, nihil)

def postbattlecheck(hero, target):
    sk = setupskills(hero)
    if len(sk) != 0:
        for i in range(len(sk)): #skills can be simultaneously activated
            skill = sk[i]
            if target.isdead():
                if skill == "Despoil" and hero.luck >= random.randrange(100):
                    Despoil(hero)            
                if skill == "Lifetaker":
                    Lifetaker(hero)

def Weaponfaire(hero, skill, amount):
    k = hero.equip.obj.school
    sk = setupskills(hero)
    check = False
    faire = False
    if skill in hero.skillset:
        check = True
    if check: #Will activate upon equipping and unequipping
#        print("Now checking...")
        if k == "Sword" and "Swordfaire" in sk:
            print("Swordfaire activated!")
            faire = True
        elif k == "Lance" and "Lancefaire" in sk:
            print("Lancefaire activated!")
            faire = True
        elif k == "Axe" and "Axefaire" in sk:
            print("Axefaire activated!")
            faire = True
        elif k == "Bow" and "Bowfaire" in sk:
            print("Bowfaire activated!")
            faire = True
        elif k == "Magic" and "Tomefaire" in sk:
            print("Tomefaire activated!")
            faire = True
    if faire and hero.equip.obj.type == "W":
        hero.stats[1] += amount
        hero.max[1] += amount
    else:
        hero.stats[2] += amount
        hero.max[2] += amount
    hero.setstats()

'''
def Weaponfaire(hero, str, mag, sk):
	wep = hero.equip.obj.school
	type = hero.equip.obj.type
	s = st
	m = mag
	faire = False
	if "Swordfaire" in sk and wep == "Sword":
		faire = True
	elif "Lancefaire" in sk and wep == "Lance":
		faire = True
	elif "Axefaire" in sk and wep == "Axe":
		faire = True
	elif "Bowfaire" in sk and wep == "Bow":
		faire = True
	if faire and type == "W":
		s+=5
	#This is for the following weapons: Levin Sword, Shock Stick, Bolt Axe
	elif faire and type == "M":
		m+= 5
		return m
	return s


def Tomefaire(hero, mag, sk):
	wep = hero.equip.obj.school
	m = mag
	faire = False
	if "Tomefaire" in sk and wep == "Magic":
		faire = True
	if faire:
		m += 5
	return m
'''

def hitmidbattlecheck(hero, target, hit): #good guys
    sk = setupskills(hero)
    h = hit
    if target.equip != None:
        h = breakercheck(hit, hero, target, sk)
    if len(sk) != 0:
        for i in range(len(sk)):
            skill = sk[i]
            if skill == "Prescience":
                print("Prescience activated!")
                h += 10
    return h

def avomidbattlecheck(hero, target, avo): #bad guys
    sk = setupskills(target)
    sk2 = setupskills(hero)
    a = avo
    if hero.equip != None:
        a = secondbreakercheck(avo, hero, target, sk)
    if len(sk) != 0:
        if "Patience" in sk:
            print("Patience activated!")
            a += 10
        if "Miracle" in sk:
            a += Miracle(hero)
    if len(sk2) != 0:
        if "Hex" in sk2:
            print("Hex activated!")
            a -= 15
        if "Anathema" in sk2:
            print("Anathema activated!")
            a -= 10
    return a, c

def Anathema(hero): #separate anathema skill to modify crit
    sk = setupskills(hero)
    if "Anathema" in sk:
        return 10
    return 0

def breakercheck(hit, hero, target, sk):
    h = hit
    weapon = target.equip.obj.school
    breaker = False
    if "Swordbreaker" in sk and weapon == "Sword":
        print("Swordbreaker activated!")
        breaker = True
    elif "Lancebreaker" in sk and weapon == "Lance":
        print("Lancebreaker activated!")
        breaker = True
    elif "Axebreaker" in sk and weapon == "Axe":
        print("Axebreaker activated!")
        breaker = True
    elif "Bowbreaker" in sk and weapon == "Bow":
        print("Bowbreaker activated!")
        breaker = True
    elif "Tomebreaker" in sk and weapon == "Magic":

        print("Tomebreaker activated!")
        breaker = True
    if breaker:
        h += 50
    return h

def secondbreakercheck(avo, hero, target, sk):
    a = avo
    weapon = hero.equip.obj.school
    breaker = False
    if "Swordbreaker" in sk and weapon == "Sword":
        print("Swordbreaker activated!")
        breaker = True
    elif "Lancebreaker" in sk and weapon == "Lance":
        print("Lancebreaker activated!")
        breaker = True
    elif "Axebreaker" in sk and weapon == "Axe":
        print("Axebreaker activated!")
        breaker = True
    elif "Bowbreaker" in sk and weapon == "Bow":
        print("Bowbreaker activated!")
        breaker = True
    elif "Tomebreaker" in sk and weapon == "Magic":
        print("Tomebreaker activated!")
        breaker = True
    if breaker:
        a += 50
    return a

def Wrath(hero):
    sk = setupskills(hero)
    if len(sk) != 0:
        if "Wrath" in sk and hero.HP <= int(hero.HP / 2):
            print("Wrath activated!")
            return 20
    return 0

def Armsthrift(hero):
    sk = setupskills(hero)
    if len(sk) != 0:
        if "Armsthrift" in sk and random.randrange(100) <= hero.luck * 2:
            print("Armsthrift activated!")
            return True
    return False

def Miracle(hero):
    if hero.HP < 11:
        print("Miracle activated!")
        return 10 * (11 - hero.HP)
    return 0    

def Lethality(hero, target): #This will be player only because hax sucks
    print("Lethality activated! ")
    dmg = target.HP
    target.HP = 0
    return dmg

def Nihil(target): #Blocks critical hits(FE4) and activation of other skills(FE4, 5, 9, 10). Amazing.
    print("Nihil activated!")
    return True

def Astra(hero, target, damage): #halves damage, but allows the unit to hit 5 times
    times = 0
    accum = 0
    print("Astra activated! ")
    while times < 5 and target.HP > 0:
        hit = hero.attacking(target, int(damage / 2))
        accum += hit
        sys.stdout.write("Hit number {}! Dealt {} damage!\n".format(times+1, hit))
        times += 1
    return accum

def Luna(hero, target, damage):
    sys.stdout.write("Luna activated! ")
    if hero.equip.obj.type == "W":
        damage += int(hero.strength / 2)
    else:
        damage += int(hero.magic / 2)
    return hero.attacking(target, damage)

def Sol(hero, target, damage):
    sys.stdout.write("Sol activated! ")
    d = hero.attacking(target, damage)
    hero.heal(int(d/2))
    return d

def Ignis(hero, target, damage):
    sys.stdout.write("Ignis activated! ")
    if hero.equip.obj.type == "W":
        damage += int(hero.magic/2) 
    else:
        damage += int(hero.strength/2)
    return hero.attacking(target,damage)

def Aether(hero, target, damage):
    sys.stdout.write("Aether activated! ")
    dmg = 0
    dmg += Aether1(hero, target, damage)
    if target.HP <= 0:
        dmg += Aether2(hero, target, damage)
    return dmg

def Aether1(hero, target, damage):
    hero.attacking(target, damage)
    hero.heal(int(damage/2))
    return damage

def Aether2(hero, target, damage):
    if hero.equip.obj.type == "W":
        damage += int(hero.strength / 2)
    else:
        damage += int(hero.magic / 2)
    return hero.attacking(target, damage)

def Vengeance(hero, target, damage):
    sys.stdout.write("Vengeance activated! ")
    damage += int((hero.maxHP - hero.HP) / 2)
    return hero.attacking(target, damage)

def Despoil(hero):
    sys.stdout.write("Despoil activated! Gained 1000G.")
    hero.money += 1000

def Lifetaker(hero):
    sys.stdout.write("Lifetaker activated! ")
    hero.heal(int(hero.maxHP / 2))

def Counter(hero, target, dmg):
    sk = setupskills(target)
    if len(sk) != 0:
        for i in range(len(sk)):
            skill = sk[i]
            if skill == "Counter":
                print("Counter activated! {} reprisal from Counter!".format(dmg))
                hero.HP -= dmg
    

'''
public class Skills{

Random procRate = new Random();

//Damage manipulating skills
//priority: Lethality, Astra, Aether(?), Luna/Ignis, Vengeance
public void Luna(int skill, Monster o, Player p){
//halves target defense
int proc = skill/2;
int rate = procRate.nextInt(99)+1;
if(rate <= proc){
if(p.equip().type().equals("W")
o.defense() = o.defense()/2;
if(p.equip().type().equals("M")
o.resistance() = o.resistance()/2;
}
}

public void LunaE(Monster o, Player p){
//secondary effect for Aether, in essence, should only be used for this purpose
if(p.equip().type().equals("W")
o.defense() = o.defense()/2;
if(p.equip().type().equals("M")
o.resistance() = o.resistance()/2;
}

}
public void Astra(int skill, int damage, Player p1, Monster o){
//halves damage, but allows the unit to hit 5 times
d = damage/2;
int p = skill/2;
int r = procRate.nextInt(99)+1;
if(r <= p){
//each hit has a crit chance. Other abilities except Sol/Luna(I think) do not stack
for(int x = 0; x < 5; x++){
attack(p1, p1.equip(), o, d);
}

}
public void Aether(int skill, int damage, Player p1, Monster o){
int d = 0;
int p = skill/2;
int r = 100*Math.random()+1;
if(r <= p){
d = attack(p1, p1.equip(), o, damage);
heal(d/2);
LunaE(o);
d+= attack(p1, p1.equip(), o, damage;
}
}
}
public void Ignis(int skill, int mag, int str, int attack, String wType){
// half of str/mag is added to attack
int p = skill/2;
int r = procRate.nextInt(99)+1;
if(r <=p) {
if(wType.equals("W"){
attack += mag/2;}
if(wType.equals("M"){
attack += str/w;
}
}
}
public void Lethality(int skill, int eHP){
//instant kill
proc = skill/4;
int rate = procRate.nextInt(99)+1;
if(rate <= proc){
eHP = 0;
}
public void Vengeance(int damage, int rDamage){
//half of damage taken is added into next attack
damage += rDamage/2;
}
}
public void Sol(int damageD, int skill){
//deals half of the damage dealt
int p = skill/2;
int r = 100*Math.random()+1;
if(r <= p)
heal(damageD/2);

}
//misc skills
public boolean Armshrift(int luck){
//preserves weapon durability
int proc = luck*2;
int rate = procRate.nextInt(99)+1;
if(rate <= proc){
return true;
}
return false;
}
public boolean Miracle(int luck, int rDamage, int hp){
//Ensures survival through an otherwise lethal hit, triggers AFTER damage is taken
int p = luck/2;
int r = procRate.nextInt(99)+1;
if(r <= p && rDamage > 79){
hp = 1;
}
}
public boolean Tomefaire(String wT, int magic){
if(wT = "M"){
magic += 5;
return true;
}
return false;

}

public boolean HPPlusFive(int maxhp){
maxhp += 5;
return true;
}

public boolean Discipline(double proficiencyR){
proficiencyR = proficienc
'''
