import numpy as np
import matplotlib.pyplot as plt
import random

leafyFactor = .15
herbFactor = .5
predFactor = .7

leafyMat = np.full((10,10), 100)
herbMat = np.full((10,10), 50)

turn = 0 

#max leafyPop = 100
leafyPop = 80
herbPop = 5
predPop = .5

def leafyGrowth():

    leafyConc = leafyPop / 100
    leafyInv = 1-leafyConc
    leafyGrowth = leafyPop * leafyFactor * leafyInv
    randy = random.uniform(.9, 1.1)
    return leafyGrowth * randy

def leafyConsumption():
    return herbPop/3

def herbGrowth(herbPop):

    leafyConc = leafyPop / 100
    growth = herbPop * herbFactor*leafyConc
    randy = random.uniform(.9, 1.1)
    return growth * randy

def herbStarvation():

    leafyConc = leafyPop / 100
    leafyInv = 1-leafyConc

    randy = random.uniform(.9, 1.1)
    return (leafyInv*herbPop)*randy*leafyInv/2

def herbPredation():

    randy = random.uniform(.9, 1.1)
    return predPop*randy

def predGrowth(predPop):

    predConc = predPop / herbPop
    predInv = 1-predConc
    growth = predPop * predFactor*predInv
    randy = random.uniform(.9, 1.1)
    return growth*randy

def predStarvation():

    predConc = predPop / herbPop
    randy = random.uniform(.9, 1.1)
    return predPop*predConc*randy


turn = 0

leafyList = [80,80]
herbList = [5,5]
predList = [.5,.5]

while turn < 1000:
    turn +=1
    print("Turn: " + str(turn))
    leafyPop = leafyPop + leafyGrowth()
    print("Leafy growth: " + str(leafyGrowth()))
    leafyPop = leafyPop - leafyConsumption()
    print("Leafy cons: " + str(leafyConsumption()))
    if (leafyPop > 100):
        leafyPop = 100
    if (leafyPop < 0):
        leafyPop = 1

    herbPop = herbPop + herbGrowth(herbList[-2])
    print()
    print("Herb growth: " + str(herbGrowth(herbList[-2])))
    herbPop = herbPop - herbStarvation()
    print("Herb starv: " + str(herbStarvation()))
    herbPop = herbPop - herbPredation()
    print("Herb pred: " + str(herbPredation()))
    if (herbPop < 0):
        herbPop = .002

    predPop = predPop + predGrowth(predList[-2])
    print()
    print("Pred growth: " + str(predGrowth(predList[-2])))
    predPop = predPop - predStarvation()
    print("Pred starv: " + str(predStarvation()))
    if (predPop < 0):
        print("blern")
        predPop = .001

    print()
    print()
    
    print("Leaf: " + str(leafyPop))
    print("Herb: " + str(herbPop))
    print("Pred: " + str(predPop))
    print()
    print()
    print()
    print()
    print()
    print()
    leafyList.append(leafyPop)
    herbList.append(herbPop)
    predList.append(predPop)



plt.plot(leafyList, label = "Leafy")
plt.plot(herbList, label = "Herb")
plt.plot(predList, label = "Pred")
plt.legend()
plt.show()
    