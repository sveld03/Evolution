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
        self.heatResistance = heatResistance
        self.coldResistance = coldResistance
        self.diseaseResistance = diseaseResistance
        self.strength = strength
        self.hitPoints = int(strength) + 10

    #code to initialize a plant by interacting with user.
    def initializePlant():
        print ("""Welcome to our game! You are going to make a plant. Each plant has four attributes:
        "heat resistance, cold resistance, disease resistance, and strength. Before selecting your values, 
        remember, they must all add up to 10""")
        answerHeat = float(input("what number heat resistance do you you want?"))
        answerCold = float(input("what number cold resistance do you want?"))
        answerDisease = float(input("what number disease resistance do you want?"))
        answerStrength = float(input("what number strength do you want?"))
        plant = Plant(answerHeat, answerCold, answerDisease, answerStrength)
        print ("Here are the qualities of your plant") 
        print ("HR:" + str(plant.heatResistance) + " CR:" + str(plant.coldResistance) + " DR:" + str(plant.diseaseResistance) + " Str:" + str(plant.strength))
        return plant

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


"""Represents the ten plants that make up a field. Has its own initializeField method that makes ten plants and adds them to the field.
Helpful for method calls that effect all of the plants, like environmental attacks.
It also will have the methods that create new plants after each round
class Field (object):
     numPlants = 10

    #Not totally sure how - I want to pass an array of 10 plants into the field
     def __innit__(self, plants):
        self.plants = plants """

#End result of this section: it starts the initializeField code, which uses a loop of 10 iterations to make 10 plants with initializePlant
def start():
    #placeholder: it just calls initializePlant method
    plant1a = Plant.initializePlant()

    # Run one generation: plant takes damage from the environment, then reproduces (we can add random mutations later)
    environment = Environment.initializeEnvironment()
    hitMarker = 0
    if plant1a.heatResistance < environment.hot:
        hitMarker += environment.hot - plant1a.heatResistance
    if plant1a.coldResistance < environment.cold:
        hitMarker += environment.cold - plant1a.coldResistance
    if plant1a.diseaseResistance < environment.disease:
        hitMarker += environment.disease - plant1a.diseaseResistance
    print("Hitmarker: " + str(hitMarker))
    plant1a.hitPoints -= hitMarker
    plant2a = plant1a
    """THIS IS THE CODE I WAS REFERRING TO
    traits = [trait for trait in dir(plant1a)]
    bestTraits = []
    for trait in traits:
        for compare in traits:
            if trait >= compare:
                bestTraits.append(trait)
    for trait in bestTraits:
        plant2a.trait = plant1a.trait + 2/(bestTraits.len())"""

    print("Your generation 1 plant now has " + str(plant1a.hitPoints) + " remaining hitpoints. "
          "It reproduced, and you now have a generation B plant with the following stats:\n",
          "HR: " + str(plant2a.heatResistance),
          "CR: " + str(plant2a.coldResistance),
          "DR: " + str(plant2a.diseaseResistance),
          "Str: " + str(plant2a.strength))

#starts the program (this will go in another main file obviously, right now its set to a default of initializing one plant)
start()



