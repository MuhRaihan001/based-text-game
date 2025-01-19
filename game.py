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
    "Master Guild", "Kurozawa Descendants", 'Wind Dragon', 'Lighthing Dragon', 'Dragon King'
]

dragonSlayerATTACK = [
    "Dragon Roar", "Dragon Punch", "Dragon Cry", "Dragon E.N.D",
    "Dragon Force", "Dragon Wing", "Dragon Drill", "Dragon Giga Drill"
]

divineAttack = [
    "Divine Blast", "Divine Fire", "Holy Punisment", "Divine Jail"
]


#function
def sendMessage(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()  

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")

def SelectTable(init):
    if init == "1":
        foundEnemy()

def LoadAdmins():
    global name, Admin
    with open('database/admin.json', 'r') as f:
        admin = json.load(f)
        if name in admin['admins']:
            print('You login as admin')
            Admin = True
            time.sleep(1)

def createAccount():
    global dmgBonus, userSide
    name = input('Enter your name: ')
    list_side = ['Knight', 'Ninja', 'Villain', 'DragonSlayer']
    race_list = ['Human', 'Elf', 'Demon', 'Fishman'] #Basic Race
    race = random.choice(race_list)
    print('Your race is:', race)
    time.sleep(1)
    weaponName = 'Knife'
    side = random.choice(list_side)
    if side == "DragonSlayer":
        weaponName = "DragonArt"
        dmgBonus += 35
    if race == 'Demon':
        dmgBonus += 5
    time.sleep(1)
    sendMessage(f'Your role is {side}')

    if side == 'Ninja':
        weaponName = 'Shuriken'
        dmgBonus += 15
        getRandomClan()

    data = {
        "name": name,
        "current_title": '',
        "race": race,
        "userSide": side,
        "kill": 0,
        "money": 1000,
        "weaponName": weaponName,
        "playerHP": 100,
        "dmgBonus": dmgBonus,
        "clan": '',
        "dragonKill": 0
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
    if dmg > 20:
        print("Crital Hit", dmg)
    elif dmg < 20:
        print("Damage", dmg)

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
    global playerHP, enemyDamage

    time.sleep(2)
    clear()
    print("Enemy Turn")
    time.sleep(2)

    if race == 'Dragon':
        enemyDamage = max(0, enemyDamage - random.randint(10, 30))
        enemyHP -= random.randint(10, 15)
        sendMessage('Dragon Full Counter activated, reflecting some damage back to the enemy')

    playerHP -= enemyDamage
    showDamage(enemyDamage)

    if race == 'Demon':
        playerHP += random.randint(5, 25)
        sendMessage('Demon Race Buff: Life steal activated')
    elif race == 'High Demon':
        playerHP += random.randint(5, 25)
        enemyHP -= random.randint(10, 60)
        sendMessage('High Demon used Demonic Lifesteal')

    if playerHP <= 0:
        handleDefeat(location)
    else:
        foundEnemy(location)

def handleDefeat(location):
    global playerHP, money

    if race == 'Angel':
        playerHP = 100
        sendMessage('Angel Race Buff: You resurrected')
        time.sleep(1)
        foundEnemy(location)
        return

    print("You lose")
    time.sleep(1)
    print("Dracon -20")
    money -= 20
    time.sleep(1)
    hospitalMenu()

def handleCitySituation(location):
    global userSide, race
    if userSide == 'DragonSlayer' or race == 'Demon':
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

def showShopMenu(shop_name = ''):
    clear()
    if userSide == "DragonSlayer":
        sendMessage("No shop accepts you")
        time.sleep(3)
        runGame()
    sendMessage(f'Welcome T0 {shop_name} Shop')
    if userSide == "Ninja":
        print("1.Shuriken(25$)\n2.Kunai(15$)\n3.Jutsu(35$)")
        ninjaSelect = input("")
        if ninjaSelect == "1":
            buyNinjaWeapon(1)
        elif ninjaSelect == "2":
            buyNinjaWeapon(2)
        elif ninjaSelect == "3":
            buyNinjaWeapon(3)

    elif userSide != "Ninja":
        print(
            "1.Excalibur (50$)\n2.Diamond Katana(15$)\n3.Durendal(25$)\n4.Yoru(100$)"
        )
        select = input("")
        if select == "1":
            buyWeapon(1)
        elif select == "2":
            buyWeapon(2)
        elif select == "3":
            buyWeapon(3)
        elif select == "4":
            buyWeapon(4)


def buyNinjaWeapon(wp):
    clear()
    global weaponName
    global dmgBonus
    global money
    if wp == 1:
        if money < 25:
            sendMessage("You need 25 Dracon For Buy This Weapon")
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 25
            weaponName = "Shuriken"
            dmgBonus = 15
            runGame()
    if wp == 2:
        if money < 15:
            sendMessage("You need 15 Dracon For Buy This Weapon")
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 15
            weaponName = "Kunai"
            dmgBonus = 10
            runGame()
    if wp == 3:
        if money < 35:
            sendMessage("You need 35 Dracon For Buy This Weapon")
            time.sleep(1)
            runGame()
        else:
            dmgBonus = 0
            money -= 35
            weaponName = "Jutsu"
            dmgBonus = 25
            runGame()


def buyWeapon(wp):
    clear()
    global weaponName
    global dmgBonus
    global money
    if wp == 1:
        if money < 50:
            sendMessage("You Need 25 Dracon For buuy This Weapon")
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "excalibur"
            dmgBonus += 35
            money -= 50
            runGame()
    if wp == 2:
        if money < 15:
            sendMessage("You Need 25 Dracon For buuy This Weapon")
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "DiamondKatana"
            dmgBonus += 15
            money -= 50
            runGame()
    if wp == 3:
        if money < 25:
            sendMessage("You Need 25 Dracon For buuy This Weapon")
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Durendal"
            dmgBonus += 25
            money -= 25
            runGame()
    if wp == 4:
        if money < 100:
            sendMessage("You Need 100 Dracon For Buy This Weapon")
            time.sleep(2)
            runGame()
        else:
            dmgBonus = 0
            weaponName = "Yoru"
            dmgBonus += 65
            money -= 100
            runGame()


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
    if inSea:
        print('1.Forward\n2.Back\n3.Left\n4.Right\n')
        way = int(input())
        
        if way == '1' or way == '2' or way == '3' or way == '4':
            sea_event = ["Nothing", "Pirate", "Sea Beast", "Kraken", "City"]
            event = random.choice(sea_event)
            if event == "Pirate":
                enemyHP = 250
                sendMessage(f'You attacked by Pirate Group')
                foundEnemy('Pirate')
            elif event == "Sea Beast":
                enemyHP = 500
                sendMessage(f'You attacked by Sea Beast')
                foundEnemy('Sea Beast')
            elif event == "Kraken":
                enemyHP = 1000
                sendMessage(f'You attacked by Kraken')
                foundEnemy('Kraken')
            elif event == "Nothing":
                sendMessage('You found an endless sea')
                time.sleep(1)
                exploreSea()
            elif event == "City":
                city_name = GenerateCity()
                sendMessage(f'You found {city_name}')
                time.sleep(1)
                inSea = False
                ExploreCity()
        else:
            exploreSea()

def ExploreCity(city_name):
    clear()
    global money, race, inCity, enemyHP
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
            money -= 5
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
    if dungeon == True:
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

    if dungeon == True: #Dungeon monsters stronger than normal monsters
        dungeon_monster = ['Goblin', 'Golem', 'Undead', 'Salamander [BOSS]', 'Giant Golem [BOSS]']
        enemy = random.choice(dungeon_monster)
        if enemy.endswith('[BOSS]'):
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
    elif way == '1' or way == '2' or way == '3' or way == '4':
        list_event = ['Nothing', 'Treasure', 'Enemy', 'Trap', 'Dungeon', 'City']
        event = random.choice(list_event)
        if event == 'Nothing':
            sendMessage('You found nothing in this way')
            time.sleep(1)
            Explore()
        elif event == 'Treasure':
            sendMessage('You Found a treasure')
            prize = random.randint(25, 40)
            money += prize
            sendMessage(f'money +{prize}')
            if race == 'Elf':
                prize = random.randint(25, 40) #Elf race buff
                money += prize
                sendMessage(f'Elf Race bonus, prize increase more +{prize}')
            Explore()
        elif event == 'Trap':
            sendMessage('You fall into bandit trap')
            time.sleep(1)
            if race == 'Demon' or race == 'Dragon' or race == 'High Demonic' or userSide == 'DragonSlayer':
                sendMessage('The bandit scare of you')
                sendMessage('Safe')
                time.sleep(1)
                Explore()
            else:
                money -= random.randint(20, 50)
                sendMessage('You lose some money')
                time.sleep(1)
                Explore()
        elif event == 'City':
            cityname = GenerateCity()
            sendMessage(f'You arrive at city named: {cityname}')
            time.sleep(1)
            ExploreCity(cityname)
        elif event == 'Dungeon':
            sendMessage('You found an dungeon and enter it')
            time.sleep(1)
            dungeon = True
            time.sleep(1)
            Explore()
        elif event == 'Enemy':
            enemyHP = 100
            if userSide == "Villain":
                tekiDa = random.choice(villainEnemy)
                sendMessage(f"Your Enemy Is: {tekiDa}")
            if userSide == "Knight":
                enemyK = random.choice(knightEnemy)
                sendMessage(f"Your Enemy Is: {enemyK}")
            if userSide == "Ninja":
                enemyN = random.choice(ninjaEnemy)
                sendMessage(f"Your Enemy Is {enemyN}")
            if userSide == "DragonSlayer":
                Denemy = random.choice(dragonSlayerEnemy)
                sendMessage(f"You enemy is {Denemy}")
                if Denemy.endswith("Dragon") or Denemy.startswith("Dragon"):
                    global enemyDragon
                    enemyDragon = True
                    sendMessage(name + ": This time i will stop you")
                    enemyHP = 2000
            time.sleep(2)
            foundEnemy('Forest')
    else:
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
    if userSide != "Ninja":
        if title != "":
            print(f"Hello [The {title}]", name)
        else:
            print(f"Hello {name}")
    print(f'Your Race: {race}')
    print("This Is Your Stats:")
    print("Health:", playerHP, "Dracon:", money, "\tWeapon:", weaponName,
          "\tHealthPoin:", playerHP, "\nDamageBonus:", dmgBonus, "Role:",
          userSide, 'Kill:', kill)
    print("1.Explore\n2.Hospital\n3.Shop\n4.Choose Title\n5.Exit")
    select = input("")
    if select == "1":
        Explore()
    elif select == "3":
        showShopMenu()
    elif select == "2":
        hospitalMenu()
    elif select == "4":
        selected_title = choose_title()
        title = selected_title
        print(f'You use Selected title, {selected_title}')
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