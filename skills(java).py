import java.util.Random;
import Weapon;
//Or something like that

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
proficiencyR = proficiencyR*1.5;
return true;

}
public boolean GaleForce(Monster o){
if(o.die()){
//insert turn renewal here
return true;
}
return false'
}







}
