from bge import logic
from random import randrange

global positions = []

def init():
    arrayList = []
    array1 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array2 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array1)
    arrayList.append(array2)
    
    array3 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array4 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array3)
    arrayList.append(array4)
    
    array5 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array6 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array5)
    arrayList.append(array6)
    
    array7 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array8 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array7)
    arrayList.append(array8)
    
    array9 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array10 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array9)
    arrayList.append(array10)
    
    array11 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array12 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array11)
    arrayList.append(array12)
    
    array13 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array14 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array13)
    arrayList.append(array14)
    
    array15 = [(50,1),(47,-5),(15,0.5),(60,-3),(20,-7),(35,6),(75,1)]
    array16 = [(50,-1),(53,5),(85,-0.5),(40,3),(80,7),(65,-6),(25,-1)]
    arrayList.append(array15)
    arrayList.append(array16)
    
    randList = []
    finalRandList = []
    for i in range(16):
        for j in range(4):
            randList.append(i+1)
    
    while(len(randList) > 0):
        num = randrange(0,len(randList))
        finalRandList.append(arrayList[randList[num]-1])
        randList.pop(num)
        
    positions = finalRandList
    
    print("hello")
    
def trial():
    
    controller = logic.getCurrentController()
    obj = controller.owner

    # get the current scene
    scene = logic.getCurrentScene()
    
    # and use it to get a list of the objects in the scene
    objList = scene.objects
    
    currPositions = positions[logic.trial_number]
    
    for i in range(7):
        string = "Cylinder" + str(i+1) 
        curr = objList[string]
        (x,y) = currPositions[i]
        obj.position = [x,y,0]
        
    logic.trial_number += 1