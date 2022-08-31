import os
import colorama
from colorama import Fore
from time import sleep


inventory = []


def game():
    """Title page"""
    print(Fore.RED + r"""

╭╮╭╮╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃┃┃┃┃┃╱╱╱╱╱╱┃┃╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭╯╱╱╱╱╱╱╱╱╱╭╯╰╮
┃┃┃┃┃┣┳━╮╭━━┫╰━┳━━┳━┻╮╭╋━━┳━╮┃╰━┳━━┳╮╭┳━━┳━━╮╭━━┳╯╰╮╭╮╭┳╮╱╭┳━┻╮╭╋━━┳━┳╮╱╭╮
┃╰╯╰╯┣┫╭╮┫╭━┫╭╮┃┃━┫━━┫┃┃┃━┫╭╯┃╭╮┃╭╮┃┃┃┃━━┫┃━┫┃╭╮┣╮╭╯┃╰╯┃┃╱┃┃━━┫┃┃┃━┫╭┫┃╱┃┃
╰╮╭╮╭┫┃┃┃┃╰━┫┃┃┃┃━╋━━┃╰┫┃━┫┃╱┃┃┃┃╰╯┃╰╯┣━━┃┃━┫┃╰╯┃┃┃╱┃┃┃┃╰━╯┣━━┃╰┫┃━┫┃┃╰━╯┃
╱╰╯╰╯╰┻╯╰┻━━┻╯╰┻━━┻━━┻━┻━━┻╯╱╰╯╰┻━━┻━━┻━━┻━━╯╰━━╯╰╯╱╰┻┻┻━╮╭┻━━┻━┻━━┻╯╰━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╰━━╯
                                                """)

    print(Fore.YELLOW + "To start game enter y for yes and n for no.")
    answer = input_validation(Fore.YELLOW + "=> \n", ["y", "n"]).strip()
    if answer == "y":
        clr_terminal()
        introduction()
    if answer == "n":
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

    print(Fore.RED + """
       ________________INTRODUCTION____________\n
     Welcome to the Winchester House Mystery Game!
     This is a text based mystery game. You will need to use text based
     answers to traverse through the game collets items and solve the mystery.
    """)
    print(Fore.RED + r"""
                               !!!!!!!
                       .       [[[|]]]    .
                       !!!!!!!!|--_--|!!!!!
                       [[[[[[[[\_(X)_/]]]]]
               .-.     /-_--__-/_--_-\-_--\
               |=|    /-_---__/__-__-_\__-_\
           . . |=| ._/-__-__\===========/-__\_
           !!!!!!!!!\========[ /]]|[[\ ]=====/
          /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
         /-_--_--_--_|=  === ||=/^|^\ ||== =|
        /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
       /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
      /-__--|_|_|_-_-| |_|_|=||______=||_| =|
     /_-__--_-__-___-|_=__=_.`---------'._=_|__
    /-----------------------\===========/-----/
   ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
       |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
       | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
       ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
       || == `||-----||' = ==|| | | |=|| |=||
       ||= == ||:^s^:|| = == ||=| | | || |=||
       || = = ||:___:||= == =|| |_|_| ||_|=||
      _||_ = =||o---.|| = ==_||_= == =||==_||_
      \__/= = ||:   :||= == \__/[][][][][]\__/
      [||]= ==||:___:|| = = [||]\\//\\//\\[||]
      }  {---'"'-----'"'- --}  {//\\//\\//}  {
    __[==]__________________[==]\\//\\//\\[==]_
   |`|~~~~|================|~~~~|~~~~~~~~|~~~~||
jgs|^| ^  |================|^   | ^ ^^ ^ |  ^ ||
  \|//\\/^|/==============\|/^\\\^/^.\^///\\//|///
 \\///\\\//===============\\//\\///\\\\////\\\/////



      ,----.---------- .---------------\                            .-_.
   _                 |.`.,' `.           `.                         || |
    \                \ _|`. / `.            `.                      \|_o
     \                | \  `.   \.-----_-----.\     `
      \               `.|.`| `./ \\  c__)___/ \\             .
       \        `         `.   `. \\____\___)__\\
                            `. _ `.\`____________\
                              | \  |_|   ____   |_|
          _                   `.|\ ||__[.     ]__|_|`.
           \                      `================'  `.

    """)
    print("Enter y to continue or n to exit")
    answer = input_validation(Fore.YELLOW + "=> \n", ["y", "n"])
    if answer == "y":
        clr_terminal()
        scene1()
    if answer == "n":
        clr_terminal()
        game()


