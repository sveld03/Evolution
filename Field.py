from Plant import *
from Environment import *
from grid import *

class Field (object):
    #this is all you need to change to mess with number of starting plants parameter
    # numberStartingPlants = Parameters.fieldSize
    #Field constructor takes an array of plants as a parameter
    def __init__(self, grid, playerNumber, plants = []):
        self.plants = plants
        self.grid = grid
        self.player = playerNumber
        #number of plants set to the static numberStartingPlants
        self.numPlants = Parameters.fieldSize

        self.drawPlants()

    #prints out the stats of all the plants in your field
    def getPlants(self):
        print("Here is your field:\n")
        for i in range(len(self.plants)):
            plant = self.plants[i]
            print("HR:" + str(plant.heatResistance) + " CR:" + str(plant.coldResistance) + 
                  " DR:" + str(plant.diseaseResistance) + " Str:" + str(plant.strength) + 
                  " HP:" + str(plant.hitPoints)  + " Coords: (" +  str(plant.x + 1) + ", " + str(plant.y + 1) + ")" + "\n")

    #gets number of plants
    def getNumPlants(self):
        print (str(self.numPlants))
    
    #initializes a field by introducing what a field is and then initializing each plant
    #The result is stored into a new Field aptly titled field (remember where to put this for game mechanics)
    #The method ends by calling getPlants()
    def initializeField(grid, playerNumber):
        print("Each plant has four attributes: heat resistance, cold resistance, disease resistance, and strength.\nBefore selecting your values, remember, they must all add up to 10\n")
        plantArray = []
        for i in range(Parameters.fieldSize):
            placeholder = str(i + 1)
            print("Initializing plant #" + placeholder + ": ")
            plant = Plant.initializePlant(playerNumber)
            plantArray.append(plant)
        field = Field(grid, playerNumber, plantArray)
        field.getPlants()
        # field.drawPlants()
        return field

    #method that enacts plantLoss on each plant in field array
    def fieldLoss(self, environment, generation):
        print("Oh no, here comes the environment! The heat is now " + str(environment.temperature) + " degrees and the disease level is " + str(environment.disease) + "\n")
        for i in range(self.numPlants):
            self.plants[i].plantLoss(environment, generation)

    #method that makes two copies of plant with highest HP and adds it to the field
    #searches through array of plants and compares HP
    ##IMPORTANT MECHANIC: when it reproduces the new plants, it increases their strongest trait by 2
    def reproduceStrongestPlant(self):
        if (self.numPlants == 0):
            print ("You cannot reproduce! Your plants are dead!\n")
        else:
            print("Your strongest plant managed to reproduce " + str(Parameters.reproductionRate) + " times. With a bonus!\n")
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
            #creates copies of strongest plant, with its highest trait +2
            if (maxValueIndex == 0):
                heat += Parameters.reproductionImprovement
                """newPlantOne = Plant(heat, cold, disease, strength)
                newPlantTwo = Plant(heat, cold, disease, strength)"""
            elif (maxValueIndex == 1):
                cold += Parameters.reproductionImprovement
                """newPlantOne = Plant(heat, cold, disease, strength)
                newPlantTwo = Plant(heat, cold, disease, strength)"""
            elif (maxValueIndex == 2):
                disease += Parameters.reproductionImprovement
                """newPlantOne = Plant(heat, cold, disease, strength)
                newPlantTwo = Plant(heat, cold, disease, strength)"""
            else:
                strength += Parameters.reproductionImprovement
                """newPlantOne = Plant(heat, cold, disease, strength)
                newPlantTwo = Plant(heat, cold, disease, strength)"""

            # Find free spot on grid next to parent; if no free spot, then do not reproduce
            free_spots = []
            x = strongestPlant.x
            y = strongestPlant.y
            if x < FIELDWIDTH - 1 and self.grid.plant_list[x + 1][y] == 0:
                free_spots.append([x + 1, y])
            if x > 0 and self.grid.plant_list[x - 1][y] == 0:
                free_spots.append([x - 1, y])
            if y < FIELDHEIGHT - 1 and self.grid.plant_list[x][y + 1] == 0:
                free_spots.append([x, y + 1])
            if y > 0 and self.grid.plant_list[x][y - 1] == 0:
                free_spots.append([x, y - 1])

            for i in range(Parameters.reproductionRate):
                if len(free_spots) > 0:
                    x = free_spots[-1][0]
                    y = free_spots[-1][1]
                    free_spots.pop()

                    newPlant = Plant(heat, cold, disease, strength, x, y)
                    self.plants.append(newPlant)
                    self.numPlants += 1

    #method that removes any plant with less than 0 HP from the plants array
    def removeDeadPlants(self):
        temp = []
        for i in range (0, self.numPlants):
            if self.plants[i].hitPoints <= 0:
                temp.append(self.plants[i])
        for deadPlant in temp:
            x = deadPlant.x
            y = deadPlant.y
            self.grid.plant_list[x][y] = 0
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
        self.drawPlants()

    def drawPlants(self):
        for plant in self.plants:
            x = plant.x * BLOCKSIZE
            y = plant.y * BLOCKSIZE
            if self.player == 1 and self.grid.plant_list[plant.x][plant.y] == 0:
                self.grid.WIN.blit(self.grid.PLANT1, (x, y))
                self.grid.plant_list[plant.x][plant.y] = 1
            elif self.player == 2 and self.grid.plant_list[plant.x][plant.y] == 0:
                self.grid.WIN.blit(self.grid.PLANT2, (x, y))
                self.grid.plant_list[plant.x][plant.y] = 2
        pygame.display.update()