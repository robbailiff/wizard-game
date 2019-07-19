from random import choice, randint

start_cons = ["b", "c", "ch", "d", "dr", "f", "fr", "g", "h", "j", "k", "l", "m", "n" , "p", "qu", "r", "s", "st","t", "th", "v", "w", "x", "y", "z"]
p_mid_cons = ["b", "c", "ch", "d", "dr", "f", "fr", "g", "h", "k", "l", "m", "n" , "p", "ph", "r", "s", "st","t", "th", "v", "z"]
s_mid_cons = "b", "c", "d", "f", "g", "h", "k", "l", "m", "n", "r", "s", "st", "t", "th", "v", "z"
end_cons = ["d", "dh", "hl", "hr", "l", "lf", "lyn", "m", "n", "r", "rn", "ryn", "s", "st", "ster", "t", "th", "z"]
vowel = ["a", "e", "i", "o", "u"]
end_vowel = ["a", "i", "o", "u"]
db_vowel = ["ae", "ai", "ao", "au", "ea", "ei", "eo", "eu", "ia", "ie", "io", "oa", "uo"]
#db_vowel = ["ae", "ai", "ao", "au", "ea", "ei", "eo", "eu", "ia", "ie", "io", "iu", "oa", "oe", "oi", "ou", "ua", "ue", "ui", "uo"]


#suffix = ["riel", "driel", "thriel", "yiel", "tiel", "siel", "liel", "ziel", "xiel", "ciel", "viel", "biel", "niel", "mel", "del", "thel", "sel", "rel", "yel", "fel", "gel", "jel", "kel", "zel", "xel", "vel", "bel", "nel", "mal", "dal", "thal", "sal", "ral", "yal", "fal", "gal", "jal", "kal", "zal", "xal", "val", "bal", "nal", "baster", "rana", "tana", "yana", "sana", "gana", "jana", "lana", "kana", "zana", "xana", "cana", "vana", "bana", "mana", "thana","rano", "tano", "yano", "sano", "gano", "jano", "lano", "kano", "zano", "xano", "cano", "vano", "bano", "mano", "thano", "rani", "tani", "yani", "sani", "gani", "jani", "lani", "kani", "zani", "xani", "cani", "vani", "bani", "mani", "thani", "bar", "tar", "yar", "sar", "dar", "gar", "jar", "thar", "kar", "lar", "zar", "xar", "car", "var", "mar", "rar","bor", "tor", "yor", "sor", "dor", "gor", "jor", "thor", "kor", "lor", "zor", "xor", "cor", "vor", "mor", "ror","bir", "tir", "yir", "sir", "dir", "gir", "jir", "thir", "kir", "lir", "zir", "xir", "cir", "vir", "mir", "rir", "bin", "tin", "yin", "sin", "din", "gin", "jin", "thin", "kin", "lin", "zin", "xin", "cin", "vin", "min", "rin", "born", "torn", "yorn", "sorn", "dorn", "gorn", "jorn", "thorn", "korn", "lorn", "zorn", "xorn", "corn", "vorn", "morn", "rorn", "bon", "ton", "yon", "son", "don", "gon", "jon", "thon", "kon", "lon", "zon", "xon", "con", "von", "mon", "ron", "zoth", "xoth", "roth", "loth", "voth", "goth"]


