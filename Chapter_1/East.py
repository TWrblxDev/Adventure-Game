import os 
import time
import Blaster_Pistol
import Game_Time
import keyboard
import sys
import Chapter_1.East
import Chapter_1.North
import Chapter_2.Chapter2
import inv.inv
import random
import items.ammo
import items.food
import items.dollar
import simple_colors
import items.power
import debug.debug
import time
import os
import Chapter_1.West
import Chapter_1.North
import random
import inv.inv
import simple_colors

dollar = 20

PlayerHealth = 100
EnemyHealth = 20
EnemyDamage = 20

bossnames = ["Mutated Bear", "Mutated Lion"]


def East():
    clear = lambda: os.system('clear')
    print("You chose East")

    ch1_east = input(
        "You dicide that going towards the zombies is a good idea. after 3 hours of walking you stop to take a break near Ottawa"
    )
    clear()
    food = 20
    dollar = 20
    ammo = 10
    food = food - 1
    print("Food", food)
    print("You here rustling in the bushes nearby your camp.")
    print("before you can do anything, a Zombie stumbles out of the bushes")
    print("Bill says'Battle time'")
    print("you can chose 2 options. attack, or heal.")
    input(
        "Bill says' this is a turtorial battle. the battles will get harder. Good Luck'"
    )

    #Battle
    def battle():
        import time
        EnemyHealth = 100
        PlayerHealth = 50
        ClearLoop = 80

        print("fight starting")
        time.sleep(1)
        print("...")
        time.sleep(3)
        print("ready?")
        time.sleep(2)
        print("fight!")
        time.sleep(1)
        while EnemyHealth > int(0):
            while ClearLoop > int(0):
                print(" ")
                ClearLoop = (ClearLoop - 1)

            if PlayerHealth < int(1):
                print("You Died! Restart The Game To Replay")
                exit()

                for names in bossnames:
                     print(names, simple_colors.red("Health = ", EnemyHealth))
            time.sleep(0.5)
            print("Player Health = ", PlayerHealth)
            time.sleep(0.5)
            print(" ")
            print(
                "type 'attack' to deal damage, type 'heal' to restore health by 30"
            )
            print("mistyping the action will cause you to miss the attack")
            file = input("")

            #Attack
            if file == ("attack" or "Attack"):
                EnemyHealth = (EnemyHealth - 10)
                print(" ")
                print("You attacked, and dealt 10 DMG")
                time.sleep(1)
            #heal
            if file == ("heal" or "Heal"):
                PlayerHealth = (PlayerHealth + 30)
                print(" ")
                print(simple_colors.cyan("You healed yourself for 20 HP"))
                time.sleep(0.5)
            #max health
            if PlayerHealth > int(50):
                PlayerHealth = 50
                print(" ")
                print(simple_colors.red("Max HP reached!"))
                time.sleep(0.5)
            #Enemy attack
            PlayerHealth = (PlayerHealth - 10)
            print(" ")
            for names in bossnames:
                 print(names, simple_colors.red(" attacked you, dealing 10 DMG"))
            file = ("")
            time.sleep(1)
            ClearLoop = 80
        #If you won battle
        dollar = 20
        print(" ")
        print("You won the fight!")
        print(" ")
        print("+5 Dollars")
        dollar = dollar + 5
        print("You have $", dollar)

    battle()   #delete this line here temporarily (line 94) to skip battle. if you forgot what goes here. this is the command:   battle()    don't forget indent

    input(
        "Bill says 'nice job. you have killed your first enemy. you realize that your gun is not out of ammo. each battle will reduce your ammo by ten. "
    )
    ammo = 10
    ammo = ammo - 10
    print("Ammo:", ammo)

    #go West or East
    ch1 = input("Do you want to go West or continue going East")

    #West
    if ch1.lower() == "west":
        Chapter_1.West.West()
    #East
    elif ch1.lower() == "east":

        print("You decide to continue going East")
        input(
            "as you continue your trek along the road you encounter a person that tells you there is an inn 5 miles away."
        )
        input(
            "on your way to the inn you decide that you need more ammo but you only have $25. you most likely only have enough to get a room for the night and enough to get one special item"
        )
        print("Walking...")
        time.sleep(3)
        input(
            "5 hours after travelling you arrive in the inn which has a small shop. you go to the shopkeeper and he tells you what is for sale."
        )
        dollar = 25

    clear()

    #Shop time
    shop = input("Today we have: $20 fro 20 ammo. type ammo to buy")
    if shop := "ammo" or "Ammo" or "AMMO" or "AmmO":
        dollar = dollar - 20
        print("$", dollar)
        ammo = ammo + 20
        print("ammo:", ammo)

    input(
        "you continue going east, but as you continue after some time you realize that you are near Montreal. 'The zombies are in this area' you think"
    )
    i = 3
    while i > 0:
        print(simple_colors.red("setting up camp."))
        time.sleep(1)
        clear()
        print(simple_colors.blue("setting up camp.."))
        time.sleep(1)
        clear()
        print(simple_colors.yellow("setting up camp..."))
        time.sleep(1)
        clear()
        i = i - 1
    print("Camp Setup")
    food = food - 1
    time.sleep(3)
    print(" you decide to set up camp")
    print("Day one is ending")
    print("Your Stats...")
    print("Food:", food)
    print("$", dollar)
    print("Ammo:", ammo)
    time.sleep(3)
    clear()
    print("Day 2 Rises")
    time.sleep(3)
    clear()
    print("You wake up its 8:30 AM in the morning on Tuesday")
    print('Bill says "Good Morning"')
    print("ready to start walking?")
    i = 3
    while i > 0:
        print("walking.")
        time.sleep(1)
        clear()
        print("walking..")
        time.sleep(1)
        clear()
        print("walking...")
        time.sleep(1)
        clear()
        i = i - 1
    print("you are walking East more now passing Montreal")
    battle()  #delete this line to skip battle
    dir = input(
        "There is a path that leads north. There is a path that leads West"
    )
    if dir.lower() == "north":
      Chapter_1.North.North()
      if dir.lower() == "West":
         Chapter_1.West.West()