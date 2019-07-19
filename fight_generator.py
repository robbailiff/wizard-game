"""
This is a random fight generator I've made using a section of code from a larger wizard game I've been working on for a while now.

I have tested it a bit but there may be some encounters that are unbalanced. 

I'd be happy for any feedback on any bugs or ways I can improve or clean up the code.

Enjoy!

"""

# Import libraries
from random import randint, choice

###############
### Classes ###
###############

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
        print(f"{self.name} focuses his magical energy through his staff and fires an arcane bolt at the {monster.name} dealing {atk_dmg} damage")
        return monster.health

    # Combat Spells
    def electric_spell(self, monster):
        atk_dmg = round(((self.attack + randint(1,15)) * self.powerup) / monster.e_resist)
        monster.health = monster.health - atk_dmg
        self.powerup = 1
        self.spells -= 1
        print(f"{self.name} fires a charged bolt of lightning at the {monster.name} and deals {atk_dmg} damage")
        return (monster.health, self.powerup, self.spells)

    def fire_spell(self, monster):
        atk_dmg = round(((self.attack + randint(1,15)) * self.powerup) / monster.f_resist)
        monster.health = monster.health - atk_dmg
        self.powerup = 1
        self.spells -= 1
        print(f"{self.name} conjures a blast of fire that engulfs the {monster.name} deals {atk_dmg} damage")
        return (monster.health, self.powerup, self.spells)

    def ice_spell(self, monster):
        atk_dmg = round(((self.attack + randint(1,15)) * self.powerup) / monster.i_resist)
        monster.health = monster.health - atk_dmg
        self.powerup = 1
        self.spells -= 1
        print(f"{self.name} fires a shard of ice that pierces into the {monster.name} deals {atk_dmg} damage")
        return (monster.health, self.powerup, self.spells)

    def shield_spell(self):
        self.resist = self.resist + 5
        self.spells -= 1
        print(f"{self.name} casts a shield spell to reduce the damage taken from energy based attacks")
        return (self.resist, self.spells)

    def powerup_spell(self):
        self.powerup = 2
        self.spells -= 1
        print(f"{self.name} focuses spell energy to increase the power of the next attack spell")
        return (self.powerup, self.spells)

    # Heal Ability
    def heal_pendant(self):
        heal = 5 + (randint(1,6))
        self.health = self.health + heal
        print(f"{self.name} uses the Pendant of Healing and regains {heal} life")
        return (self.health, self.pendant)


class Familiar:
    # familiar to be a bat
    def __init__(self, name):
        self.name = name
        self.attack = 1

    def bite(self, monster):
        atk_dmg = self.attack + (randint(1,3))
        monster.health = monster.health - atk_dmg
        print(f"{self.name} swoops down and bites the {monster.name} with its fangs and deals {atk_dmg} damage")
        return monster.health

    def leech(self, monster, wizard):
        atk_dmg = self.attack + (randint(1,2))
        monster.health = monster.health - atk_dmg
        wizard.health = wizard.health + atk_dmg
        print(f"{self.name} bites and leeches the life from the {monster.name}. It deals {atk_dmg} damage and gives {atk_dmg} life back to {wizard.name}")
        return (wizard.health, monster.health)

    def choose_attack(self, monster, wizard):
        atk = randint(1,4)
        if atk == 1:
            leech = self.leech(monster, wizard)
            return leech
        else:
            bite = self.bite(monster)
            return bite


class Monster:

    def __init__(self, health, attack):
        self.health = health
        self.attack = attack
        self.a_resist = 1
        self.e_resist = 1
        self.f_resist = 1
        self.i_resist = 1
        self.powerup = 1

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

