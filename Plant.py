from Environment import *
from config import *

#Represents the properties of an individual plant
class Plant (object):

    #initializes a plant for its four traits, including calculating HP from strength
    def __init__(self, heatResistance, coldResistance, diseaseResistance, strength, x, y):
        self.heatResistance = int(heatResistance)
        self.coldResistance = int(coldResistance)
        self.diseaseResistance = int(diseaseResistance)
        self.strength = int(strength)
        self.hitPoints = (int(strength) * Parameters.strengthImpactOnHitpoints) + 10
        self.x = x
        self.y = y

    #code to initialize a plant by interacting with user.
    def initializePlant(playerNumber):
        answerHeat = float(input("what number heat resistance do you you want?"))
        answerCold = float(input("what number cold resistance do you want?"))
        answerDisease = float(input("what number disease resistance do you want?"))
        answerStrength = float(input("what number strength do you want?"))

        side = ""
        boundary = ""
        if playerNumber == 1:
            side = "left"
            boundary = "(1 to 3): "
        elif playerNumber == 2:
            side = "right"
            boundary = "(4 to 6): "
        print("Now it's time to choose your plant's location! You will choose where to place your plant on a(n) " 
              + str(FIELDWIDTH) + "x" + str(FIELDHEIGHT) + " grid. As player " + str(playerNumber) + ", you must place your plant on the " 
              + side + " side of the grid.")
        answerX = int(input("Choose your plant's X location " + boundary)) - 1
        answerY = int(input("Choose your plant's Y location (1 to 6): ")) - 1

        #checks that each plant's attibutes adds up to ten
        if (answerHeat + answerCold + answerDisease + answerStrength == 10):
            plant1 = Plant(answerHeat, answerCold, answerDisease, answerStrength, answerX, answerY)
            print("Here are the qualities of your plant: ") 
            print("HR:" + str(plant1.heatResistance) + " CR:" + str(plant1.coldResistance) + " DR:" + str(plant1.diseaseResistance) + " Str:" + str(plant1.strength) + "\n")
            #return plant1 so that other methods can access the data of the plant (i.e this plant gets added to field array)
            return plant1
        #if they don't add up to 10, you have to start over on that plant
        else:
            print("Your qualities do not add up to 10: try again\n")
            Plant.initializePlant(playerNumber)

    
    def plantLoss(self, environment, generation):

        # Run one generation: plant takes damage from the environment, then reproduces (we can add random mutations later)
        #I wanted the environment to be the same for each round of plants, so I moved this to fieldLoss
        # environment = Environment.initializeEnvironment()
        hitMarker = 0
        if self.heatResistance < environment.hot:
            hitMarker += environment.hot - self.heatResistance
        if self.coldResistance < environment.cold:
            hitMarker += environment.cold - self.coldResistance
        if self.diseaseResistance < environment.disease:
            hitMarker += environment.disease - self.diseaseResistance
        print("Hitmarker: " + str(hitMarker) + "\n")
        self.hitPoints -= hitMarker
        gen = generation
        print("Your generation " + str(gen) + " plant now has " + str(self.hitPoints) + " remaining hitpoints.\n")

    def improveTrait(self, trait):
        if trait == 'h':
            self.heatResistance += Parameters.playerImpactOnPlants
        elif trait == 'c':
            self.coldResistance += Parameters.playerImpactOnPlants
        elif trait == 'd':
            self.diseaseResistance += Parameters.playerImpactOnPlants
        elif trait == 's':
            self.strength += Parameters.playerImpactOnPlants
        else:
            return -1




