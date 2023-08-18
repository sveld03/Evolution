from plant import *
from environment import *

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
        print("Here is your field:\n")
        for i in range(len(self.plants)):
            print("HR:" + str(self.plants[i].heatResistance) + " CR:" + str(self.plants[i].coldResistance) + " DR:" + str(self.plants[i].diseaseResistance) + " Str:" + str(self.plants[i].strength) + " HP:" + str(self.plants[i].hitPoints)  + " \n")

    #gets number of plants
    def getNumPlants(self):
        print (str(self.numPlants))
    
    #initializes a field by introducing what a field is and then initializing each plant
    #The result is stored into a new Field aptly titled field (remember where to put this for game mechanics)
    #The method ends by calling getPlants()
    def initializeField():
        print("Each plant has four attributes: heat resistance, cold resistance, disease resistance, and strength.\nBefore selecting your values, remember, they must all add up to 10\n")
        plantArray = []
        for i in range(Field.numberStartingPlants):
            placeholder = str(i + 1)
            print("Initializing plant #" + placeholder + ": ")
            plant = Plant.initializePlant()
            plantArray.append(plant)
        field = Field(plantArray)
        field.getPlants()
        return field

    #method that enacts plantLoss on each plant in field array
    def fieldLoss(self, environment, generation):
        print("Oh no, here comes the environment! The heat is now " + str(environment.temperature) + " degrees and the disease level is " + str(environment.disease) + "\n")
        for i in range(self.numPlants):
            self.plants[i].plantLoss(environment, generation)

    #method that makes two copies of plant with highest HP and adds it to the field
    #searches through array of plants and compares HP
    ##IMPORTANT MECHANIC: when it reproduces the two new plants, it increases their strongest trait by 2
    def reproduceStrongestPlant(self):
        if (self.numPlants == 0):
            print ("You cannot reproduce! Your plants are dead!\n")
        else:
            print("Your strongest plant managed to reproduce two times. With a bonus!\n")
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
        temp = []
        for i in range (0, self.numPlants):
            if self.plants[i].hitPoints <= 0:
                temp.append(self.plants[i])
        for deadPlant in temp:
            (self.plants).remove(deadPlant)
        self.numPlants = len(self.plants)



    
    #returns total hit points of a field
    def getHitPoints(self):
        totalHitPoints = 0
        for i in range (self.numPlants):
            totalHitPoints += self.plants[i].hitPoints
        return totalHitPoints



    #processes a turn for a field: calls fieldLoss, reproducton, and removal of all plants in the field array
    #after processing the methods, a message saying turn has ended, as well as getPlants() and a new method getTotalHitPoints
    def processTurn(self, environment, generation):
        self.fieldLoss(environment, generation)
        self.removeDeadPlants()
        self.reproduceStrongestPlant()
        print("Turn has ended. \n")
        #print("Here are your plants:")
        print(str(self.getPlants()))
        #print("The total field's hit points are: " + self.getHitPoints())