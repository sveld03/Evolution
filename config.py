class Parameters(object):
    fieldSize = 3
    turns = 3
    playerImpactOnTemperature = 2
    playerImpactOnDisease = 1
    playerRandomEnvironmentImpact = False
    randomEnvironmentImpactScalarRange = [0, 2]
    #put a double to scale strength by
    strengthImpactOnHitpoints = 0.5
    reproductionRate = 2
    reproductionImprovement = 2
    playerImpactOnPlants = 1

WIDTH, HEIGHT = 700, 700
FIELDWIDTH = 6
FIELDHEIGHT = 6

FPS = 30