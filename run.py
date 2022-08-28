#Created by Rhys Pegrume

import sys
import os
import time


def game():
    print("""       
                ==================================
                =________WINCHESTER_HOUSE________=
                =____________MYSTERY_____________= 
                ==================================
        

                                                \n""")
    print(r"""\

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
       
def inventory():
    print("##__Inventory__##")
    inventory = []

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
    car = input("=>")
    if car == "1":
        searchCar()
    elif car == "2":
        leaveCar()    

def searchCar():
    print("")


def leaveCar():
    print("")
game()