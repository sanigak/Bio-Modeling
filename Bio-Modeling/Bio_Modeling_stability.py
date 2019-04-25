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
herbPop = 1
predPop = 2

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

turn = 0

leafyList = []
herbList = []

while turn < 500:
    turn +=1
    leafyPop = leafyPop + leafyGrowth()
    leafyPop = leafyPop - leafyConsumption()
    herbPop = herbPop + herbGrowth()
    print("grow: " + str(herbGrowth()))
    herbPop = herbPop - herbStarvation()
    print("strv: " + str(herbStarvation()))
    print()
    print()
    print("Turn: " + str(turn))
    print("Leaf: " + str(leafyPop))
    print("Herb: " + str(herbPop))
    leafyList.append(leafyPop)
    herbList.append(herbPop)

plt.plot(leafyList)
plt.plot(herbList)
plt.show()
    