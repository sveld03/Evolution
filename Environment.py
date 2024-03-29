import random
from config import Parameters

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
        temperature = random.randint(50, 90)
        disease = random.randint (0, 10)
        environment = Environment(temperature, disease)
        return environment
    
    def getImpactScalar():
        #makes toggleable a random magnitude of impact of a player's actions
        one = Parameters.randomEnvironmentImpactScalarRange[0]
        two = Parameters.randomEnvironmentImpactScalarRange[1]
        if (Parameters.playerRandomEnvironmentImpact):
            return random.randint(one, two)
        else:
            return 1

    def makeHotter(self):
        self.temperature +=  (Environment.getImpactScalar() * (Parameters.playerImpactOnTemperature))

    def makeColder(self):
        self.temperature -= (Environment.getImpactScalar() * (Parameters.playerImpactOnTemperature))
    
    def increaseDisease(self):
        self.disease += (Environment.getImpactScalar() * (Parameters.playerImpactOnDisease))

    def decreaseDisease(self):
        self.disease -= (Environment.getImpactScalar() * (Parameters.playerImpactOnDisease))