import turtle

opnum = 0
compnum = 0
yournum = 0

#Board Setup
char1 = turtle.Turtle()
char1.shape('circle')
char1.pensize(2)
char1.pencolor("blue")
char1.color("blue")

char2 = turtle.Turtle()
char2.shape('circle')
char2.pensize(2)
char2.pencolor("purple")
char2.color("purple")

def board_setup():
    import tkinter
    turtle.setup(640, 640)
    wn = turtle.Screen()
    wn.title("Climb & Slide")
    canvas = wn.getcanvas()
    map_bg_img = tkinter.PhotoImage(file="images\climbandslide.gif")
    canvas.create_image(-300, -300, anchor = tkinter.NW, image = map_bg_img)
    t = turtle.Turtle()
    return (t, wn, map_bg_img)
(t, wn, map_bg_img) = board_setup()

import random

n = 0

def roll():
    global n
    n = random.randint(1,6)

def youroll():
    ip = input("Press Enter to Roll: ")
    if ip == "":
        roll()
    else:
        youroll()

def moves():
    roll()
    global n
    n = n
    if n == 1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
    elif n == 2:
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
    elif n == 3:
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
    elif n == 4:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
    elif n == 5:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
    elif n == 6:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")
    print(n, "was rolled.")
    print("Move", n, "spaces.")

def chooseplayers():
    global you
    you = random.randint(1,2)
    if you == 1:
        print("You are Player 1 (Blue).")
    else:
        print("You are Player 2 (Purple).")


def whatgame():
    global x
    x = input("What game do you want to play? Type M for multiplayer or C for against the computer: ")
    x = x.upper()
    print("You chose:", x)
    print()
    if x == "M":
        print("Welcome to Multiplayer Climb & Slide!")
        chooseplayers()
    elif x == "C":
        print("Welcome to Beat the Computer Climb & Slide!")
        chooseplayers()


def welcome():
    instructions = """
Welcome to Climb & Slide!
Directions:
    1. Choose what kind of game you want to play. You can either against with a friend or against the computer.
    2. You and your opponent will take turns rolling a dice to determine how many spaces you can move forward.
    3. If you land on a slide, you will have to move to the space that the slide ends on.
    4. If you land on a rope, you move to the space that the rope leads to.
    5. If you land on a space with a star, you will be asked a trivia question. If you get it right, you will be able to move forward a number of spaces. If you get the question wrong, you will be penalized and set back a number of spaces.
    6. The first person to reach the "Finish" space WINS!
"""
    print(instructions)
    whatgame()
welcome()


def yourturn():
    global n
    n = n
    ip = input("Press Enter to Roll: ")
    if ip == "":
        moves()
    else:
        youroll()
    global yournum
    yournum = yournum
    yournum = yournum + n
    print(yournum)
    if yournum <= 10:
        if you == 1:
            char1.goto((-255 + (n * 55)), -265)
        else:
            char2.goto((-255 + (n * 55)),-245)
    if yournum > 10:
        pass
    if yournum > 10 and yournum <= 20:
        if you == 1:
            char1.goto((255 - (n * 55)), -265)
        else:
            char2.goto((255 - (n * 55)),-245)

def opturn():
    z = 0
    ip = input("Press Enter to Roll: ")
    if ip == "":
        moves()
    else:
        youroll() 
    global n
    n = n
    global opnum
    opnum = opnum
    opnum = opnum + n
    if yournum <= 10:
        if you == 1:
            z = -255 + (n*55)
            char2.goto(z ,-245)                         
        else:
            z = -255 + (n*55)
            char1.goto(z, -265)                 
    print(opnum)

def compturn():
    moves()
    global n
    global you
    you = you
    n = n
    m = n * 55
    global compnum
    compnum = compnum
    compnum = compnum + n
    if yournum <= 10:
        if you == 1:
            
           char2.goto((-255 + (n * 55)), -245)                         
        else:
           char1.goto((-255 + (n * 55)), -265)    
    print(compnum)
    
def rungame():
    global x
    x = x
    global you
    you = you
    print()
    print("It is Player 1's turn.")
    global yournum
    yournum = yournum
    global opnum
    opnum = opnum
    global compnum
    compnum = compnum
    if you == 1:
        if x == "M":
            yourturn()
            if yournum < 100 and opnum < 100:
                print()
                print("It is Player 2's turn.")
                opturn()
        elif x == "C":
            yourturn()
            if yournum < 100 and compnum < 100:
                print()
                print("It is Player 2's turn.")
                compturn()
    else:   
        if x == "M":
            opturn()
            if yournum < 100 and opnum < 100:
                print()
                print("It is Player 2's turn.")
                yourturn()
        elif x == "C":
            compturn()
            if yournum < 100 and compnum < 100:
                print()
                print("It is Player 2's turn.")
                yourturn()

def setup():
    char1.goto(-255,-265)
    char2.goto(-255,-245)
    global yournum
    global compnum
    global opnum
    yournum = yournum
    compnum = compnum
    opnum = opnum
    while yournum < 100 and compnum < 100 and opnum < 100:
        rungame()
setup()



#Unfinished

"""
    if yournum == 7 or opnum == 7:
        answer = input("Which U.S. state is known for peaches?: ")
    if yournum == 15 or opnum == 15:
        answer = input("What does Na stand for on the periodic table?: ")
    if yournum == 21 or opnum == 21:
        answer = input("Who is the author of the Harry Potter series?: ")
    if yournum == 38 or opnum == 38:
        answer = input("This place is known as the City of Brotherly Love. What is this city called?: ")
    if yournum == 46 or opnum == 46:
        answer = input("How many days are there in a leap year?: ")
    if yournum == 56 or opnum == 56:
        answer = input("What country gifted the Statue of Liberty to the U.S?: ")
    if yournum == 69 or opnum == 69:
        answer = input("How many bones are there in the human body?: ")
    if yournum == 78 or opnum == 78:
        answer = input("Where is the world's largest active volcano located?: ")
    if yournum == 87 or opnum == 87:
        answer = input("Which bird is often associated with delivering babies?: ")
    if yournum == 93 or opnum == 93:
        answer = input("In Greek Mythology, who is the Queen of the Underworld and wife of Hades?: ")
    if yournum == 98 or opnum == 98:
        answer = input("Where is the Great Barrier Reef located?: ")
"""