def scene1():
    """First chapter of the game"""
    print(Fore.RED + """
    ###______CHAPTER__1____###\n
    You Wake up in a car dazed confused and unsure of where you are.
    There is heavy rain beating the car making it almost impossible
    make out where you are.\n
    you.....


    """)
    print(Fore.GREEN + "1 - Search the car..")
    print(Fore.GREEN + "2 - leave the the car..\n\n")
    print(Fore.YELLOW + "Select 1/2")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"])
    if answer == "1":
        clr_terminal()
        search_car()
    elif answer == "2":
        clr_terminal()
        leave_car()


def search_car():

    """Search car for hidden item"""

    print(Fore.GREEN + "You Search the car...")
    print(Fore.GREEN + " Do you open the glove compartment...")
    print(Fore.YELLOW + "Enter y/n.")
    answer = input_validation(Fore.YELLOW + "=> \n", ["y", "n"])
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
    print(Fore.GREEN + "You open the glove compartment and find...\n")
    print(Fore.GREEN + "Youn find a phone..\n\n")

    print(Fore.GREEN + "Would you like to add this item to your Inventory\n")
    print(Fore.YELLOW + "Enter y/n")
    item = input(Fore.YELLOW + "=> \n").lower().strip()
    if item == "y":
        clr_terminal()
        print(Fore.GREEN + "items added to your inventory")
        addToInventory(Fore.GREEN + "phone")
        print(inventory)
        phone()
    if item == "n":
        clr_terminal()
        leave_car()


def phone():
    """Option for phone item"""

    print(Fore.GREEN + "You pick up the phone and look intently at it.")
    print(Fore.GREEN + """
    Hoping to jog any memory
    you have of the events that led you here.""")
    print(Fore.GREEN + "you notice you have two missed calls from James.")
    print(Fore.GREEN + "and a message...\n\n")

    print(Fore.GREEN + "Options....\n")
    print(Fore.GREEN + "1 -Read message ")
    print(Fore.GREEN + "2 - Leave car\n\n")
    print(Fore.YELLOW + "Select option (1,2) \n")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"])
    if answer == "1":
        clr_terminal()
        print(Fore.GREEN + "Message from James")
        print(Fore.CYAN + """
        Buddy you got to come check out this house.
        Its perfect for our next Pod Cast.
        I will send you the address meet me at
        the Old Winchester House on friday,
        you will not be dissapointed.
        \n\n""")
        print(Fore.CYAN + """
        'I remember now... I was meeting James at the location to
        record an episode of our haunted house pod cast'...\n
        'But how did i get here...'
        """)
        print(Fore.GREEN + "You peer through the windscreen.")
        print(Fore.GREEN + """
        Through the heave rain you can just about make out
        a large house shrouded in darkness.
        """)
        print(Fore.YELLOW + "Enter 1 to continue")
        answer = input_validation(Fore.YELLOW + "=> \n", ["1"])
        if answer == "1":
            leave_car()

    if answer == "2":

        print(Fore.GREEN + "Still confused you peer through the windscreen.")
        print(Fore.GREEN + """
        Through the heave rain you can just about make out
        a large house shrouded in darkness.
        """)
        print("Enter 1 to continue")
        answer = input_validation(Fore.YELLOW + "=> \n", ["1"])
        if answer == "1":
            leave_car()
            clr_terminal()


def leave_car():
    """Leave the car and enter house"""

    print(Fore.GREEN + "you you push the door open...")
    print(Fore.GREEN + "lightning cracks above your head!\n")
    print(Fore.GREEN + "you sheild you face from the stinging rain,")
    print(Fore.GREEN + "and run to the house.\n\n")

    print(Fore.GREEN + "Options....\n")
    print(Fore.GREEN + "1 - open door")
    print(Fore.GREEN + "2 - Look through the window\n\n")

    print("Select Option enter (1,2)")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"]).strip()
    if answer == "1":
        scene1()
    elif answer == "2":
        clr_terminal()
        window()


