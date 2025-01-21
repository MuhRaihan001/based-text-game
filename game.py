import time
import random
import os
import json
import string

name = ''
race = 'unknown'
userSide = "Citizen"

database = 'database/data.json'

#main stat
money = 35
weaponName = "knife"
playerHP = 100
enemyHP = 100
dmgBonus = 0
playerDamage = random.randint(1, 25)
enemyDamage = random.randint(1, 25)
clan = ""
dungeon = False
kill = 0
dragonKill = 0
title = ""
inCity = False
inSea = False
enemyDragon = False
Admin = False

#side enemy
villainEnemy = ["Knight", "King", "Bounty Hunter", "DragonSlayer", "DevilKing"]

knightEnemy = [
    "Skeleton", "Dragon", "Treasure Hunter", "DragonSlayer", "Devil King"
]

ninjaEnemy = [
    "Fugutive", "Swordman", "Daimyo BodyGuard", "Dragon", "DragonSlayer"
]

ninjaJutsu = [
    "Katon", "Shadow Clone", "Suiton", "Chidori", "Rasengan", "Doton", "Fuin",
    "Mokuton", "Kemuri", "RaiKiri", "Amaterasu"
]

dragonSlayerEnemy = [
    "Fire Dragon", "Knight", "Main Villain", "Ninja", "Guild Member",
    "Master Guild", "Samurai", 'Wind Dragon', 'Lighthing Dragon', 'Dragon King'
]

dragonSlayerATTACK = [
    "Dragon Roar", "Dragon Punch", "Dragon Cry", "Dragon E.N.D",
    "Dragon Force", "Dragon Wing", "Dragon Drill", "Dragon Giga Drill"
]

divineAttack = [
    "Divine Blast", "Divine Fire", "Holy Punisment", "Divine Jail"
]

samuraiEnemy = [
    "Ninja", "Knight", "Ronin", "Another Samurai", "DragonSlayer"
]

roninEnemy = [
    "Samurai", "Knight", "Ninja", "DragonSlayer", "Another Ronin"
]

#race definition
dangerous_race = ["Leviathan", "Demon", "High Demon", "Sea Beast", "Dragon"]
normal_race = ["Human", "Elf", "Super Human", "Angel", "Spirit"]

#side Definition
dangerous_side = ["DragonSlayer", "Villain", "Ronin"]
normal_side = ["Ninja", "Knight", "Samurai"]

