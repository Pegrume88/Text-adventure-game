
import os
import colorama
from colorama import Fore, Back, Style
from time import sleep
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
    """Collect items and add to inventory"""
    inventory.append(item)


def input_validation(input_text, valid_values):
    """Input validator to check for valid input values"""
    input_is_valid = False
    while input_is_valid is False:
        value = input(input_text)
        if value in valid_values:
            input_is_valid = True
        else:
            print("Please enter a valid option")
    return value


def clr_terminal():
    """
   Clear screen after each function is declared with a delay of 1 second
    """
    sleep(1)
    os.system('clear')


def introduction():
    """
    Intro to game with path to the first scene
    """

    print("""
       ________________INTRODUCTION____________\n
     Welcome to the Winchester House Mystery Game!
     This is a text based mystery game. You will need to use text based
     answers to traverse through the game and solve the mystery.
    """)
    print("""
           ========================================\n
    """)
    # add picture of house here

    answer = input_validation("Are you ready to play y/n", ["y", "n"])
    if answer == "y":
        clr_terminal()
        scene1()

    if answer == "n":
        clr_terminal()
        game()


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
    answer = input_validation("Select option (1, 2)", ["1", "2"])
    if answer == "1":
        clr_terminal()
        search_car()
    elif answer == "2":
        clr_terminal()
        leave_car()


def search_car():
    print("You Search the car...")
    print(" Do you open the glove compartment...")
    print("Enter y/n.")
    answer = input_validation("=>", ["y", "n"])
    if answer == ("y"):
        clr_terminal()
        glove_compartment()
    elif answer == ("n"):
        clr_terminal()
        leave_car()


def glove_compartment():
    """
    first location to pick up items
    """
    print("You open the glove compartment and find...\n")
    print("Youn find a phone..\n\n")

    print("Would you like to add this item to your Inventory\n")
    print("Enter y/n")
    item = input("=> ").lower().strip()
    if item == "y":
        clr_terminal()
        print("items added to your inventory")
        addToInventory("phone")
        print(inventory)
        phone()
    if item == "n":
        clr_terminal()
        leave_car()


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
    print("Select option (1,2) \n")
    answer = input_validation("=> ", ["1", "2"])
    if answer == "1":
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
        answer = input_validation("Enter 1 to continue", ["1"])
        if answer == "1":
            leave_car()

    if answer == "2":

        print("Still confused you peer through the windscreen of you car.")
        print("""
        Through the heave rain you can just about make out
        a large house shrouded in darkness.
        """)
        answer = input_validation("Enter 1 to continue", ["1"])
        if answer == "1":
            leave_car()


