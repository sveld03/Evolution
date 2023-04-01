from Environment import *
from Field import *

#Represents the properties of an individual plant
class Plant (object):

    #initializes a plant for its four traits, including calculating HP from strength
    def __init__(self, heatResistance, coldResistance, diseaseResistance, strength):
        self.heatResistance = int(heatResistance)
        self.coldResistance = int(coldResistance)
        self.diseaseResistance = int(diseaseResistance)
        self.strength = int(strength)
        self.hitPoints = int(strength) + 10

    #code to initialize a plant by interacting with user.
    def initializePlant():
        print ("""Each plant has four attributes:
        "heat resistance, cold resistance, disease resistance, and strength. Before selecting your values, 
        remember, they must all add up to 10""")
        answerHeat = float(input("what number heat resistance do you you want?"))
        answerCold = float(input("what number cold resistance do you want?"))
        answerDisease = float(input("what number disease resistance do you want?"))
        answerStrength = float(input("what number strength do you want?"))
        #checks that each plant's attibutes adds up to ten
        if (answerHeat + answerCold + answerDisease + answerStrength == 10):
            plant1 = Plant(answerHeat, answerCold, answerDisease, answerStrength)
            print ("Here are the qualities of your plant") 
            print ("HR:" + str(plant1.heatResistance) + " CR:" + str(plant1.coldResistance) + " DR:" + str(plant1.diseaseResistance) + " Str:" + str(plant1.strength))
            #return plant1 so that other methods can access the data of the plant (i.e this plant gets added to field array)
            return plant1
        #if they don't add up to 10, you have to start over on that plant
        else:
            print ("your qualities do not add up to 10: try again")
            Plant.initializePlant()

    
    def plantLoss(self, plant, environment):

        # Run one generation: plant takes damage from the environment, then reproduces (we can add random mutations later)
        environment = Environment.initializeEnvironment()
        hitMarker = 0
        if plant.heatResistance < environment.hot:
            hitMarker += environment.hot - plant.heatResistance
        if plant.coldResistance < environment.cold:
            hitMarker += environment.cold - plant.coldResistance
        if plant.diseaseResistance < environment.disease:
            hitMarker += environment.disease - plant.diseaseResistance
        print("Hitmarker: " + str(hitMarker))
        plant.hitPoints -= hitMarker
        print("Your generation 1 plant now has " + str(plant.hitPoints) + " remaining hitpoints. ")




