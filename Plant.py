import random

# Represents the properties of the environment
class Environment (object):
    
    # Initializes all environmental factors: temperature, disease, cold, and hot
    def __init__(self, temperature, disease):
        # self.temperature = random(50, 90)
        # self.disease = random(0, 10)
        self.temperature = temperature
        self.disease = disease
        if self.temperature < 70:
            self.cold = (70 - self.temperature) / 2
            self.hot = 0
        elif self.temperature > 70:
            self.cold = 0
            self.hot = (self.temperature -  70) / 2
        else:
            self.cold = 0
            self.hot = 0

    def initializeEnvironment():
        temperature = random.randint(50, 90)
        disease = random.randint(0, 10)
        environment = Environment(temperature, disease)
        return environment

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
        print (""" Each plant has four attributes:
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

    #method that calculates how much hp a plant loses from each kind of attack and deducts it (Q for future: separate method to actual deduct? Helpful for user to know their risk?)
    #The environment code should handle these variables? Basically communicate to me how you will do it
    # I SET 10 AS A DEFAULT FOR ENVIRONMENT STRENGTH - NEED TO CHANGE THAT BASED ON STEVEN CODE
    ##It is commented out becase of this
    """""
    def plantLoss(self, environmentCondition):
        if environmentCondition == heatCondition:
            self.hitPoints -= (10 - self.heatResistance)
        elif environmentCondition == coldCondition:
            self.hitPoints -= (10 - self.coldResistance)
        else:
            self.hitPoints -= (10 - self.diseaseResistance) """
    
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


"""Represents the ten plants that make up a field. Has its own initializeField method that makes ten plants and adds them to the field.
Helpful for method calls that effect all of the plants, like environmental attacks.
It also will have the methods that create new plants after each round
class Field (object):
     numPlants = 10

    #Not totally sure how - I want to pass an array of 10 plants into the field
     def __innit__(self, plants):
        self.plants = plants """

#End result of this section: it starts the initializeField code, which uses a loop of 10 iterations to make 10 plants with initializePlant

class Field (object):
    #this is all you need to change to mess with number of starting plants parameter
    numberStartingPlants = 3
    #Field constructor takes an array of plants as a parameter
    def __init__(self, plants = []):
        self.plants = plants
        #number of plants set to the static numberStartingPlants
        self.numPlants = int(Field.numberStartingPlants)

    #prints out the stats of all the plants in your field
    def getPlants(self):
        print ("Here is your field:")
        for i in range(len(self.plants)):
            print ("HR:" + str(self.plants[i].heatResistance) + " CR:" + str(self.plants[i].coldResistance) + " DR:" + str(self.plants[i].diseaseResistance) + " Str:" + str(self.plants[i].strength))

    #gets number of plants
    def getNumPlants(self):
        print (self.numPlants)
    
    #initializes a field by introducing what a field is and then initializing each plant
    #The result is stored into a new Field aptly titled field (remember where to put this for game mechanics)
    #The method ends by calling getPlants()
    def initializeField():
        plantArray = []
        for i in range(Field.numberStartingPlants):
            plant = Plant.initializePlant()
            plantArray.append(plant)
        field = Field(plantArray)
        field.getPlants()

    #method that enacts plantLoss on each plant in field array
    def fieldLoss(self, environment):
        for i in range(Field.numPlants):
            self.plants[i].plantLoss(environment)

    #method that makes two copies of plant with highest HP and adds it to the field
    #searches through array of plants and compares HP
    ##IMPORTANT MECHANIC: when it reproduces the two new plants, it increases their strongest trait by 2
    def reproduceStrongestPlant(self):
         strongestPlant = self.plants[0]
         #finds plant with highest HP
         for i in range(len(self.plants)):
             currentPlant = self.plants[i]
             if (currentPlant.hitPoints > strongestPlant.hitPoints):
                 strongestPlant = currentPlant 
        #finds the highest trait of strongest Plant
         strongestPlantStats = [strongestPlant.heatResistance, strongestPlant.coldResistance, strongestPlant.diseaseResistance, strongestPlant.strength]
         maxValueIndex = strongestPlantStats.index(max(strongestPlantStats))
         #variables for traits of strongest plant to make their else statement easier
         heat = strongestPlant.heatResistance
         cold = strongestPlant.coldResistance
         disease = strongestPlant.diseaseResistance
         strength = strongestPlant.strength
         #creates two copies of strongest plant, with its highest trait +2
         if (maxValueIndex == 0):
            heat += 2
            newPlantOne = Plant(heat, cold, disease, strength)
            newPlantTwo = Plant(heat, cold, disease, strength)
         elif (maxValueIndex == 1):
            cold += 2
            newPlantOne = Plant(heat, cold, disease, strength)
            newPlantTwo = Plant(heat, cold, disease, strength)
         elif (maxValueIndex == 2):
            disease += 2
            newPlantOne = Plant(heat, cold, disease, strength)
            newPlantTwo = Plant(heat, cold, disease, strength)
         else:
            strength += 2
            newPlantOne = Plant(heat, cold, disease, strength)
            newPlantTwo = Plant(heat, cold, disease, strength)
         self.plants.append(newPlantOne)
         self.plants.append(newPlantTwo)
         self.numPlants += 2
        


    #method that removes any plant with less than 0 HP from the plants array
    def removeDeadPlants(self):
        #I was having some index out of range issues here - so I did length of array instead of running number of plants
        for i in range (self.numPlants - 2):
            ##MUST FIX HERE - MIGHT NEED STEVEN HELP
            """NOT FULLY WORKING RIGHT HERE - I SET THE RANGE WRONG INTENTIONALLY CUZ I KEPT GETTING RANGE ERRORS"""""
            if (int(self.plants[i].hitPoints) <= 0):
                (self.plants).remove(self.plants[i])

                """Is this necessary?"""
                self.numPlants -= 1
                #to help test and figure out whats wrong
                self.getNumPlants()
                print (self.plants[i])



    
    #returns total hit points of a field
    def getHitPoints(self):
        totalHitPoints = 0
        for i in range (self.numPlants):
            totalHitPoints += self.plants[i].hitPoints
        print (totalHitPoints)
        return totalHitPoints



    #processes a turn for a field: calls fieldLoss, reproducton, and removal of all plants in the field array
    #after processing the methods, a message saying turn has ended, as well as getPlants() and a new method getTotalHitPoints
    def processTurn(self):
        self.fieldLoss()
        self.reproduceStrongestPlant()
        self.removeDeadPlants()
        print("Turn has ended")
        print("Here are your plants:" + self.getPlants())
        print("The total field's hit points are: " + self.getHitPoints())


#End result of this section: it starts the initializeField code, which uses a loop of 10 iterations to make 10 plants with initializePlant
def start():
    # Field.initializeField()
    ##reproduceStrongestPlant@TEST
    plantOne = Plant(1, 1, 1, 7)
    plantTwo = Plant(1, 2, 3, 4)
    plantThree = Plant(4, 3, 2, 1)
    plantArray = [plantOne, plantTwo, plantThree]
    myField = Field(plantArray)
    myField.getPlants()
    myField.reproduceStrongestPlant()
    myField.getPlants()
    myField.getNumPlants()
    #RemovePlants@TEST
    plantOne.hitPoints = -12
    plantTwo.hitPoints = 0
    plantThree.hitPoints = -2
    # myField.removeDeadPlants()
    # myField.getPlants()
    #totalHitPoints test
    myField.getHitPoints()


#starts the program (this will go in another main file obviously, right now its set to a default of initializing one plant)
start()