def leave_car():
    clr_terminal()

    print("you you push the door open...")
    print("lightning cracks above your head!\n")
    print(" you sheild you face from the stinging rain,")
    print(" and run to the house.\n\n")

    print("Options....\n")
    print("1 - open door")
    print("2 - Look through the window\n\n")

    print("Select Option enter (1,2)")
    answer = input_validation("=>", ["1", "2"]).strip()
    if answer == "1":
        leave_car()
    if answer == "1":
        clr_terminal()
        scene2()
    elif answer == "2":
        clr_terminal()
        window()


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
    answer = input_validation("=>", ["1", "2", "3", "4"]).strip()
    if answer == "1":
        hallway()
    elif answer == "2":
        living_room()
    elif answer == "3":
        stairs()


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
    answer = input_validation("=>", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        inspect_wall()
    elif answer == "2":
        clr_terminal()
        kitchen()


def inspect_wall():
    print("""
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

    if "phone" in inventory:
        print("You call out")
        print("'JAMES!!..JAMES!!....'")
        print("no reply..'Where is he?'")
        kitchen()
    else:
        print("press 1 to continue")
        answer = input_validation("=>", ["1"]).strip()
        if answer == "1":
            kitchen()


def kitchen():

    clr_terminal()
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
    answer = input_validation("=>", ["1", "2", "3"]).strip()

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

    print("You find a bloody knife just laying on the counter top.")
    print("No traces of blood anywhere in the kitchen")
    print("The hairs on the back of your neck stand up")
    print("A sense of terror washes over you\n\n")

    print("What should you do next?\n")
    print("1 - Check backpack")
    print("2 - head back to entrance\n")
    print("Enter choice (1,2)")
    answer = input_validation("=>", ["1", "2"]).strip()
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
    print("Where would you like to go?\n\n")

    print("1 - living room")

    print("3 - stairs")
    print("4 - Hallway")
    print("5 - kitchen\n")
    print("Enter (1,2,3,4,5)")
    answer = input("=>").strip()
    if answer == "1":
        living_room()

    elif answer == "3":
        stairs()
    elif answer == "4":
        hallway()
    elif answer == "5":
        kitchen()


def living_room():
    """
    Living room sequence
    """
    print("""
    ____Living_Room_______
    You enter the room and notice the embers in the fire place
    are still glowing.The room is shrouded in shadow the feeling
    that something could jump out the many corners of darkness is
    unnerving.\n

    You scan the room...
    """)
    print("what would you like to inspect.\n")
    print("1- Fire place")
    print("2 - Antique Grand clock")#remove

    print("4 - leave room\n")
    print("Please select (1,2,3,4)")
    answer = input_validation("=>", ["1", "2", "3", "4"]).strip()
    if answer == "1":
        fire_place()
    elif answer == "2":
        clock()

    elif answer == "4":
        entrance()


def fire_place():
    print("""
    _____Fire_Place___________________\n
    You cautiously make your way over to teh fire place.
    The warmth coming from the red embers helps,
    settle your nerves.

    You notice something petruding out of the wall
    to the right of the fireplace. It looks like a skull
    coming out of the wall.....
    """)
    print("What do you next?\n")
    print("1 - Place your hand on the skull.")
    print("2 - Antique Grand clock")#remove
    print("4 - leave room\n")
    print("Please select (1,2,3,4)")

    answer = input_validation("=>", ["1", "2", "3", "4"]).strip()
    if answer == "1":
        hidden_room()

    elif answer == "4":
        entrance()


def hidden_room():
    print(r"""
         .AMMMMMMMMMMA.
       .AV. :::.:.:.::MA.
      A' :..        : .:`A
     A'..              . `A.
    A' :.    :::::::::  : :`A
    M  .    :::.:.:.:::  . .M
    M  :   ::.:.....::.:   .M
    V : :.::.:........:.:  :V
   A  A:    ..:...:...:.   A A
  .V  MA:.....:M.::.::. .:AM.M
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A
:M .  .`VMMMMMMV.:A `VMMMMV .:M:
 V.:.  ..`VMMMV.:AM..`VMV' .: V
  V.  .:. .....:AMMA. . .:. .V
   VMM...: ...:.MMMM.: .: MMV
       `VM: . ..M.:M..:::M'
         `M::. .:.... .::M
          M:.  :. .... ..M
          V:  M:. M. :M .V
          `V.:M.. M. :M.V'
    """)
    clr_terminal()

    print("You place you hand on the skull..")
    print("The skull pushes into the back of the wall..")
    print("You hear a loud mechanical sounds coming from the wall.")
    print("........\n")
    print("The wll suddenly opens up revealing a hidden room.\n")
    print("""
    _______Hidden_Room_________
    You step into the in the room. It resembles a small study,
    there are peices of paper scattered around the room. You
    take a closer look at the papers stroon over a small desk
    and notice various sketches of symbols and what look like runes
    and what seems to be a letter\n.
    """)
    print("You search the desk")
    print("Enter 1 to continue")
    answer = input_validation("=>", ["1"]).strip()
    if answer == "1":
        desk()


def desk():
    print("""
    You search the desk and find a small box.
    You open the box and find an old rusty key.
    Something tells you to take the key.
    """)
    answer = input_validation("=>", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        print("item added to your inventory")
        addToInventory("key")
        print(inventory)
        letter()


def letter():
    print("""
    You picj up the letter and attemp to read it in the dimly lit room.\n

    the letter reads:
    'A great evil has been released upon this house,
    beware of GOZO!'
    """)
    print("What do you do next?\n")
    print("1 - enspect the clock")
    print("2 - return to entrance")

    answer = input_validation("=>", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        clock()
    elif answer == "2":
        clr_terminal()
        entrance()


def clock():
    print("You approach the old Atique clock and immediatly notice something weird.")
    print("instead of number there are symbols, you dont recognise.\n")
    print("You hear a noise coming from upstairs!!")
    print("What do you do next?\n")
    print("1 - Go to stair case")
    print("2 - Head back to entrance\n")

    answer = input_validation("=>", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        stairs()
    elif answer == "2":
        clr_terminal()
        entrance()


def stairs():
    print("You make you way to up the elegent stair case.")
    print("You something almost like someone whispered in you ear.")
    print("You pause for a moment to make sense of it.")
    print("Everything goes quiet..Dead silence..")
    print("You make your way up the stairs")
    print("You hear a shuffling noise coming form above you.")
    print("You see a thin ladder leading to what must be the attic\n")

    print("what do you do next?\n")
    print("1 - Go to attic")
    print("2 - Back to entrance")

    answer = input_validation("=>", ["1", "2"]).strip()
    if answer == "1":
        attic()
    elif answer == "2":
        entrance()


def attic():
    if "key" in inventory:
        print("You use the key to open the hatch to the attic.")
        the_end()
    else:
        clr_terminal()
        print("You need a key to open this door")
        entrance()


def window():
    print("You peer in through the window to see a dimly lit entrance")
    print("You Enter the house\n")
    print("press 1 to continue")
    answer = input_validation("=>", ["1"]).strip()

    if answer == "1":
        scene2()


def the_end():
    print("""
_____Chapter_3___________________\n
You climb up the and use a the key to unlock the hatch
leading to the attic.

The room is shrouded in a thick blanket of darkness, apart
from a singular window at the far end of the room.

The air in the room feels charged, almost as if you are
surounded by static electricity.

As your eyes adjust to the darkness you see a silouit of a
figure standing in the corner.

    """)
    if "phone" in inventory:
        print("You grab you phone and turn on the torch.\n")
        print("You see your friend James standing in the corner.\n")
        print("'James..James are you ok'")
        print("'Where are we?.'")
        print("'What is going on?'\n")
        print("You get no response.")
        end_2()
    else:
        print("You walk slowly to the figure in the corner.")
        print("You realize that the figure is your friend James.\n")
        print("'James are you ok'")
        print("'What is going on'")
        end_2()

def end_2():
    clr_terminal()
    print("James turns and looks at you")
    print("He looks different..not himself.\n")
    print("You grab James and shake him..")
    print("He looks at you, almost surprised you see.")
    print("And says..")
    print("'It wont let us leave.'\n")
    print("'Who wont let us leave?'\n")
    print("James raises his hand and point behind you...\n\n")
    print("Enter 1 to continue.")
    answer = input_validation("=>", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        the_demon()


def the_demon():
    print("")

game()
