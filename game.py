#This script inspired By: Naruto, Fairy Tail, One Piece
#Owner: RyuX
#Support: Novi

import time
import random
import os
import json

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
title = ""

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
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return ("   ")

def SelectTable(init):
    if init == "1":
        foundEnemy()

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
    print(f'Your role is {side}')
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
        "clan": ''
    }
    with open(database, 'w') as f:
        json.dump(data, f, indent=4)
    time.sleep(1)
    loadData()

def loadData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race, kill, title
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
    print("Game loaded.")
    if name == 'RyuX':
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
            chosen_title_id = int(input("Input Title ID: "))
            if chosen_title_id not in [int(title['id']) for title in existing_titles]:
                chosen_title_id = None
        except ValueError:
            print("ID harus berupa angka.")
    
    chosen_title = get_title_by_id(existing_titles, chosen_title_id)
    return chosen_title

def saveData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race, kill, title
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
        "clan": clan
    }
    with open(database, 'w') as f:
        json.dump(data, f, indent=4)

def showDamage(dmg):
    if dmg > 20:
        print("Crital Hit", dmg)
    elif dmg < 20:
        print("Damage", dmg)

def evoleRace(races):
    global race, dmgBonus
    if races == 'Demon':
        print('What??')
        time.sleep(1)
        print('Something happened to your body...')
        print('You evolve to higher level of demon. your race now is High Demonic')
        race = 'High Demonic'
        GiveTitle('Demon King', 'Evolve Demon To High Demonic')
    elif races == 'Human':
        print('What??')
        time.sleep(1)
        print('Your Body Feel Stranger Power')
        time.sleep(1)
        race = 'Super Human'
        print('You evolve to super human')
        dmgBonus += random.randint(30, 45)
        GiveTitle('Human Weapon', 'Evolve Human Into Super Human')
    elif race == 'Fishman':
        print('What??')
        time.sleep(1)
        print('Something happened to your body...')
        time.sleep(1)
        print('You evolve to Sea Beast')
        race = 'Sea Beast'
        GiveTitle('Sea King', 'Evolve Fishman Into Sea Beast')
    time.sleep(1)
    runGame()

def foundEnemy():
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
        attackEnemy(1)
    elif choice == "2":
        attackEnemy(2)