class Firecat(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Firecat"
        self.f_resist = 2
        self.i_resist = 0.5

    def flaming_bite(self, wizard):
        atk_dmg = 10 + (randint(1,10)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} bites {wizard.name} with it flaming fangs and deals {atk_dmg} damage")
        return wizard.health

    def choose_attack(self, wizard):
        atk = randint(1,4)
        if atk == 1:
            flaming = self.flaming_bite(wizard)
            return flaming
        else:
            claw = self.claw_attack(wizard)
            return claw


class MagmaElemental(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Magma Elemental"
        self.f_resist = 3
        self.i_resist = 0.5

    def slam_attack(self, wizard):
        atk_dmg = self.attack + (randint(1,5)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} uses its scorching arms to slam {wizard.name} and deals {atk_dmg} damage")
        return wizard.health

    def magma_ball(self, wizard):
        atk_dmg = 5 + (randint(1,10)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} hurls an ball of searing magma at {wizard.name} and deals {atk_dmg} damage")
        return wizard.health

    def choose_attack(self, wizard):
        atk = randint(1,4)
        if atk == 1:
            spray = self.magma_ball(wizard)
            return spray
        else:
            slam = self.slam_attack(wizard)
            return slam


class HellKnight(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Hellknight"
        self.f_resist = 2
        self.e_resist = 0.75
        self.powerup = 1

    def flame_sword(self, wizard):
        atk_dmg = ((self.attack + randint(1,10)) * self.powerup) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        self.powerup = 1
        print(f"The {self.name} strikes {wizard.name} with his flaming blade and deals {atk_dmg} damage")
        return (wizard.health, self.powerup)

    def flame_strike(self, wizard):
        atk_dmg = self.attack + (randint(1,20)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} shoots a burst of fire from his sword that hits {wizard.name} and deals {atk_dmg} damage")
        return wizard.health

    def imbue(self):
        self.powerup = 2
        print(f"{self.name} focuses energy into his sword to increase the power of his next strike")
        return self.powerup

    def choose_attack(self, wizard):
        atk = randint(1,6)
        if atk == 1:
            powerup = self.imbue()
            return powerup
        elif atk == 2:
            flame = self.flame_strike(wizard)
            return flame
        else:
            sword = self.flame_sword(wizard)
            return sword


class FleshGolem(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Flesh Golem"
        self.a_resist = 2
        self.e_resist = 4
        self.f_resist = 0.75

    def slam_attack(self, wizard):
        atk_dmg = self.attack + (randint(1,5))
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} slams down its huge arms on {wizard.name} and deals {atk_dmg} damage")
        return wizard.health

    def choose_attack(self, wizard):
        slam = self.slam_attack(wizard)
        return slam


class Lich(Monster):

    def __init__(self, health, attack):
        super().__init__(health, attack)
        self.name = "Lich"
        self.i_resist = 2

    def shadow_blast(self, wizard):
        atk_dmg = self.attack + (randint(1,10)) - wizard.resist
        wizard.health = wizard.health - atk_dmg
        print(f"The {self.name} blasts {wizard.name} with dark energy and deals {atk_dmg} damage")
        return wizard.health

    def sap_strength(self, wizard):
        str_dmg = randint(1,2)
        wizard.strength =  wizard.strength - str_dmg
        print(f"The {self.name} touches {wizard.name} with the chill of undeath and deals {str_dmg} strength damage")
        return wizard.strength

    def leech_life(self, wizard):
        atk_dmg = randint(3,10)
        wizard.health = wizard.health - atk_dmg
        self.health = self.health + atk_dmg
        print(f"{self.name} bites and leeches the life from the {wizard.name}.\nIt deals {atk_dmg} damage and gives {atk_dmg} life back to {self.name}")
        return (wizard.health, self.health)

    def choose_attack(self, wizard):
        atk = randint(1,6)
        if atk == 1:
            sap = self.sap_strength(wizard)
            return sap
        elif atk == 2:
            shadow = self.shadow_blast(wizard)
            return shadow
        elif atk == 3:
            leech = self.leech_life(wizard)
            return leech
        else:
            claw = self.claw_attack(wizard)
            return claw

######################
### Name Generator ###
######################

def name_gen():
    # Forename generator lists
    start_cons = ["b", "c", "ch", "d", "dr", "f", "fr", "g", "h", "j", "k", "l", "m", "n" , "p", "qu", "r", "s", "st","t", "th", "v", "w", "x", "y", "z"]
    p_mid_cons = ["b", "c", "d", "dr", "f", "g", "h", "k", "l", "m", "n" , "p", "ph", "r", "s", "st","t", "th", "v", "z"]
    s_mid_cons = "b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "r", "s", "st", "t", "th", "v", "z"
    end_cons = ["d", "dh", "hl", "hr", "l", "lf", "lyn", "m", "n", "r", "rn", "ryn", "s", "st", "ster", "t", "th", "z"]
    vowel = ["a", "e", "i", "o", "u"]
    end_vowel = ["a", "i", "o", "u"]
    db_vowel = ["ae", "ai", "ao", "au", "ea", "ei", "eo", "eu", "ia", "ie", "io", "oa", "uo"]

    # List of titles
    titles = ["Adept", "Amazing", "Alchemist", "Artificer", "Arcanist", "Archivist", "Artisan", "Astute", "Adventurous", "Archmage", "Apprentice", "Blue", "Brown", "Black", "Blessed", "Bright", "Brilliant", "Bold", "Brave", "Crafty", "Cunning", "Conjurer", "Curator", "Champion", "Clever", "Clairvoyant", "Confident", "Diviner", "Dazzling", "Daring", "Dauntless", "Dignified", "Distinguished", "Dream-walker", "Deathless", "Deceptive", "Evoker", "Enchanter", "Exalted", "Enlightened", "Exceptional", "Enduring", "Educated", "Elder", "Eldritch", "Eloquent", "Fantastic", "Fascinating", "Fearless", "Fabulous", "Fabled", "Faceless", "Famed", "Famous", "Favoured", "Fervent", "Flawless", "Green", "Grey", "Guardian", "Genious", "Gallant", "Great", "Grand", "Gifted", "Glorious", "Golden", "Good", "Graceful", "Grandmaster", "Hermit", "Hardened", "Highborn", "Honourable", "Heroic", "Hallowed", "Harmonious", "Hawk-eyed", "Healer", "Herbalist", "Honest", "Inventor", "Indomitable", "Invincible", "Illuminator", "Illusionist", "Ingenius", "Insightful", "Imperial", "Initiate", "Judicious", "Joyous", "Just", "Journeyed", "Jovial", "Jolly", "Jolting", "Keeper", "Knowing", "Knowledgeable", "Kingly", "Leader", "Lucky", "Luckbringer", "Loremaster", "Learned", "Laudable", "Liberator", "Magician", "Magus", "Mystic", "Marvellous", "Mighty", "Mindreader", "Master", "Masterful", "Magnificent", "Mysterious", "Noble", "Nomad", "Nameless", "Naturalist", "Negotiator", "Nice", "Novice", "Oracle", "Orange", "Occultist", "Old", "Obstinate", "Observer", "Omnipotent", "Optimal", "Otherworldly", "Obsessive", "Powerful", "Potent", "Purple", "Pink", "Psychic", "Perceptive", "Pyromancer", "Philosopher", "Peerless", "Quick", "Quick-witted", "Quizzical", "Questioning", "Resolute", "Red", "Runekeeper", "Rover", "Reverent", "Ready", "Rabble-rouser", "Rapturous", "Resplendent", "Researcher", "Redeemer", "Reformer", "Scholar", "Scribe", "Steadfast", "Seer", "Sorcerer", "Summoner", "Sage", "Savant", "Seeker", "Traveller", "Truthseeker", "Trickster", "Transmuter", "Thaumaturge", "Tutor", "Unwavering", "Unyielding", "Unflinching", "Undaunted", "Unfaltering", "Unfearing", "Undying", "Valiant", "Valorous", "Vanquisher", "Venerable", "Veteran", "Vigilant", "Visionary", "Wise", "Wonderer", "Wondrous", "Witty", "Willful", "Wayfarer", "Yellow", "Young", "Youthful", "Zealous", "Zealot"]



    p_start = choice(start_cons)
    p_mid = choice(vowel) + choice(p_mid_cons)
    p_end = choice(vowel)

    num = randint(1,2)
    if num == 1:
        prefix = p_mid + p_end
        prefix = prefix.capitalize()
    else:
        prefix = p_start + p_mid + p_end
        prefix = prefix.capitalize()

    s_start = choice(s_mid_cons)
    s_mid = choice(vowel)
    s_end = choice(end_cons)

    num2 = randint(1,6)
    if num2 == 1 or num2 == 2:
        suffix = choice(s_mid_cons) + choice(vowel) + choice(end_cons)

    elif num2 == 3:
        suffix = choice(s_mid_cons) + choice(vowel) + choice(end_cons) + choice(end_vowel)

    else:
        suffix = choice(end_cons)


    forename = prefix + suffix

    letter = forename[0]
    title_list = []

    if letter == 'X' or letter == 'Z':
        for t in titles:
            if t[0] == 'S' or t[0] == 'Z':
                title_list.append(t)

    elif letter == 'Y':
        for t in titles:
            if t[0] == 'J' or t[0] == 'Y':
                title_list.append(t)

    elif letter == 'J':
        for t in titles:
            if t[0] == 'J' or t[0] == 'G':
                title_list.append(t)

    elif letter == 'K':
        for t in titles:
            if t[0] == 'C' or t[0] == 'K':
                title_list.append(t)

    else:
        for t in titles:
            if t[0] == letter:
                title_list.append(t)

    wiz_name = forename + " the " + choice(title_list)
    return wiz_name


######################
### Fight Function ###
######################

def fight(wizard, monster, familiar, surprise=False):

   # Initiative rolls
    while True:
        human_roll = randint(1,6)
        comp_roll = randint(1,6)

        if surprise == True:
            print(f"{wizard.name} has taken the {monster.name} by surprise and gets to act first!\n")
            player1 = wizard
            player2 = monster
            break

        elif human_roll > comp_roll:
            print(f"{wizard.name} has the initiative and gets to act first!\n")
            player1 = wizard
            player2 = monster
            break

        elif comp_roll > human_roll:
            print(f"{monster.name} has the initiative and gets to act first!\n")
            player1 = monster
            player2 = wizard
            break

        else:
            continue

    health1 = player1.health
    health2 = player2.health
    strength = wizard.strength

    print("Get ready to fight!\n")

    # Main fight loop
    while health1 > 0 and health2 > 0 and strength > 0:

        while player1 == wizard and health1 > 0 and health2 > 0 and strength > 0:

            # Wizard action choice

            action = randint(1,3)

            if action == 1:

                while True:
                    try:
                        staff = randint(1,2)

                        if staff == 1:
                            result = player1.staff_attack(player2)
                            health2 = result
                            print(f"{player2.name} is down to {health2} health\n")
                            break

                        elif staff == 2:
                            result = player1.arcane_attack(player2)
                            health2 = result
                            print(f"{player2.name} is down to {health2} health\n")
                            break
                    except:
                        print("That was not a valid input!")
                        continue

                    break

            elif action == 2:

                while True:
                    try:
                        spell = randint(1,5)

                        if spell == 1:
                            result = player1.electric_spell(player2)
                            health2 = result[0]
                            player1.powerup = result[1]
                            player1.spells = result[2]
                            print(f"{player2.name} is down to {health2} health\n")
                            break

                        elif spell == 2:
                            result = player1.fire_spell(player2)
                            health2 = result[0]
                            player1.powerup = result[1]
                            player1.spells = result[2]
                            print(f"{player2.name} is down to {health2} health\n")
                            break

                        elif spell == 3:
                            result = player1.ice_spell(player2)
                            health2 = result[0]
                            player1.powerup = result[1]
                            player1.spells = result[2]
                            print(f"{player2.name} is down to {health2} health\n")
                            break

                        elif spell == 4:
                            result = player1.shield_spell()
                            player1.resist = result[0]
                            player1.spells = result[1]
                            break

                        elif spell == 5:
                            result = player1.powerup_spell()
                            player1.powerup = result[0]
                            player1.spells = result[1]
                            break

                    except:
                        print("That was not a valid input!")
                        continue

                    break

            elif action == 3:
                result = player1.heal_pendant()
                health1 = result[0]
                player1.pendant = result[1]
                print(f"{player1.name} is now up to {health1} health\n")
                break

            else:
                print("That was not a valid input!")
                continue

            break


        while player2 == monster and health1 > 0 and health2 > 0 and strength > 0:

            # Monster attack choice
            result = player2.choose_attack(player1)
            r_type = type(result)
            if r_type == tuple:
                index_1 = result[1]
                if index_1 == 1:
                    health1 = result[0]
                    print(f"{player1.name} is down to {health1} health\n")
                elif index_1 > 1:
                    health1 = result[0]
                    health2 = result[1]
                    print(f"{player1.name} is down to {health1} health\n")
                    
            elif result is wizard.strength:
                strength = result
                print(f"{player1.name} is down to {strength} strength\n")
                
            elif result is monster.powerup:
                pass
            
            else:
                health1 = result
                print(f"{player1.name} is down to {health1} health\n")

            # Familiar attack choice
            fam_result = familiar.choose_attack(player2, player1)
            if type(fam_result) == tuple:
                health2 = fam_result[1]
                print(f"{player2.name} is down to {health2} health\n")
            else:
                health2 = fam_result
                print(f"{player2.name} is down to {health2} health\n")
            break


        while player1 == monster and health1 > 0 and health2 > 0 and strength > 0:

            # Monster attack choice
            result = player1.choose_attack(player2)
            r_type = type(result)
            if r_type == tuple:
                index_1 = result[1]
                if index_1 == 1:
                    health2 = result[0]
                    print(f"{player2.name} is down to {health1} health\n")
                elif index_1 > 1:
                    health2 = result[0]
                    health1 = result[1]
                    print(f"{player2.name} is down to {health1} health\n")
                    
            
            elif result is wizard.strength:
                strength = result
                print(f"{player2.name} is down to {strength} strength\n")
            
            elif result is monster.powerup:
                pass
            
            else:
                health2 = result
                print(f"{player2.name} is down to {health2} health\n")

            # Familiar attack choice
            fam_result = familiar.choose_attack(player1, player2)
            if type(fam_result) == tuple:
                health1 = fam_result[1]
                print(f"{player1.name} is down to {health1} health\n")
            else:
                health1 = fam_result
                print(f"{player1.name} is down to {health1} health\n")
            break

        while player2 == wizard and health1 > 0 and health2 > 0 and strength > 0:

                # Wizard action choice

                action = randint(1,3)

                if action == 1:

                    while True:
                        try:
                            staff = randint(1,2)

                            if staff == 1:
                                result = player2.staff_attack(player1)
                                health1 = result
                                print(f"{player1.name} is down to {health1} health\n")
                                break

                            elif staff == 2:
                                result = player2.arcane_attack(player1)
                                health1 = result
                                print(f"{player1.name} is down to {health1} health\n")
                                break
                        except:
                            print("That was not a valid input!")
                            continue

                        break

                elif action == 2:

                    while True:
                        try:
                            spell = randint(1,5)

                            if spell == 1:
                                result = player2.electric_spell(player1)
                                health1 = result[0]
                                player2.powerup = result[1]
                                player2.spells = result[2]
                                print(f"{player1.name} is down to {health1} health\n")
                                break

                            elif spell == 2:
                                result = player2.fire_spell(player1)
                                health1 = result[0]
                                player2.powerup = result[1]
                                player2.spells = result[2]
                                print(f"{player1.name} is down to {health1} health\n")
                                break

                            elif spell == 3:
                                result = player2.ice_spell(player1)
                                health1 = result[0]
                                player2.powerup = result[1]
                                player2.spells = result[2]
                                print(f"{player1.name} is down to {health1} health\n")
                                break

                            elif spell == 4:
                                result = player2.shield_spell()
                                player2.resist = result[0]
                                player2.spells = result[1]
                                break

                            elif spell == 5:
                                result = player2.powerup_spell()
                                player2.powerup = result[0]
                                player2.spells = result[1]
                                break

                        except:
                            print("That was not a valid input!")
                            continue

                        break

                elif action == 3:
                    result = player2.heal_pendant()
                    health2 = result[0]
                    player2.pendant = result[1]
                    print(f"{player2.name} is now up to {health2} health\n")
                    break

                else:
                    print("That was not a valid input!")
                    continue

                break


    if health1 <=0 and health2 <= 0:
        print("It's a draw")

    elif player1 == wizard and health1 <= 0 or strength <= 0:
        print("You lose!")

    elif player2 == wizard and health2 <= 0 or strength <= 0:
        print("You lose!")

    elif player1 == wizard and health2 <= 0:
        print("You win!")

    elif player2 == wizard and health1 <= 0:
        print("You win!")



#################
### Main Game ###
#################
wiz_name = name_gen()

### Class Instances ###
my_wizard = Wizard(wiz_name)
my_familiar = Familiar("Nightwing")
imp = Imp(80, 5)
firedemon = FireDemon(80, 10)
firecat = Firecat(80, 10)
elemental = MagmaElemental(80, 10)
hellknight = HellKnight(80, 10)
golem = FleshGolem(90, 10)
lich = Lich(100, 10)

monster_list = [imp, firedemon, firecat, elemental, hellknight, golem, lich]
monster_choice = choice(monster_list)

print("You will play as " + str(wiz_name))
print("Your opponent will be the " + str(monster_choice.name))

fight(my_wizard, monster_choice, my_familiar)
