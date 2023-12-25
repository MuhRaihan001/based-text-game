#This script inspired By: Naruto, Fairy Tail

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
    race_list = ['Human', 'Elf', 'Demon'] #Basic Race
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
        "race": race,
        "userSide": side,
        "money": 1000,
        "weaponName": weaponName,
        "playerHP": 100,
        "dmgBonus": dmgBonus,
        "clan": ''
    }
    with open(database, 'w') as f:
        json.dump(data, f)
    time.sleep(1)
    loadData()

def loadData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race
    with open(database, 'r') as f:
        data = json.load(f)
        if data == {}:
            createAccount()
        else:
            name = data["name"]
            race = data["race"]
            userSide = data["userSide"]
            money = data["money"]
            weaponName = data["weaponName"]
            playerHP = data["playerHP"]
            dmgBonus = data["dmgBonus"]
            clan = data["clan"]
    print("Game loaded.")
    runGame()

def saveData():
    global name, userSide, money, weaponName, playerHP, enemyHP, dmgBonus, clan, race
    data = {
        "name": name,
        "race": race,
        "userSide": userSide,
        "money": money,
        "weaponName": weaponName,
        "playerHP": playerHP,
        "dmgBonus": dmgBonus,
        "clan": clan
    }
    with open(database, 'w') as f:
        json.dump(data, f)

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
    elif races == 'Human':
        print('What??')
        time.sleep(1)
        print('Your Body Feel Stranger Power')
        time.sleep(1)
        race = 'Super Human'
        print('You evolve to super human')
        dmgBonus += random.randint(30, 45)

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
    global dragonSlayerATTACK, race
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
            money += 35
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
            if drop == 10:
                if userSide == 'DragonSlayer':
                    race = 'Dragon' #Rare race
                    print('Your Body Slowly show a scale...')
                    time.sleep(1)
                    print('You become a dragon in human body')
            time.sleep(2)
            runGame()

        time.sleep(2)
        clear()
        print("Enemy Turn")
        time.sleep(2)
        if race == 'Dragon':
            enemyDamage -= random.randint(10, 30) #buff damage
            enemyHP -= random.randint(10, 15)
            print('Your enemy has hit by Dragon Full Counter that make them feel pain in theur own attack')
            time.sleep(1)
        showDamage(enemyDamage)
        playerHP -= enemyDamage
        if race == 'Demon':
            playerHP += random.randint(5, 25) #buff life steal
            print('Demon Race Buff your hp increase')
            time.sleep(1)
        if race == 'High Demon':
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
        runGame()


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
        runGame()
    else:
        playerHP = 100
        print("done +100Hp")
        money -= 5
        time.sleep(2)
        print("")
        runGame()


def runGame():
    global enemyHP
    global playerHP
    global villainEnemy
    global knightEnemy
    global ninjaEnemy
    global dragonSlayerEnemy
    global weaponName
    global dmgBonus, race
    clear()
    if userSide == "Ninja":
        print("Hello", clan, name)
    if userSide != "Ninja":
        print("Hello", name)
    print(f'Your Race: {race}')
    print("This Is Your Stats:")
    print("Health:", playerHP, "Dracon:", money, "\tWeapon:", weaponName,
          "\tHealthPoin:", playerHP, "\nDamageBonus:", dmgBonus, "Role:",
          userSide)
    print("1.Search Enemy\n2.Hospital\n3.Shop\n4.Exit")
    select = input("")
    if select == "1":
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
        time.sleep(2)
        enemyHP = 100
        foundEnemy()
    elif select == "3":
        showShopMenu()
    elif select == "2":
        hospitalMenu()
    elif select == "4":
        saveData()
        time.sleep(1)
        exit()


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
loadData()