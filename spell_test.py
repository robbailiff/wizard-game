from random import randint, choice

class Wizard:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.resist = 0
        self.attack = 5
        self.strength = 10
        self.powerup = 1
        self.pendant = 10
        self.spells = 10

    # Staff attacks
    def staff_attack(self, monster):
        atk_dmg = self.attack + (randint(1,5))
        monster.health = monster.health - atk_dmg
        print(f"{self.name} swings his staff at the {monster.name} and deals {atk_dmg} damage")
        return monster.health

    def arcane_attack(self, monster):
        atk_dmg = round(self.attack + (randint(0,3)) / monster.a_resist)
        monster.health = monster.health - atk_dmg
        print(f"{self.name} focuses his magical energy through his staff and fires arcane bolt at the {monster.name} dealing {atk_dmg} damage")
        return monster.health
        
    def fire_spell(self, monster):
        atk_dmg = round(((self.attack + randint(1,15)) * self.powerup) / monster.f_resist)
        monster.health = monster.health - atk_dmg
        self.powerup = 1
        self.spells -= 1
        print(f"{self.name} conjures a blast of fire that engulfs the {monster.name} and deals {atk_dmg} damage")
        return (monster.health, self.powerup, self.spells)

    def polymorph(self, monster):
        critter_list = ["Rat", "Frog", "Toad", "Newt", "Larva", "Crab", "Fish", "Squirrel", "Rabbit", "Chicken"]
        critter = choice(critter_list)
        self.spells -= 1
        print(f"{self.name} utters an incation which turns the {monster.name} into a {critter}!")
        return self.spells
        
        
class Monster:

    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
        self.a_resist = 1
        self.e_resist = 1
        self.f_resist = 1
        self.i_resist = 1

    def claw_attack(self, wizard):
        atk_dmg = self.attack + (randint(1,5))
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} attacks {wizard.name} with its claws and deals {atk_dmg} damage")
        return wizard.health

class Imp(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Imp"
        self.f_resist = 2
        self.i_resist = 0.5

    def fireball(self, wizard):
        atk_dmg = self.attack + (randint(1,10)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} hurls a ball of fire at {wizard.name} and deals {atk_dmg} damage")
        return wizard.health

    def choose_attack(self, wizard):
        atk = randint(1,4)
        if atk == 1:
            fireball = self.fireball(wizard)
            return fireball
        else:
            claw = self.claw_attack(wizard)
            return claw
            
#################################

wizard = Wizard("Horvath")
imp = Imp(20, 5)

imp.fireball(wizard)
print(" ")
wizard.staff_attack(imp)
print("Spells left: " + str(wizard.spells))
wizard.arcane_attack(imp)
print("Spells left: " + str(wizard.spells))
wizard.fire_spell(imp)
print("Spells left: " + str(wizard.spells))
wizard.polymorph(imp)
print("Spells left: " + str(wizard.spells))
