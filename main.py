from Plant import *
from Environment import *
from Field import *
from config import Parameters
from grid import *

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
    print ("Welcome to Evolution!\nIn this game, you will be designing a field of plants and watching them evolve in response to changing environments.\nAre you ready to play? ")
    answer = input("Click enter to start:")
    playerOne = input("Player one, enter your name: ")
    playerTwo = input("Player two, enter your name: ")
    grid = Grid()
    print(playerOne + ", let's start by designing your field of plants. You will have to customize " + str(Parameters.fieldSize) + " plants.\n")
    playerOneField = Field.initializeField(grid, 1)
    print(playerTwo + ", let's start by designing your field of plants. You will have to customize "  + str(Parameters.fieldSize) + " plants.\n")
    playerTwoField = Field.initializeField(grid, 2)
    '''Trying this code will result in an infinite loop while game remains unbalanced
    while(len(field1.plants) != 0):
        environment1 = Environment.initializeEnvironment()
        field1.processTurn(environment1) '''
    
    # pygame.display.update()

    environment1 = Environment.initializeEnvironment()

    i = 0
    while (i < Parameters.turns and playerOneField.numPlants != 0 and playerTwoField.numPlants != 0):
        grid.draw_grid()
        
        generation = i + 1
        print("Turn number " + str(generation) + ": ")
        print(playerOne + ", it's your turn. ")
        playerAction(environment1, playerOneField)
        playerOneField.processTurn(environment1, generation)

        print(playerTwo + ", it's your turn. ")
        playerAction(environment1, playerTwoField)
        playerTwoField.processTurn(environment1, generation)

        i = i + 1
        input("Click any key to go to your next turn: ")
    if playerOneField.getHitPoints() > playerTwoField.getHitPoints():
        print (playerOne + " wins!")
    else:
        print(playerTwo + " wins!")

    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()

#defines how a player can influence the game
def playerAction(environment, field):
    environment1 = environment
    eorf = input("Would you like to influence the environment (e) or your field of plants (f) ? ")
    if (eorf == 'e'):
        environmentBuffType = input("Would you like to make it hotter (h), colder (c), or change the disease(d) ? ")
        if (environmentBuffType == 'h'):
            environment1.makeHotter()
        elif(environmentBuffType == 'c'):
            environment1.makeColder()
        elif (environmentBuffType == 'd'):
            diseaseBuffType = input("Would you like to increase(i) or decrease(d) the disease level? ")
            if (diseaseBuffType == 'i'):
                environment1.increaseDisease()
            elif(diseaseBuffType == 'd'):
                environment1.decreaseDisease()
            else:
                print("you suck at typing, try again\n")
                playerAction(environment1, field)
        else:
            print("You suck at typing, try again\n")
            playerAction(environment1, field)
    elif (eorf == 'f'):
        plantNumber = int(input("What plant would you like to improve? Type the number "))
        plantBuffType = input("Would you like to improve heat resistance (h), cold resistance (c), disease resistance(d) or strength(s) ? ")
        check = field.plants[plantNumber - 1].improveTrait(plantBuffType)
        if check == -1:
            print("You suck at typing, try again\n")
            playerAction(environment1, field)
    else:
        print("You suck at typing, try again\n")
        playerAction(environment1, field)


start()