def scene2():
    """second scene enter the house"""
    clr_terminal()
    print(Fore.RED + """
                _________Chapter_2_________
    You slowly open the door entering a dimly lit entrance.
    The interior of the house is old with signs of decay.
    You look around squinting in the dim light and see...
    \n""")
    print(Fore.GREEN + "1 - A hallway straight infront of you.")
    print(Fore.GREEN + "2 - Living Room to your left.")
    print(Fore.GREEN + "3 - A grand stair case leading to the next floor\n")
    print(Fore.YELLOW + "select where you want to go (1,2,3")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2", "3"]).strip()
    if answer == "1":
        hallway()
        clr_terminal()
    elif answer == "2":
        living_room()
        clr_terminal()
    elif answer == "3":
        stairs()
        clr_terminal()


def hallway():
    """Section where you can enteract with Objects in the hallway"""

    print(Fore.RED + """
    ______Hallway______\n
    You make your way down to the door at the end of the hallway.
    you notice the walls are filled with old portraits and paintings.
    you.....\n\n
    """)
    print(Fore.GREEN + "1 - inspect the walls")
    print(Fore.GREEN + "2 - carry on to the doorway at the end of the hallway")
    print("")
    print("select option (1/2)")
    answer = input_validation(Fore.YELLOW + "=>\n ", ["1", "2"]).strip()
    if answer == "1":
        inspect_wall()
    elif answer == "2":
        clr_terminal()
        kitchen()


def inspect_wall():

    """Interact with pictures on wall"""
    print(Fore.GREEN + """
    You walk up to a an old black and white picture of what looks like,
    A family standing behind a sculpture of a skull.\n
    There is something very erie about this picture...
    """)

    print(Fore.GREEN + "You move on to the next the next picture\n")
    print(Fore.GREEN + """
    Thiis seems to be an even even older picture but the similarities
    between the two are uncanny. There is a family standing behind the
    same sulpture of a skull.
    """)
    print(Fore.CYAN + "'This is just getting creepy now.'")

    if "phone" in inventory:
        print(Fore.GREEN + "You call out")
        print(Fore.CYAN + "'JAMES!!..JAMES!!....'")
        print(Fore.GREEN + "no reply..'Where is he?'")
        kitchen()
    else:
        print(Fore.YELLOW + "press 1 to continue")
        answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
        if answer == "1":
            clr_terminal()
            kitchen()


def kitchen():
    """User enters the kitchen"""
    print(Fore.RED + """
    _______Kitchen______\n
    You open the door enter what looks a kitchen, all be it missing
    all the modern appliances you would find in a kitchen today.
    you flick the light switch and the several lights flicker but
    only one turns on.
    You around the shadow shrouded kitchen and see...

    """)
    print(Fore.GREEN + "1 - a Backpack on the floor")
    print(Fore.GREEN + "2 - A knife lying on the table")
    print(Fore.GREEN + "3 - You return to the entrance\n")
    print(Fore.GREEN + "Answer (1,2,3)")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2", "3"]).strip()
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
    """Interact with knife in kitchen"""
    print(Fore.GREEN + "You find a bloody knife laying on the counter top.")
    print(Fore.GREEN + "No traces of blood anywhere in the kitchen")
    print(Fore.GREEN + "The hairs on the back of your neck stand up")
    print(Fore.GREEN + "A sense of terror washes over you\n\n")

    print(Fore.GREEN + "What should you do next?\n")
    print(Fore.GREEN + "1 - Check backpack")
    print(Fore.GREEN + "2 - head back to entrance\n")
    print(Fore.YELLOW + "Enter choice (1,2)")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        backpack()
    elif answer == "2":
        clr_terminal()
        entrance()


