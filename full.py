from random import randint
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
        #i don't know if I missed something but the random wasn't working?
        temperature = randint(50, 90)
        disease = randint (0, 10)
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
        answerHeat = float(input("what number heat resistance do you you want?"))
        answerCold = float(input("what number cold resistance do you want?"))
        answerDisease = float(input("what number disease resistance do you want?"))
        answerStrength = float(input("what number strength do you want?"))
        #checks that each plant's attibutes adds up to ten
        if (answerHeat + answerCold + answerDisease + answerStrength == 10):
            plant1 = Plant(answerHeat, answerCold, answerDisease, answerStrength)
            print("Here are the qualities of your plant: ") 
            print("HR:" + str(plant1.heatResistance) + " CR:" + str(plant1.coldResistance) + " DR:" + str(plant1.diseaseResistance) + " Str:" + str(plant1.strength) + "\n")
            #return plant1 so that other methods can access the data of the plant (i.e this plant gets added to field array)
            return plant1
        #if they don't add up to 10, you have to start over on that plant
        else:
            print("Your qualities do not add up to 10: try again\n")
            Plant.initializePlant()

    
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
        for i in range(len(self.plants) - 1):
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
    """def getHitPoints(self):
        totalHitPoints = 0
        for i in range (self.numPlants):
            totalHitPoints += self.plants[i].hitPoints
        print (totalHitPoints)
        return totalHitPoints"""



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

    


