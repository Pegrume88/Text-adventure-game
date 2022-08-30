

import os
import colorama
from colorama import Fore, Back, Style

 #Initialize colorama
colorama.init(autoreset=True)

inventory = []


def game():
    print(Fore.RED + r"""       
                 
░██╗░░░░░░░██╗██╗███╗░░██╗░█████╗░██╗░░██╗███████╗░██████╗████████╗███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║██╔══██╗██║░░██║██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║██║░░╚═╝███████║█████╗░░╚█████╗░░░░██║░░░█████╗░░██████╔╝
░░████╔═████║░██║██║╚████║██║░░██╗██╔══██║██╔══╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║╚█████╔╝██║░░██║███████╗██████╔╝░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

██╗░░██╗░█████╗░██╗░░░██╗░██████╗███████╗
██║░░██║██╔══██╗██║░░░██║██╔════╝██╔════╝
███████║██║░░██║██║░░░██║╚█████╗░█████╗░░
██╔══██║██║░░██║██║░░░██║░╚═══██╗██╔══╝░░
██║░░██║╚█████╔╝╚██████╔╝██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░╚══════╝

░█████╗░███████╗
██╔══██╗██╔════╝
██║░░██║█████╗░░
██║░░██║██╔══╝░░
╚█████╔╝██║░░░░░
░╚════╝░╚═╝░░░░░

███╗░░░███╗██╗░░░██╗░██████╗████████╗███████╗██████╗░██╗░░░██╗
████╗░████║╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗╚██╗░██╔╝
██╔████╔██║░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██████╔╝░╚████╔╝░
██║╚██╔╝██║░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗░░╚██╔╝░░
██║░╚═╝░██║░░░██║░░░██████╔╝░░░██║░░░███████╗██║░░██║░░░██║░░░
╚═╝░░░░░╚═╝░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░
                                                """)
    
    print(Fore.YELLOW + "To start game enter y for yes and n for no.")                                         
    start = input(Fore.YELLOW + "=> ").lower().strip()
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
    scene = input("=>").lower().strip()
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
    car = input("=> ").lower().strip()
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
    compartment = input("=> ").lower().strip()
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
    item = input("=> ").lower().strip()
    if item == "y":
        clr_terminal()
        print("items added to your inventory")
        addToInventory("phone" "torch")
        print(inventory)
        phone()
    if item == "n":
        clr_terminal()
        leaveCar()
       

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
    option = input("=> ").lower().strip()
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
    clr_terminal()

    print("you you push the door open...")
    print("lightning cracks above your head!\n")
    print(" you sheild you face from the stinging rain,")
    print(" and run to the house.\n\n")

    print("Options....\n")
    print("1 - open door")
    print("2 - Look through the window\n\n")

    print("Select Option enter 1 or 2")
    option = input("=> ").lower().strip()
    if option == "1":
        clr_terminal()
        scene2()
    elif option == "2":
        clr_terminal()
        window()    


# begining of chapter 2    
def scene2():
    clr_terminal()
    print(Fore.RED + """
                _________Chapter_2_________ 
    You slowly open the door entering a dimly lit entrance.
    The interior of the house is old with signs of decay.
    You look around squinting in the dim light and see... 
    \n""")
    print(Fore.GREEN + "1 - A hallway straight infront of you.")
    print(Fore.GREEN + "2 - Living Room to your left.")
    print(Fore.GREEN + "3 - A grand stair case leading to the next floor")
    print(Fore.GREEN + "4 - What looks like a study to the right.\n")
    print(Fore.YELLOW + "select where you want to go (1,2,3,4")
    answer = input(Fore.YELLOW + "=>")
    if answer == "1":
        hallway()
    elif answer == "2":
        living_room()
    elif answer == "3":
        stairs()
    elif answer == "4":
        study()            


def hallway():
    clr_terminal()
    print("""
    
    """)
    print(Fore.GREEN + """
    ______Hallway______\n
    You make your way down to the door at the end of the hallway.
    you notice the walls are filled with old portraits and paintings.
    you.....\n\n
    """)
    print("1 - inspect the walls")
    print("2 - carry on to the doorway at the end of the hallway\n\n")
    print("select option (1/2)")
    answer = input("=> ")
    if answer == "1":
        clr_terminal()
        inspect_wall()
    elif answer == "2":
        clr_terminal()
        kitchen()


def inspect_wall():
    print(r"""
    You walk up to a an old black and white picture of what looks like,
    A family standing behind a sculpture of a skull.\n
    There is something very erie about this picture...
    """)
   
    print("You move on to the next the next picture\n")
    print("""
    Thiis seems to be an even even older picture but the similarities
    between the two are uncanny. There is a family standing behind the
    same sulpture of a skull.
    """)
    print(Fore.BLUE + "'This is just getting creepy now.'")
    
    for phone in inventory(items):
        print(Fore.BLUE + "'JAMES!!..JAMES!!...where is this guy.'")
    if phone in inventory == False:
        kitchen() 
        print("You make your way to the room at at the end of the hallway")
    

def kitchen():
    
    print(Fore.RED + """
    _______Kitchen______\n
    You open the door enter what looks a kitchen, all be it missing 
    all the modern appliances you would find in a kitchen today.
    you flick the light switch and the several lights flicker but
    only one turns on. 
    You around the shadow shrouded kitchen and see...

    """)
    print("1 - a Backpack on the floor")
    print("2 - A knife lying on the table")
    print("3 - You return to the entrance\n")
    print("Answer (1,2,3)")
    answer = input("=> ")
    if answer == "1":
        clr_terminal()
        backpack()
    elif answer == "2":
        clr_terminal()
        knife()
    elif answer == "3":
        clr_terminal()
        entrance()        


def knife():

    print("You find a bloody knife jsut laying on the counter top.")
    print("No traces of blood anywhere else in the kitchen")
    print("The hairs on the back of your neck stand up")
    print("A sense of terror washes over you\n\n")

    print("What should you do next?\n")
    print("1 - Check backpack")
    print("2 - head back to entrance\n")
    print("Enter choice (1,2)")
    answer = input("=> ")
    if answer == "1":
        clr_terminal()
        backpack()
    elif answer == "2":
        clr_terminal()
        entrance()
        

def backpack():

    print("You pick up the backpack and empty the contents on the table.")
    print("A voice recorder slams on the table.")
    print(" you pick up the device and press play\n")

    print("James' voice echos out the recorder....")
    print("""
    'I dont know how I found this place or how I got here'..
    'This house must be over 200 yrs old'..
    'Its in remarkebly good condition'

    """)
    print(" A loud BANG!!! shoots out the speaker on the recorder!!")
    print("James calls out 'who's there!!'\n")
    print("""
    you hear what sound like foot steps getting closer closer through
    the recorder....\n
    """)
    print("Then silence followed by an inhuman SCREAM!!\n")
    print("The scream makes you drop the recorder.")
    print(" It smashes into pieces on the hard kitchen floor.\n\n")

    print("What do you do next.....\n")
    print("1 - Inspect Knife")
    print("2 - Leave kitchen\n")
    print("Enter choice (1,2)")
    answer = input("=> ")
    if answer == "1":
        clr_terminal()
        knife()
    elif answer == "2":
        clr_terminal()
        entrance()


def entrance():
    print("")


def living_room():
    print("")


def stairs():
    print("")


def study():
    print("")


def window():
    print("You peer in through the window to see a dimly lit entrance")
    print("You Enter the house")
    scene2()


game()