def backpack():
    """Backback object contains important items"""
    print(Fore.GREEN + "You pick up the backpack and empty the contents.")
    print(Fore.GREEN + "A voice recorder slams on the table.")
    print(Fore.GREEN + "you pick up the device and press play\n")

    print(Fore.GREEN + "James's voice echos out the recorder....\n")
    print(Fore.CYAN + """
    'I dont know how I found this place or how I got here'..
    'This house must be over 200 yrs old'..
    'Its in remarkebly good condition'

    """)
    print(Fore.GREEN + "A loud BANG!! shoots out the speaker on the recorder")
    print(Fore.GREEN + "James calls out 'who's there!!'\n")
    print(Fore.GREEN + """
    you hear what sound like foot steps getting closer closer through
    the recorder....\n
    """)
    print(Fore.GREEN + "Then silence followed by an inhuman SCREAM!!\n")
    print(Fore.GREEN + "The scream makes you drop the recorder.")
    print(Fore.GREEN + "It smashes into pieces on the hard kitchen floor.\n\n")

    print(Fore.GREEN + "What do you do next.....\n")
    print(Fore.GREEN + "1 - Inspect Knife")
    print(Fore.GREEN + "2 - Leave kitchen\n")
    print(Fore.YELLOW + "Enter choice (1,2)")
    answer = input(Fore.YELLOW + "=> \n")
    if answer == "1":
        clr_terminal()
        knife()
    elif answer == "2":
        clr_terminal()
        entrance()


def entrance():
    """Main point of access to rooms"""

    print(Fore.GREEN + "Where would you like to go?\n\n")
    print(Fore.GREEN + "1 - living room")
    print(Fore.GREEN + "2 - stairs")
    print(Fore.GREEN + "3 - Hallway")
    print(Fore.GREEN + "4 - kitchen\n")
    print(Fore.YELLOW + "Enter (1,2,3,4)")
    answer = input(Fore.YELLOW + "=>\n").strip()
    if answer == "1":
        living_room()
    elif answer == "2":
        stairs()
    elif answer == "3":
        hallway()
    elif answer == "4":
        kitchen()


def living_room():
    """
    Living room sequence
    """
    print(Fore.RED + """
    ____Living_Room_______
    You enter the room and notice the embers in the fire place
    are still glowing.The room is shrouded in shadow the feeling
    that something could jump out the many corners of darkness is
    unnerving.\n

    You scan the room...
    """)
    print(Fore.GREEN + "what would you like to inspect.\n")
    print(Fore.GREEN + "1- Fire place")
    print(Fore.GREEN + "2 - leave room\n")
    print(Fore.YELLOW + "Please select (1,2)")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"]).strip()
    if answer == "1":
        fire_place()
    elif answer == "2":
        entrance()


def fire_place():

    """Where user interacts with fire to find hidden room"""

    print(Fore.RED + """
    _____Fire_Place___________________\n
    You cautiously make your way over to the fire place.
    The warmth coming from the red embers helps,
    settle your nerves.

    You notice something petruding out of the wall
    to the right of the fireplace. It looks like a skull
    coming out of the wall.....
    """)
    print(Fore.GREEN + "What do you next?\n")
    print(Fore.GREEN + "1 - Place your hand on the skull.")
    print(Fore.GREEN + "2 - leave room\n")
    print(Fore.YELLOW + "Please select (1,2)")

    answer = input_validation(Fore.YELLOW + "=>\n ", ["1", "2"]).strip()
    if answer == "1":
        hidden_room()
    elif answer == "2":
        clr_terminal()
        entrance()


