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
    answer = input(" Click any key to start:")
    print("Let's start by designing your field of plants. You will have to customize three plants.\n")
    field1 = Field.initializeField()
    '''Trying this code will result in an infinite loop while game remains unbalanced
    while(len(field1.plants) != 0):
        environment1 = Environment.initializeEnvironment()
        field1.processTurn(environment1) '''
    i = 0
    while (i < 3 and field1.numPlants != 0):
        generation = i + 1
        print("Turn number " + str(generation) + ": ")
        #This makes it so that environment is initialized each turn, rather than each plant
        environment1 = Environment.initializeEnvironment()
        field1.processTurn(environment1, generation)
        i = i + 1
        input("Click any key to go to your next turn: ")
    if i == 3:
        print ("Your plants are alive! Thanks for playing!")
    else:
        print("Your plants did not survive!")

start()