titles = ["Adept", "Amazing", "Alchemist", "Artificer", "Arcanist", "Archivist", "Artisan", "Astute", "Adventurous", "Archmage", "Blue", "Brown", "Black", "Blessed", "Bright", "Brilliant", "Bold", "Brave", "Crafty", "Cunning", "Conjurer", "Curator", "Champion", "Clever", "Clairvoyant", "Confident", "Diviner", "Dazzling", "Daring", "Dauntless", "Dignified", "Distinguished", "Dream-walker", "Deathless", "Deceptive", "Evoker", "Enchanter", "Exalted", "Enlightened", "Exceptional", "Enduring", "Educated", "Elder", "Eldritch", "Eloquent", "Fantastic", "Fascinating", "Fearless", "Fabulous", "Fabled", "Faceless", "Famed", "Famous", "Favoured", "Fervent", "Flawless", "Green", "Grey", "Guardian", "Genious", "Gallant", "Great", "Grand", "Gifted", "Glorious", "Golden", "Good", "Graceful", "Grandmaster", "Hermit", "Hardened", "Highborn", "Honourable", "Heroic", "Hallowed", "Harmonious", "Hawk-eyed", "Healer", "Herbalist", "Honest", "Inventor", "Indomitable", "Invincible", "Illuminator", "Illusionist", "Ingenius", "Insightful", "Imperial", "Judicious", "Joyous", "Just", "Journeyed", "Jovial", "Jolly", "Jolting", "Keeper", "Knowing", "Knowledgeable", "Kingly", "Leader", "Lucky", "Luckbringer", "Loremaster", "Learned", "Laudable", "Liberator", "Magician", "Magus", "Mystic", "Marvellous", "Mighty", "Mindreader", "Master", "Masterful", "Magnificent", "Mysterious", "Noble", "Nomad", "Nameless", "Naturalist", "Negotiator", "Nice", "Novice", "Oracle", "Orange", "Occultist", "Old", "Obstinate", "Observer", "Omnipotent", "Optimal", "Otherworldly", "Obsessive", "Powerful", "Potent", "Purple", "Pink", "Psychic", "Perceptive", "Pyromancer", "Philosopher", "Peerless", "Quick", "Quick-witted", "Quizzical", "Questioning", "Resolute", "Red", "Runekeeper", "Rover", "Reverent", "Ready", "Rabble-rouser", "Rapturous", "Resplendent", "Researcher", "Redeemer", "Reformer", "Scholar", "Scribe", "Steadfast", "Seer", "Sorcerer", "Summoner", "Sage", "Savant", "Seeker", "Traveller", "Truthseeker", "Trickster", "Transmuter", "Thaumaturge", "Tutor", "Unwavering", "Unyielding", "Unflinching", "Undaunted", "Unfaltering", "Unfearing", "Undying", "Valiant", "Valorous", "Vanquisher", "Venerable", "Veteran", "Vigilant", "Visionary", "Wise", "Wonderer", "Wondrous", "Witty", "Willful", "Wayfarer", "Yellow", "Young", "Youthful", "Zealous", "Zealot"]

counter = 10

while counter > 0:
    # Forename Prefix choices
    p_start = choice(start_cons)
    p_mid = choice(vowel) + choice(p_mid_cons)
    p_end = choice(vowel)
    
    # Concatenate Prefix
    num = randint(1,2)
    if num == 1:
        prefix = p_mid + p_end
        prefix = prefix.capitalize()
    else:
        prefix = p_start + p_mid + p_end
        prefix = prefix.capitalize()
    
    # Forename Suffix choices
    s_start = choice(s_mid_cons)
    s_mid = choice(vowel)
    s_end = choice(end_cons)
    
    #Choose and Concatenate Suffix
    
    # Medium length suffixes have 33% chance of being selected
    num2 = randint(1,6)
    if num2 == 1 or num2 == 2:
        num3 = randint(1,2)
        if num3 == 1:
            suffix = choice(s_mid_cons) + choice(vowel) + choice(end_cons)
        else:
            suffix = choice(s_mid_cons) + choice(db_vowel) + choice(end_cons)
    
    #Long suffixes have 17% chance of being selected    
    elif num2 == 3:
        num4 = randint(1,1)
        if num4 == 1:
            suffix = choice(s_mid_cons) + choice(vowel) + choice(end_cons) + choice(end_vowel)
        #elif num4 == 2:
            #suffix = choice(s_mid_cons) + choice(vowel) + choice(s_mid_cons) + choice(vowel) + choice(end_cons)
        #elif num4 == 2:
            #suffix = choice(s_mid_cons) + choice(db_vowel) + choice(end_cons) + choice(end_vowel)
        #elif num4 == 5:
            #suffix = choice(s_mid_cons) + choice(db_vowel) + choice(s_mid_cons) + choice(vowel) + choice(end_cons)
        #elif num4 == 4:
            #suffix = suffix = choice(s_mid_cons) + choice(vowel) + choice(end_cons) + choice(db_vowel)
    
    #Short suffix has 50% chance of being selected       
    else:  
        suffix = choice(end_cons)
        
    
    # Concatenate Forename
    forename = prefix + suffix #(s_start + s_mid + s_end)
    
    # Title Select
    letter = forename[0]
    title_list = []
    
    # Append list
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
            
    # Concatenate Name
    wiz_name = forename + " the " + choice(title_list)
    print(wiz_name)
    counter -= 1
