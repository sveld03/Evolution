from plant import *
from environment import *
from field import *

import sys
import time

#code to make the user interactions print slower
def print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #changing this value will change speed of printing
        """change to .05 for actual game"""
        time.sleep(0.01)

def start():
    #Welcome message with explanation of rules
    print ("Welcome to Evolution!\nIn this game, you will be designing a field of plants and watching them evolve in response to changing environments.\nAre you ready to play?")
    answer = input("Click any key to start:")
    playerOne = input("Player one, enter your name: ")
    playerTwo = input("Player two, enter your name: ")
    print(playerOne + ", let's start by designing your field of plants. You will have to customize three plants.\n")
    playerOneField = Field.initializeField()
    print(playerTwo + ", let's start by designing your field of plants. You will have to customize three plants.\n ")
    playerTwoField = Field.initializeField()
    '''Trying this code will result in an infinite loop while game remains unbalanced
    while(len(field1.plants) != 0):
        environment1 = Environment.initializeEnvironment()
        field1.processTurn(environment1) '''
    i = 0
    while (i < 3 and playerOneField.numPlants != 0 and playerTwoField.numPlants != 0):
        generation = i + 1
        print("Turn number " + str(generation) + ": ")

        playerAction()

        #This makes it so that environment is initialized each turn, rather than each plant
        environment1 = Environment.initializeEnvironment()
        print(playerOne + ", it's your turn")
        playerOneField.processTurn(environment1, generation)
        print(playerTwo + ", it's your turn")
        playerTwoField.processTurn(environment1, generation)
        i = i + 1
        input("Click any key to go to your next turn: ")
    if playerOneField.getHitPoints() > playerTwoField.getHitPoints():
        print (playerOne + " wins!")
    else:
        print(playerTwo + " wins!")

#defines how a player can influence the game
def playerAction():
    eorf = input("Would you like to influence the environment (e) or your field of plants (f) ? ")
    if (eorf == 'e'):
        environmentBuffType = input("Would you like to make it hotter (h), colder(h), or add more disease(d) ? ")
    else:
        plantNumber = int(input("What plant would you like to improve? Type the number"))
        plantBuffType = input("Would you like to improve heat resistance (h), cold resistance (c), disease resistance(d) or strength(s) ?")

start()