def attackEnemy(choised):
    clear()

    global playerHP
    global enemyHP
    global money
    global dmgBonus
    global playerDamage
    global enemyDamage
    global ninjaJutsu
    global weaponName
    global dragonSlayerATTACK, race, divineAttack, kill
    playerDamage = random.randint(1, 25)
    enemyDamage = random.randint(1, 25)
    if choised == 1:

        if userSide == "Ninja":
            if weaponName == "Jutsu":
                jutsu = random.choice(ninjaJutsu)
                print("You attack enemy use", jutsu, weaponName)

        elif userSide == "DragonSlayer":
            dragonArt = random.choice(dragonSlayerATTACK)
            print("You Attack Enemy Use", dragonArt)

        elif race == "Angel":
            divine = random.choice(divineAttack)
            print('You attack your enemy use', divine)

        else:
            print("You attack enemy use", weaponName)

        time.sleep(1)
        totalDamage = playerDamage + dmgBonus
        print("You hit the enemy")
        time.sleep(1)
        showDamage(totalDamage)
        enemyHP -= totalDamage

        if enemyHP <= 0:
            print("you win")
            time.sleep(1)
            print("Dracon +35")
            if kill == 500:
                GiveTitle('The Beast', 'Kill 500 Enemy')
            money += 35
            kill += 1
            if race == 'Elf':
                print('Elf Race bonus, prize increase more')
                money += random.randint(5, 25) #buff 2 times prize
            drop = random.randint(1, 100)
            if race == 'Elf':
                drop = 10
            if race == 'Demon':
                drop = random.randint(1, 100)
                if drop == 5:
                    evoleRace('Demon')
            if race == 'Human':
                drop = random.randint(1, 100)
                if drop == 2:
                    evoleRace('Human')
            if race == 'Fishman':
                drop = random.randint(1, 100)
                if drop == 25:
                    evoleRace('Fishman')

            if drop == 10:
                if userSide == 'DragonSlayer':
                    print('Your Body Slowly show a scale...')
                    time.sleep(1)
                    print(f'You become a dragon in {race} body')
                    if race == 'Sea Beast':
                        print('What??? You turn into another creature???')
                        time.sleep(1)
                        print('You Evolve to Leviathan beside Dragon!!!')
                        race = 'Leviathan'
                        GiveTitle('Sea God', 'Unlock Leviathan Race')
                        time.sleep(1)
                        runGame()
                    if race == 'Super Human': #An super human evolve to dragon will turn player into angel
                        print('What??? You turn into another creature???')
                        time.sleep(1)
                        print('You Evolve to Angel beside Dragon!!!')
                        race = 'Angel'
                        weaponName = 'Divine Energy'
                        GiveTitle('Sky God', 'Unlock Angel Race')
                        time.sleep(1)
                        runGame()
                    race = 'Dragon' #Rare race
                    GiveTitle('Sky King', 'Unlock Dragon Race')
            time.sleep(2)
            Explore()

        time.sleep(2)
        clear()
        print("Enemy Turn")
        time.sleep(2)
        if race == 'Dragon':
            enemyDamage -= random.randint(10, 30) #buff damage
            enemyHP -= random.randint(10, 15)
            print('Your enemy has hit by Dragon Full Counter that make them feel pain in theur own attack')
            time.sleep(1)
        playerHP -= enemyDamage
        showDamage(enemyDamage)
        if race == 'Demon':
            playerHP += random.randint(5, 25) #buff life steal
            print('Demon Race Buff your hp increase')
            time.sleep(1)
        if race == 'High Demon': #buff HighDemonic
            playerHP += random.randint(5, 25)
            enemyHP -= random.randint(10,60)
            print('High Demon use Demonic Lifesteel')
            time.sleep(1)
        if playerHP <= 0:
            print("You Lose")
            time.sleep(3)
            exit()
        foundEnemy()

        if playerHP <= 0:
            if race == 'Angel':
                playerHP = 100
                print('Angel Race Buff: You came back life')
                time.sleep(1)
                foundEnemy()
            print("you lose")
            time.sleep(1)
            print("Dracon -20")
            money -= 20
            time.sleep(1)
            exit()
        foundEnemy()
    if choised == 2:
        print("You run from enemy")
        time.sleep(2)
        print("Dracon -5")
        money -= 5
        time.sleep(2)
        Explore()


def showShopMenu():
    clear()

    if userSide == "Knight":
        print("WELCOME TO ISEKAI STORE")
    elif userSide == "Villain":
        print("WELCOME TO BLACK MARKET")
    elif userSide == "Ninja":
        print("WELCOME TO NINJA SHOP")
    elif userSide == "DragonSlayer":
        print("No shop accepts you")
        time.sleep(3)
        runGame()

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
            "1.Excalibur (50$)\n2.Diamond Katana(15$)\n3.Durendal(25$)\n4.Yoru(100)"
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
            print("You need 25 Dracon For Buy This Weapon")
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
            print("You need 15 Dracon For Buy This Weapon")
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
            print("You need 35 Dracon For Buy This Weapon")
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
            print("You Need 25 Dracon For buuy This Weapon")
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
            print("You Need 25 Dracon For buuy This Weapon")
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
            print("You Need 25 Dracon For buuy This Weapon")
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
            print("You Need 100 Dracon For Buy This Weapon")
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
    if money < 5:
        print("tou need 5 Dracon")
        time.sleep(2)
        print("")
    else:
        playerHP = 100
        print("done +100Hp")
        money -= 5
        time.sleep(2)
        print("")
    runGame()

