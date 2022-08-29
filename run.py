

import sys
import os
import time

inventory = []


def game():
    print("""       
                ==================================
                =________WINCHESTER_HOUSE________=
                =____________MYSTERY_____________= 
                ==================================
        

                                                \n""")
    print(r"""

                              _,                _.
                            (  `)            (`  ).
                        .=( ` ,_ `)    .-``(      ).
                        (.__.:-`-_.'   (.,,(.       '`.
                                            `--`--`'`
                                ____.........__H_
                            __/%%%%|%%%%%%%|%%%%\
                        _ ()/%%|:II:|II:::II|:II:|_ _ _
                        |-(()|--|:II:|II:H:II|:II:|-|-|-|
                        `'.'"^  ^` "^ "^|"|^'"' `^`-.^~'
                        Sher^  


                """)
    print("To start game enter y for yes and n for no.")                                         
    start = input("=> ")
    if start == "y":
        clr_terminal()
        introduction()
    if start == "n":
        clr_terminal()
        print("Maybe next time")


def addToInventory(item):
    inventory.append(item)


def clr_terminal():
    """
   Clear screen after each function is declared
    """
    os.system('clear')


def introduction():
    """
    Intro to game with path to the first scene
    """
    print(".         ________________INTRODUCTION____________\n")
    print("""   
            Welcom to the Winchester House Mystery Game!
            This is a text based mystery game. You will need to use text based 
            answers to traverse through the game and solve the mystery.
    """)
    print("""
           ========================================\n
    """)
    # add picture of house here

    print("Are you ready to play y/n")
    scene = input("=>")
    if scene == "y":
        clr_terminal()
        scene1()
        
    if scene == "n":
        clr_terminal()
        game()
        

# First scene
def scene1():
    print("""
    ###______CHAPTER__1____###\n
    You Wake up in a car dazed confused and unsure of where you are.
    There is heavy rain beating the car making it almost impossible
    make out where you are.\n
    you.....


    """)
    print("1 - Search the car..")
    print("2 - leave the the car..")
    print("Select 1/2")
    car = input("=> ")
    if car == "1":
        clr_terminal()
        searchCar()
    elif car == "2":
        clr_terminal()
        leaveCar()    

def searchCar():
    print("You Search the car...")
    print(" Do you open the glove compartment...")
    print("Enter y/n.")
    compartment = input("=> ")
    if compartment == ("y"):
        clr_terminal()
        gloveCompartment()
    elif compartment == ("n"):
        clr_terminal()
        leaveCar()  

def gloveCompartment():
    """
    first location to pick up items
    """
    print("You open the glove compartment and find...\n")
    print("Youn find a phone and torch..\n\n")

    print("Would you like to add these item to your Inventory\n")
    print("Enter y/n")
    item = input("=> ")
    if item == "y":
        clr_terminal()
        print("items added to your inventory")
        addToInventory("phone" "torch")
        print(inventory)
        phone()
    if item == "n":
        clr_terminal()
        leaveCar()
       
#accessing phone
def phone():
    print("You pick up the phone and look intently at it.")
    print("""
    Hoping to jog any memory
    you have of the events that led you here.""")
    print("you go into you your phone and see you have no signal.")
    print("you notice you have two missed calls from James.")
    print("and a message...\n\n")

    print("Options....\n")
    print("1 -Read message ")
    print("2 - Leave car\n\n")
    print("Select option 1 or 2 - \n")
    option = input("=> ")
    if option == "1":
        clr_terminal()
        print("Message from James")
        print("""
        Buddy you got to come check out this house. 
        Its perfect for our next Pod Cast.
        I will send you the address meet me at 
        the Old Winchester House on friday,
        you will not be dissapointed.
        \n\n""")
        print("""
        'I remember now... I was meeting James at the location to
        record an episode of our haunted house pod cast'...\n
        'But how did i get here...'
        """)
        print("Still confused you peer through the windscreen of you car.")
        print("""
        Through the heave rain you can just about make out
        a large house shrouded in darkness.
        """)
        leaveCar()

    if option == "2":
        clr_terminal()
        print("Still confused you peer through the windscreen of you car.")
        print("""
        Through the heave rain you can just about make out
        a large house shrouded in darkness.
        """)
        
        leaveCar()

def leaveCar():
    print("you you push the door open...")
    print("lightning cracks above your head!\n")
    print(" you sheild you face from the stinging rain,")
    print(" and run to the house.\n\n")

    print("Options....\n")
    print("1 - open door")
    print("2 - Look through the window\n\n")

    print("Select Option enter 1 or 2")
    option = input("=> ")
    if option == "1":
        clr_terminal()
        enter_house()
    elif option == "2":
        clr_terminal()
        window()    
    
def enter_house():

def window():

game()
