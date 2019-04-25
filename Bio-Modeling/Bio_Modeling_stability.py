import numpy as np
import matplotlib.pyplot as plt

leafyFactor = .2
herbFactor = .04
predFactor = .02

leafyMat = np.full((10,10), 100)
herbMat = np.full((10,10), 50)

turn = 0 

#max leafyPop = 100
leafyPop = 100
herbPop = 10
predPop = 1

def leafyGrowth():

    leafyConc = leafyPop / 100
    leafyInv = 1-leafyConc
    leafyGrowth = leafyPop * leafyFactor * leafyInv
    return leafyGrowth

def leafyConsumption():
    return herbPop

def herbGrowth():

    leafyConc = leafyPop / 100
    growth = herbPop * herbFactor*leafyConc
    return growth

def herbStarvation():

    leafyConc = leafyPop / 100

    if (leafyConc < .5):
        return .2 * herbPop
    elif (leafyConc < .2):
        return .4 * herbPop
    elif (leafyConc < .1):
        return .6*herbPop
    elif (leafyConc < .01):
        return .9*herbPop
    else:
        return 0

def predGrowth():

    predConc = predPop / herbPop
    predInv = 1-predConc
    growth = predPop * predFactor*predInv
    return growth

def predStarvation():
    predConc = predPop / herbPop

    if(predConc < .3):
        return 0
    elif(predConc > .3):
        return .1 * predPop
    elif(predConc > .4):
        return .2 * predPop
    elif(predConc > .5):
        return .5 * predPop


turn = 0

leafyList = []
herbList = []
predList = []

while turn < 500:
    turn +=1
    leafyPop = leafyPop + leafyGrowth()
    leafyPop = leafyPop - leafyConsumption()
    herbPop = herbPop + herbGrowth()
    herbPop = herbPop - herbStarvation()
    predPop = predPop + predGrowth()
    predPop = predPop - predStarvation()
    print()
    print()
    print("Turn: " + str(turn))
    print("Leaf: " + str(leafyPop))
    print("Herb: " + str(herbPop))
    leafyList.append(leafyPop)
    herbList.append(herbPop)
    predList.append(predPop)



plt.plot(leafyList)
plt.plot(herbList)
plt.plot(predList)
plt.show()
    