def Explore():
    global money, race, userSide, enemyHP, dungeon
    clear()
    if dungeon == True:
        print('Select your way to explore this dungeon')
    else:
        print('Select Your Way to Explore')
    print('1.Forward\n2.Back\n3.Left\n4.Right\n5.Stop')
    way = input()
    if way == '5':
        runGame()
    if dungeon == True: #Dungeon monsters stronger than normal monsters
        dungeon_monster = ['Goblin', 'Golem', 'Undead', 'Salamander [BOSS]', 'Giant Golem [BOSS]']
        enemy = random.choice(dungeon_monster)
        if enemy.endswith('[BOSS]'):
            dungeon = False
            enemyHP = 1000
            print(f'You Found The Boss {enemy}')
            time.sleep(1)
            foundEnemy()
        else:
            print(f'You attacked by {enemy}')
            enemyHP = 250
            time.sleep(1)
            foundEnemy()
    else:
        list_event = ['Nothing', 'Treasure', 'Enemy', 'Trap', 'Dungeon']
        event = random.choice(list_event)
        if event == 'Nothing':
            print('You found nothing in this way')
            time.sleep(1)
            Explore()
        elif event == 'Treasure':
            print('You Found a treasure')
            prize = random.randint(25, 40)
            money += prize
            print(f'money +{prize}')
            if race == 'Elf':
                prize = random.randint(25, 40) #Elf race buff
                money += prize
                print(f'Elf Race bonus, prize increase more +{prize}')
            Explore()
        elif event == 'Trap':
            print('You fall into bandit trap')
            time.sleep(1)
            if race == 'Demon' or race == 'Dragon' or race == 'High Demonic' or userSide == 'DragonSlayer':
                print('The bandit scare of you')
                print('Safe')
                time.sleep(1)
                Explore()
            else:
                money -= random.randint(20, 50)
                print('You lose some money')
                time.sleep(1)
                Explore()
        elif event == 'Dungeon':
            print('You found an dungeon and enter it')
            time.sleep(1)
            dungeon = True
            time.sleep(1)
            Explore()
        elif event == 'Enemy':
            enemyHP = 100
            if userSide == "Villain":
                tekiDa = random.choice(villainEnemy)
                print("Your Enemy Is:" + tekiDa)
            if userSide == "Knight":
                enemyK = random.choice(knightEnemy)
                print("Your Enemy Is:" + enemyK)
            if userSide == "Ninja":
                enemyN = random.choice(ninjaEnemy)
                print("Your Enemy Is", enemyN)
            if userSide == "DragonSlayer":
                Denemy = random.choice(dragonSlayerEnemy)
                print("You enemy is", Denemy)
                if Denemy.endswith("Dragon"):
                    print(name + ": This time i will stop you")
                    enemyHP = 2000
            time.sleep(2)
            foundEnemy()


def selectClan(i):
    global clan
    if i == 1:
        clan = "Uciha"
    elif i == 2:
        clan = "Nara"
    elif i == 3:
        clan = "Senju"
    elif i == 4:
        clan = "Uzumaki"
    elif i == 5:
        clan = "Hyuga"


#run all script
clear()
if userSide == "Ninja":
    print("Select Your Clan")
    print("1.Uciha\n2.Nara\n3.Senju\n4.Uzumaki\n5.Hyuga")
    myClan = input("")
    if myClan == "1":
        selectClan(1)
    elif myClan == "2":
        selectClan(2)
    elif myClan == "3":
        selectClan(3)
    elif myClan == "4":
        selectClan(4)
    elif myClan == "5":
        selectClan(5)

def runGame():
    global enemyHP
    global playerHP
    global villainEnemy
    global knightEnemy
    global ninjaEnemy
    global dragonSlayerEnemy
    global weaponName
    global dmgBonus, race, kill, title, damage
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

loadData()