#function
def sendMessage(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()  

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")

def LoadAdmins():
    global name, Admin
    with open('database/admin.json', 'r') as f:
        admin = json.load(f)
        if name in admin['admins']:
            print('You login as admin')
            Admin = True
            time.sleep(1)

def createAccount():
    global dmgBonus, weaponName
    name = input('Enter your name: ')
    
    list_side = ['Knight', 'Ninja', 'Villain', 'DragonSlayer', 'Samurai', 'Ronin']
    race_list = ['Human', 'Elf', 'Demon', 'Fishman']
    
    race, side = random.choice(race_list), random.choice(list_side)
    
    if side == "DragonSlayer":
        weaponName, dmgBonus = "DragonArt", dmgBonus + 35
    elif side in ["Ronin", "Samurai"]:
        weaponName, dmgBonus = "Katana", dmgBonus + 15
    elif side == 'Ninja':
        weaponName, dmgBonus = "Shuriken", dmgBonus + 15
        getRandomClan()
    if race == 'Demon':
        dmgBonus += 5

    print(f'Your race is: {race}')
    time.sleep(1)
    sendMessage(f'Your role is {side}')
    
    data = {
        "name": name, "current_title": '', "race": race, "userSide": side,
        "kill": 0, "money": 15, "weaponName": weaponName, "playerHP": 100,
        "dmgBonus": dmgBonus, "clan": '', "dragonKill": 0
    }
    
    with open(database, 'w') as f:
        json.dump(data, f, indent=4)
    time.sleep(1)
    loadData()

def loadData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race, kill, title, Admin, dragonKill
    with open(database, 'r') as f:
        data = json.load(f)
        if data == {}:
            createAccount()
        else:
            name = data["name"]
            title = data["current_title"]
            race = data["race"]
            userSide = data["userSide"]
            kill = data["kill"]
            money = data["money"]
            weaponName = data["weaponName"]
            playerHP = data["playerHP"]
            dmgBonus = data["dmgBonus"]
            clan = data["clan"]
            dragonKill = data["dragonKill"]
    sendMessage("Game loaded.")
    LoadAdmins()
    if Admin == True:
        title = 'Creator Of World' #Title khusus owner game
        race = 'GOD' #Race khusus owner
    runGame()

def GiveTitle(new_title, description):
    def load_titles():
        with open('database/title.json', 'r') as file:
            return json.load(file)

    def save_titles(titles):
        with open('database/title.json', 'w') as file:
            json.dump(titles, file, indent=4)

    existing_titles = load_titles()
    new_id = str(len(existing_titles))
    existing_titles.append({"id": new_id, "title": new_title, "description": description})
    save_titles(existing_titles)
    print(f'New Title Unlocked: {new_title}')
    time.sleep(1.5)

def load_titles():
    with open('database/title.json', 'r') as file:
        return json.load(file)

def show_titles(titles):
    print("Daftar Titles:")
    for title in titles:
        print(f"ID: {title['id']}, Title: {title['title']}")

def get_title_by_id(titles, title_id):
    for title in titles:
        if int(title['id']) == title_id:
            return title['title']
    return None

def choose_title():
    existing_titles = load_titles()
    show_titles(existing_titles)
    
    chosen_title_id = None
    while chosen_title_id is None:
        try:
            chosen_title_id = int(input("Input Title ID (Type Exit to exit): "))
            if chosen_title_id not in [int(title['id']) for title in existing_titles]:
                chosen_title_id = None
        except ValueError:
            print("ID harus berupa angka.")
            runGame()
    
    chosen_title = get_title_by_id(existing_titles, chosen_title_id)
    return chosen_title

def saveData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race, kill, title, dragonKill
    data = {
        "name": name,
        "current_title": title,
        "race": race,
        "userSide": userSide,
        "kill": kill,
        "money": money,
        "weaponName": weaponName,
        "playerHP": playerHP,
        "dmgBonus": dmgBonus,
        "clan": clan,
        "dragonKill": dragonKill
    }
    with open(database, 'w') as f:
        json.dump(data, f, indent=4)

def showDamage(dmg):
    global dmgBonus
    
    critical_threshold = dmgBonus * 1.5
    
    Crital = dmgBonus + dmg
    
    if Crital >= critical_threshold:
        print("Crital Hit", Crital)
    else:
        print("Damage", Crital)

def evolveRace(races):
    global race, dmgBonus, weaponName

    evolutions = {
        'Demon': ('High Demonic', 'Demon King', 'Evolve Demon To High Demonic'),
        'Human': ('Super Human', 'Human Weapon', 'Evolve Human Into Super Human', random.randint(30, 45)),
        'Fishman': ('Sea Beast', 'Sea King', 'Evolve Fishman Into Sea Beast'),
        'Sea Beast': ('Leviathan', 'Sea God', 'Unlock Leviathan Race'),
        'Super Human': ('Angel', 'Sky God', 'Unlock Angel Race', 'Divine Energy'),
    }

    if races not in evolutions:
        return

    race, title, msg = evolutions[races][:3]
    GiveTitle(title, msg)

    if len(evolutions[races]) > 3:
        bonus_or_weapon = evolutions[races][3]
        if isinstance(bonus_or_weapon, int):
            dmgBonus += bonus_or_weapon
        elif isinstance(bonus_or_weapon, str):
            weaponName = bonus_or_weapon

    special_races = {
        'Sea Beast': ('Leviathan', 'You Evolve to Leviathan beside Dragon!!!', 'Sea God', 'Unlock Leviathan Race'),
        'Super Human': ('Angel', 'You Evolve to Angel beside Dragon!!!', 'Sky God', 'Unlock Angel Race'),
        'Dragon': ('Dragon', 'You Evolve to Dragon!!!', 'Sky King', 'Unlock Dragon Race')
    }

    if race in special_races:
        new_race, message, title, unlock_msg = special_races[race]
        sendMessage(f"What??? You turn into another creature???")
        time.sleep(1)
        sendMessage(message)
        race = new_race
        weaponName = 'Divine Energy' if race == 'Angel' else weaponName
        GiveTitle(title, unlock_msg)
        time.sleep(1)
        runGame()

    time.sleep(1)
    runGame()

def foundEnemy(where):
    global enemyHP
    global playerHP
    if enemyHP < 0:
        enemyHP = 0
    if playerHP < 0:
        playerHP = 0

    print("Player Health", playerHP, "enemy Health", enemyHP)
    print("")
    time.sleep(1)
    print("Select your choice")
    print("1.Attack\t\t2.Run")
    choice = input("")
    if choice == "1":
        attackEnemy(1, where)
    elif choice == "2":
        attackEnemy(2, where)


def attackEnemy(choice, location=''):
    clear()

    global playerHP, enemyHP, money, dmgBonus
    global playerDamage, enemyDamage, ninjaJutsu
    global weaponName, dragonSlayerATTACK, race
    global divineAttack, kill, inCity, inSea, dungeon

    playerDamage = random.randint(1, 25)
    enemyDamage = random.randint(1, 25)

    buffs = {
        'Fishman': {'playerDamage': 25, 'enemyDamage': -5, 'inSea': True},
        'Sea Beast': {'playerDamage': 20, 'enemyDamage': -10, 'inSea': True},
        'Leviathan': {'playerDamage': 30, 'enemyDamage': -8, 'inSea': True},
        
        'Demon': {'playerDamage': 15, 'enemyDamage': -5, 'inDungeon': True},
        'High Demon': {'playerDamage': 25, 'enemyDamage': -10, 'inDungeon': True},
    }
    if inSea and race in buffs and 'inSea' in buffs[race]:
        playerDamage += buffs[race]['playerDamage']
        enemyDamage += buffs[race]['enemyDamage']
    
    elif dungeon and race in buffs and 'inDungeon' in buffs[race]:
        playerDamage += buffs[race]['playerDamage']
        enemyDamage += buffs[race]['enemyDamage']


    if choice == 1:
        if userSide == "Ninja" and weaponName == "Jutsu":
            jutsu = random.choice(ninjaJutsu)
            print(f"You attack enemy using {jutsu}, {weaponName}")
        elif userSide == "DragonSlayer":
            dragonArt = random.choice(dragonSlayerATTACK)
            print(f"You attack enemy using {dragonArt}")
        elif race == "Angel":
            divine = random.choice(divineAttack)
            print(f"You attack enemy using {divine}")
        else:
            print(f"You attack enemy using {weaponName}")

        time.sleep(1)
        totalDamage = playerDamage + dmgBonus
        sendMessage("You hit the enemy")
        time.sleep(1)
        showDamage(totalDamage)
        enemyHP -= totalDamage

        if enemyHP <= 0:
            handleVictory(location)
        else:
            handleEnemyTurn(location)

    elif choice == 2:
        print("You ran away from the enemy")
        time.sleep(2)
        print("Dracon -5")
        money -= 5
        time.sleep(2)
        Explore()
    else:
        foundEnemy(location)

def handleVictory(location):
    global money, kill, race, dragonKill, enemyDragon

    print("You win")
    time.sleep(1)
    print("Dracon +35")
    money += 35
    kill += 1
    if enemyDragon:
        dragonKill += 1

    if kill == 500:
        GiveTitle('The Beast', 'Kill 500 Enemy')

    if race == 'Elf':
        sendMessage('Elf Race bonus, prize increased')
        money += random.randint(5, 25)

    drop = random.randint(1, 100)
    if race == 'Elf':
        drop = 10

    if race in ['Demon', 'Human', 'Fishman'] and drop in [5, 2, 25]:
        evolveRace(race)

    if dragonKill >= 80 and userSide == 'DragonSlayer':
        sendMessage('Your body slowly shows scales...')
        time.sleep(1)
        sendMessage(f'You became a dragon in {race} body')
        race = 'Dragon'

    time.sleep(2)

    if inCity:
        handleCitySituation(location)
    elif inSea:
        exploreSea()
    else:
        Explore()

def handleEnemyTurn(location):
    global playerHP, enemyDamage, enemyHP, race, dungeon

    time.sleep(2)
    clear()
    print("Enemy Turn")
    time.sleep(2)

    if race == 'Dragon':
        enemyDamage = max(0, enemyDamage - random.randint(10, 30))
        enemyHP -= random.randint(10, 15)
        sendMessage('Dragon Full Counter activated, reflecting some damage back to the enemy')

    if race != 'Spirit':
        enemyDamage = max(0, enemyDamage - random.randint(5, 15))  # race spirit immune to any attack
    elif race == 'Spirit' and dungeon:
        enemyDamage = max(0, enemyDamage - random.randint(5, 15))  # race spirit will take damage in dungeon

    showDamage(enemyDamage)

    life_steal = random.randint(15, 30)
    if race == 'Demon' or race == 'High Demon':
        playerHP += life_steal
        enemyHP -= life_steal
        sendMessage('Demon Race Buff: Life steal activated')
    
    if playerHP <= 0:
        handleDefeat(location)
    elif enemyHP <= 0:
        handleVictory(location)
    else:
        foundEnemy(location)

def handleDefeat(location):
    global playerHP, money, race

    spiritRaceDrop = random.randint(1, 100)

    if race == 'Angel':
        playerHP = 100
        sendMessage('Angel Race Buff: You resurrected')
        time.sleep(1)
        foundEnemy(location)
        return
    elif race == 'Human' and spiritRaceDrop <= 45:
        sendMessage('You died, but your spirit is still strong')
        sendMessage('Your body slowly glow and fade but your spirit remains')
        sendMessage('You unlock new race: Spirit you are visible to NPC')
        race = 'Spirit'
        time.sleep(1)
        playerHP = 100
        runGame()
        return

    print("You lose")
    time.sleep(1)
    print("Dracon -20")
    money -= 20
    time.sleep(1)
    hospitalMenu()

def handleCitySituation(location):
    global userSide, race
    if userSide in dangerous_side or race in dangerous_race:
        sendMessage('Your attack caused destruction, and citizens noticed you as a Dragon Slayer')
        time.sleep(1)
        sendMessage('The citizens kicked you out of the city')
        global inCity
        inCity = False
        time.sleep(1)
        ExploreCity(location)
    else:
        sendMessage("The citizen appreciate your help and the store owner give you some Dracon")
        time.sleep(1)
        money += 100

def showShopMenu(shop_name=''):
    clear()
    if userSide == "DragonSlayer":
        sendMessage("No shop accepts you")
        time.sleep(3)
        runGame()
        return

    sendMessage(f'Welcome To {shop_name} Shop')

    if userSide == "Ninja":
        print("1. Shuriken (25$)\n2. Kunai (15$)\n3. Jutsu (35$)")
        ninjaSelect = input("")
        if ninjaSelect in ["1", "2", "3"]:
            buyNinjaWeapon(int(ninjaSelect))

    if userSide == "Ronin" or userSide == "Samurai":
        print("1. Katana (15$)\n2. Wakizashi (10$)\n3. Tanto (500)")
        samuraiSelect = input("")
        if samuraiSelect in ["1", "2", "3"]:
            buySamuraiWeapon(int(samuraiSelect))

    else:
        print("1. Excalibur (50$)\n2. Diamond Katana (15$)\n3. Durendal (25$)\n4. Yoru (100$)")
        select = input("")
        if select in ["1", "2", "3", "4"]:
            buyWeapon(int(select))

def buySamuraiWeapon(wp):
    clear()
    global weaponName, dmgBonus, money

    weapons = {
        1: ("Katana", 15, 15),
        2: ("Wakizashi", 10, 10),
        3: ("Tanto", 500, 35)
    }

    weaponName, cost, bonus = weapons[wp]

    if money < cost:
        sendMessage(f"You need {cost} Dracon to buy this weapon")
        time.sleep(1)
    else:
        money -= cost
        dmgBonus = bonus

    runGame()

def buyNinjaWeapon(wp):
    clear()
    global weaponName, dmgBonus, money

    weapons = {
        1: ("Shuriken", 25, 15),
        2: ("Kunai", 15, 10),
        3: ("Jutsu", 35, 25)
    }

    weaponName, cost, bonus = weapons[wp]

    if money < cost:
        sendMessage(f"You need {cost} Dracon to buy this weapon")
        time.sleep(1)
    else:
        money -= cost
        dmgBonus = bonus

    runGame()

def buyWeapon(wp):
    clear()
    global weaponName, dmgBonus, money

    weapons = {
        1: ("Excalibur", 50, 35),
        2: ("Diamond Katana", 15, 15),
        3: ("Durendal", 25, 25),
        4: ("Yoru", 100, 65)
    }

    weaponName, cost, bonus = weapons[wp]

    if money < cost:
        sendMessage(f"You need {cost} Dracon to buy this weapon")
        time.sleep(2)
    else:
        money -= cost
        dmgBonus = bonus

def hospitalMenu():
    global money
    global playerHP
    if money < 5 and playerHP > 0:
        sendMessage("tou need 5 Dracon")
        time.sleep(2)
        print("")
    else:
        playerHP = 100
        sendMessage("done +100Hp")
        money -= 5
        time.sleep(2)
        print("")
    runGame()

def GenerateCity():
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    
    random.seed()
    
    city_name = random.choice(string.ascii_uppercase)
    
    for i in range(random.randint(2, 4)):
        if i % 2 == 0:
            city_name += random.choice(consonants)
        else:
            city_name += random.choice(vowels)
    
    return city_name

def exploreSea():
    global enemyHP, inSea
    if not inSea:
        return

    print('1.Forward\n2.Back\n3.Left\n4.Right\n')
    way = int(input())

    if way not in [1, 2, 3, 4]:
        return exploreSea()

    sea_event = ["Nothing", "Pirate", "Sea Beast", "Kraken", "City"]
    event = random.choice(sea_event)
    
    if event == "Nothing":
        sendMessage('You found an endless sea')
        time.sleep(1)
        return exploreSea()
    
    if event == "City":
        city_name = GenerateCity()
        sendMessage(f'You found {city_name}')
        time.sleep(1)
        inSea = False
        return ExploreCity()

    enemies = {
        "Pirate": 250,
        "Sea Beast": 500,
        "Kraken": 1000
    }

    if event in enemies:
        enemyHP = enemies[event]
        sendMessage(f'You attacked by {event}')
        foundEnemy(event)


def ExploreCity(city_name):
    clear()
    global money, race, inCity, enemyHP, dangerous_race, dangerous_side
    inCity = True
    print(f"You are at {city_name} city\nWhat would you like to explore?")
    print('1.Forward\n2.Back\n3.Left\n4.Right\n5.Stop')
    way = input()
    if way == '5':
        inCity = False
        Explore()
    elif way == '1' or way == '2' or way == '3' or way == '4':
        city_event = ['Concert', 'Kind', 'Robbery', 'Harbor']
        event = random.choice(city_event)
        if event == 'Concert':
            sendMessage('You foun a concert and decided to watch')
            time.sleep(1)
            if race in dangerous_race or userSide in dangerous_side:
                sendMessage('The concert is canceled because of you')
                time.sleep(1)
                sendMessage('The citizen kicked you out of the city')
                inCity = False
                ExploreCity()

            money -= 5
            sendMessage('You lose 5 Dracon')
            ExploreCity(city_name)
        elif event == 'Kind':
            sendMessage('A kind person give you money')
            time.sleep(1)
            money += random.randint(1, 20)
            if race == 'Elf':
                money += random.randint(1, 20)
                sendMessage('Elf Race buff, increse money')
            time.sleep(1)
            ExploreCity(city_name)
        elif event == 'Robbery':
            sendMessage('You see a store was robbed by someone')
            enemyHP = 100
            foundEnemy(city_name)
        elif event == 'Harbor':
            sendMessage('You see a harbor and decided to go there')
            time.sleep(1)
            action = int(input("1.Explore the sea\t2. Continue Explore City"))
            if action == 1:
                inSea = True
                inCity = False
                exploreSea()
            if action == 2:
                exploreCity(city_name)
    else:
        ExploreCity(city_name)

def Explore():
    global money, race, userSide, enemyHP, dungeon
    clear()
    
    if dungeon:
        sendMessage('Select your way to explore this dungeon')
    else:
        print('Select Your Way to Explore')
    
    print('1.Forward\n2.Back\n3.Left\n4.Right\n5.Stop')
    way = input()

    if way == '5':
        if inDungeon:
            inDungeon = False
            Explore()
        else:
            runGame()

    if dungeon:
        dungeon_monster = ['Goblin', 'Golem', 'Undead', 'Salamander [BOSS]', 'Giant Golem [BOSS]']
        enemy = random.choice(dungeon_monster)
        if '[BOSS]' in enemy:
            dungeon = False
            enemyHP = 1000
            sendMessage(f'You Found The Boss {enemy}')
            time.sleep(1)
            foundEnemy('Dungeon')
        else:
            sendMessage(f'You attacked by {enemy}')
            enemyHP = 250
            time.sleep(1)
            foundEnemy('Forest')

    elif way in ['1', '2', '3', '4']:
        event = random.choice(['Nothing', 'Treasure', 'Enemy', 'Trap', 'Dungeon', 'City'])
        if event == 'Nothing':
            sendMessage('You found nothing in this way')
        elif event == 'Treasure':
            prize = random.randint(25, 40)
            money += prize
            if race == 'Elf':
                bonus = random.randint(25, 40)
                money += bonus
                sendMessage(f'Elf Race bonus, prize increase more +{bonus}')
            sendMessage(f'You found a treasure +{prize}')
        elif event == 'Trap':
            sendMessage('You fall into a bandit trap')
            if race in dangerous_race:
                sendMessage('The bandit scared of you. Safe!')
            else:
                money -= random.randint(20, 50)
                sendMessage('You lose some money')
        elif event == 'City':
            cityname = GenerateCity()
            sendMessage(f'You arrive at city named: {cityname}')
            ExploreCity(cityname)
        elif event == 'Dungeon':
            sendMessage('You found a dungeon and enter it')
            dungeon = True
        elif event == 'Enemy':
            enemyHP = 100
            enemy_list = {
                "Villain": villainEnemy,
                "Knight": knightEnemy,
                "Ninja": ninjaEnemy,
                "DragonSlayer": dragonSlayerEnemy
            }
            enemy = random.choice(enemy_list[userSide])
            sendMessage(f"Your enemy is: {enemy}")
            if userSide == "DragonSlayer" and "Dragon" in enemy:
                global enemyDragon
                enemyDragon = True
                sendMessage(f"{name}: This time I will stop you!")
                enemyHP = 2000
            time.sleep(2)
            foundEnemy('Forest')
    Explore()


def getRandomClan():
    global clan
    clan_list = ["Uchiha", "Senju", "Hyuga", "Uzumaki", "Kurozawa", "Kaguya", "Satou", "Raijin", "Kurogane", "Kurozawa"]
    clan = random.choice(clan_list)
    time.sleep(1)
    sendMessage(f'Your Clan is {clan}')

#run all script
clear()

def runGame():
    global enemyHP
    global playerHP
    global villainEnemy
    global knightEnemy
    global ninjaEnemy
    global dragonSlayerEnemy
    global weaponName
    global dmgBonus, race, kill, title, damage, money
    clear()

    if userSide == "Ninja":
        print("Hello", clan, name)
    else:
        print(f"Hello [The {title}]" if title else f"Hello {name}")

    print(f'Your Race: {race}')
    print("This Is Your Stats:")
    print(f"Health: {playerHP} Dracon: {money} \tWeapon: {weaponName}")
    print(f"DamageBonus: {dmgBonus} Role: {userSide} Kill: {kill}")
    print("1. Explore\n2. Hospital\n3. Shop\n4. Choose Title\n5. Exit")

    select = input("")
    if select == "1":
        Explore()
    elif select == "3":
        showShopMenu(GenerateCity())
    elif select == "2":
        hospitalMenu()
    elif select == "4":
        title = choose_title()
        print(f'You selected title: {title}')
        time.sleep(1)
        runGame()
    elif select == "5":
        saveData()
        time.sleep(1)
        exit()
    else:
        admin_commands(select)


def admin_commands(command):
    global money, kill, race, userSide, dmgBonus
    if Admin == False:
        runGame()
    if command.startswith('/money'):
        value = command.split()
        if len(value) == 2:
            money += int(value[1])
    elif command.startswith('/kill'):
        value = command.split()
        if len(value) == 2:
            kill += int(value[1])
    elif command.startswith('/race'):
        parts = command.split()
        if len(parts) == 2:
            new_race = parts[1]
            race = new_race
    elif command.startswith('/side'):
        parts = command.split()
        if len(parts) == 2:
            new_side = parts[1]
            userSide = new_side
    elif command.startswith('/bonus'):
        parts = command.split()
        if len(parts) == 2:
            new_bonus = int(parts[1])
            dmgBonus += new_bonus

    runGame()   

loadData()