def hidden_room():
    """Hidden room to obtain key"""
    clr_terminal()
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

    print(Fore.GREEN + "You place you hand on the skull..")
    print(Fore.GREEN + "The skull pushes into the back of the wall..")
    print(Fore.GREEN + "A loud mechanical sounds comes from the wall.")
    print(Fore.GREEN + "........\n")
    print(Fore.GREEN + "The wall suddenly opens up revealing a hidden room.\n")
    print(Fore.YELLOW + "Enter 1 to continue")
    answer = input_validation(Fore.YELLOW + "=>\n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        print(Fore.RED + """
        _______Hidden_Room_________
        You step into the in the room. It resembles a small study,
        there are peices of paper scattered around the room. You
        take a closer look at the papers stroon over a small desk
        and notice various sketches of symbols and what look like runes
        and what seems to be a letter\n.
        """)
        print(Fore.GREEN + "You search the desk")
        print(Fore.YELLOW + "Enter 1 to continue")
        answer = input_validation(Fore.YELLOW + "=>\n", ["1"]).strip()
        if answer == "1":
            clr_terminal()
            desk()


def desk():
    """Add key to inventory"""
    print(Fore.GREEN + """
    You search the desk and find a small box.
    You open the box and find an old rusty key.
    Something tells you to take the key.
    """)
    print(Fore.YELLOW + "Enter 1 to continue")
    answer = input_validation(Fore.YELLOW + "=>\n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        print("item added to your inventory")
        addToInventory("key")
        print(inventory)
        letter()


def letter():
    """Find warning letter"""
    print(Fore.GREEN + """
    You pick up the letter and try to read it in the dimly lit room.\n

    the letter reads:
    'A great evil has been released upon this house,
    beware of GOZO!'
    """)
    print(Fore.GREEN + "What do you do next?\n")
    print(Fore.GREEN + "1 - enspect the clock")
    print(Fore.GREEN + "2 - return to entrance\n\n")

    print(Fore.YELLOW + "Enter (1,2) to continue")

    answer = input_validation(Fore.YELLOW + "=>\n", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        clock()
    elif answer == "2":
        clr_terminal()
        entrance()


def clock():
    """Inspect strange clock"""
    print(Fore.GREEN + "You approach the clock and notice something weird.")
    print(Fore.GREEN + "instead of numbers there are symbols.\n")
    print(Fore.GREEN + "You hear a noise coming from upstairs!!")
    print(Fore.GREEN + "What do you do next?\n")
    print(Fore.GREEN + "1 - Go to stair case")
    print(Fore.GREEN + "2 - Head back to entrance\n")

    print(Fore.YELLOW + "Enter (1,2) to conitnue.")

    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"]).strip()
    if answer == "1":
        clr_terminal()
        stairs()
    elif answer == "2":
        clr_terminal()
        entrance()


def stairs():
    """Stairs to connect to final room"""
    print(Fore.GREEN + "You make you way to up the elegent stair case.")
    print(Fore.GREEN + "You hear a shuffling noise.")
    print(Fore.GREEN + "You pause for a moment to make sense of it.")
    print(Fore.GREEN + "Everything goes quiet..Dead silence..")
    print(Fore.GREEN + "You make your way up the stairs")
    print(Fore.GREEN + "You hear a shuffling noise coming form above you.")
    print(Fore.GREEN + "You see a ladder leading to what must be the attic\n")

    print(Fore.GREEN + "what do you do next?\n")
    print(Fore.GREEN + "1 - Go to attic")
    print(Fore.GREEN + "2 - Back to entrance\n\n")
    print(Fore.YELLOW + "Enter (1,2) to conitnue.")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1", "2"]).strip()
    if answer == "1":
        attic()
    elif answer == "2":
        entrance()


def attic():
    """Open to do to attic"""
    if "key" in inventory:
        print(Fore.GREEN + "You use the key to open the hatch to the attic.")
        the_end()
    else:
        clr_terminal()
        print(Fore.GREEN + "You need a key to open this door")
        entrance()


def window():
    """Interact with window"""
    print(Fore.GREEN + "look though the window to see a dimly lit entrance")
    print(Fore.GREEN + "You Enter the house\n")
    print(Fore.YELLOW + "press 1 to continue\n")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()

    if answer == "1":
        clr_terminal()
        scene2()


def the_end():
    """Last chapter"""
    print(Fore.RED + """
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
        clr_terminal()
        print(Fore.GREEN + "You grab you phone and turn on the torch.\n")
        print(Fore.GREEN + "You see your friend James standing in the corner.")
        print(Fore.CYAN + "'James..James are you ok'")
        print(Fore.CYAN + "'Where are we?.'")
        print(Fore.CYAN + "'What is going on?'\n")
        print(Fore.GREEN + "You get no response.")
        end_2()
    else:
        clr_terminal()
        print(Fore.GREEN + "You walk slowly to the figure in the corner.")
        print(Fore.GREEN + "You realize that its your friend James.\n")
        print(Fore.CYAN + "'James are you ok'")
        print(Fore.CYAN + "'What is going on'")
        end_2()


def end_2():
    """Find james"""
    clr_terminal()
    print(Fore.GREEN + "James turns and looks at you")
    print(Fore.GREEN + "He looks different..not himself.\n")
    print(Fore.GREEN + "You grab James and shake him..")
    print(Fore.GREEN + "He looks at you, almost surprised you see.")
    print(Fore.GREEN + "And says..")
    print(Fore.CYAN + "'It wont let us leave.'\n")
    print(Fore.CYAN + "'Who wont let us leave?'\n")
    print(Fore.GREEN + "James raises his hand and point behind you...\n\n")
    print(Fore.YELLOW + "Enter 1 to continue.\n")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        the_demon()


def the_demon():
    """Interact with demon"""
    print(Fore.GREEN + "You turn around and see piercing red eyes glowing.")

    print(Fore.RED + r"""
                               ,-.
       ___,---.__          /'|`\          __,---,___
    ,-'    \`    `-.____,-'  |  `-.____,-'    //    `-.
  ,'        |           ~'\     /`~           |        `.
 /      ___//              `. ,'          ,  , \___      \
|    ,-'   `-.__   _         |        ,    __,-'   `-.    |
|   /          /\_  `   .    |    ,      _/\          \   |
\  |           \ \`-.___ \   |   / ___,-'/ /           |  /
 \  \           | `._   `\\  |  //'   _,' |           /  /
  `-.\         /'  _ `---'' , . ``---' _  `\         /,-'
     ``       /     \    ,='/ \`=.    /     \       ''
             |__   /|\_,--.,-.--,--._/|\   __|
             /  `./  \\`\ |  |  | /,//' \,'  \
            /   /     ||--+--|--+-/-|     \   \
           |   |     /'\_\_\ | /_/_/`\     |   |
            \   \__, \_     `~'     _/ .__/   /
             `-._,-'   `-._______,-'   `-._,-'
    """)
    print(Fore.YELLOW + "Enter 1 to continue")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        the_escape()


def the_escape():
    """Escape the house"""
    print(Fore.GREEN + "You grab james and....\n")
    print(Fore.GREEN + "1 - Grab James and run to window")
    print(Fore.GREEN + "2 - Grab James and run to attic door.\n")

    print(Fore.YELLOW + "Enter 1/2 to continue.")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        print(Fore.GREEN + """
        You grab James and you both run to the window. At full speed
        you both throw yourselves into the window, smashing through
        the glass!
        """)
        print(Fore.YELLOW + "Enter 1 to continue.\n")
        answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
        if answer == "1":
            print(Fore.GREEN + "You crash out the window, roll of the roof")
            print(Fore.GREEN + "Everything goes black")
            the_end_3()


def the_end_3():
    """Sequence after use escapes"""

    print(Fore.GREEN + """
    You are awakened by voice.....

    'Son are you OK?... What are you doing all the way out here?'

    you open your eyes, squintung from the sun hittin your face.
    You see an old freindly faced man kneeling next to you.

    You reach out and grab his arm and shout 'Dont go into the house!!'

    The man looked at you confused....
    'What house?'...

    """)
    print(Fore.YELLOW + "Enter 1 to continue.\n")
    answer = input_validation("=>\n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        end_credits()


def end_credits():
    """The end credits"""
    print(r"""
▀▀█▀▀ ▒█░▒█ ▒█▀▀▀    ▒█▀▀▀ ▒█▄░▒█ ▒█▀▀▄
░▒█░░ ▒█▀▀█ ▒█▀▀▀    ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█
░▒█░░ ▒█░▒█ ▒█▄▄▄    ▒█▄▄▄ ▒█░░▀█ ▒█▄▄▀
    """)

    print(Fore.YELLOW + "Enter 1 to continue.\n")
    answer = input_validation(Fore.YELLOW + "=> \n", ["1"]).strip()
    if answer == "1":
        clr_terminal()
        game()


game()
