import Plant
from Environment import *
from Field import *


def start():
    #Welcome message with explanation of rules
    print ("""Welcome to Evolution! \n In this game, you will be designing a field of plants and watching them evolve 
    in response to changing environments. \n Are you ready to play?""")
    answer = input("Type YES to move on: ").lower()
    if (answer == "yes"):
        "Great!"
    else:
        "Wrong answer! You'll get better at that!"
    print ("Let's start by designing your field of plants")
    Field.initializeField()
    

start()