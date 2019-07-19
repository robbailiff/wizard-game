from random import randint

class Wizard:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.resist = 0

class Monster:

    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
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

class FireDemon(Imp):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Fire Demon"

    def choose_attack(self, wizard):
        atk = randint(1,4)
        if atk == 1:
            fireball = self.fireball(wizard)
            return fireball
        else:
            claw = self.claw_attack(wizard)
            return claw

wizard = Wizard("Horus")
demon = FireDemon(50, 8)

demon.claw_attack(wizard)
demon.fireball(wizard)
