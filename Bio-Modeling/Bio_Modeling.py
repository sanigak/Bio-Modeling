import numpy as np

leafyGrowth = .04
herbGrowth = .10
predGrowth = .05

leafyMat = np.full((10,10), 100)
herbMat = np.full((10,10), 50)

turn = 0 


leafyPop = 100
herbPop = 10
predPop = 2


while turn < 100:
    turn+=1
    leafyChange = (leafyPop * leafyGrowth) - herbPop
    print("LEAFY: " + str(leafyChange))
    if leafyPop > abs(leafyChange):
        leafyPop = leafyPop + leafyChange
        herbPop = (herbPop * herbGrowth) + herbPop
    else:
        leafyPop = 1
        herbPop = herbPop+leafyChange
    print()
    print()
    print("Turn: " + str(turn))
    print("Leafs: " + str(leafyPop))
    print("Herbs: " + str(herbPop))
    