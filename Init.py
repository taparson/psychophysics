from bge import logic
from random import randrange
import random

def init():
    logic.globalDict["randNum"] = randrange(0,1000)
    random.seed(0)
    logic.globalDict["saveString"] = '{"trials":['
    positions = []
    arrayList = []

 array15 = [2,17;4,24;-1,25;-4,32;4,38;-4,52;4,54];
 array16 = [-2,53;-4,46;1,45;4,38;-4,32;4,18;-4,16];

    array1 = [(1,50),(-5,47),(1,15),(-3,60),(-7,20),(6,35),(1,55)]
    array2 = [(-1,20),(5,23),(-1,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array1)
    arrayList.append(array2)
    
    array3 = [(-2, 4), (4, 18), (3, 28), (4, 33), (-1, 38), (-5, 55), (4, 62)]
    array4 = [(2, 66), (-4, 52), (-3, 42), (-4, 37), (1, 32), (5, 15), (-4, 8)]
    arrayList.append(array3)
    arrayList.append(array4)
    
    array5 = [(-2.5, 9), (4, 28), (3, 38), (-7, 42), (-7, 63), (3, 64), (8, 43)]
    array6 = [(2.5, 61), (-4, 42), (-3, 32), (7, 28), (7, 7), (-3, 6), (-8, 27)]
    arrayList.append(array5)
    arrayList.append(array6)
    
    array7 = [(3, 8), (-4, 15), (-2, 33), (2, 38), (7, 35), (-2, 54), (7, 65)]
    array8 = [(-3, 62), (4, 55), (2, 37), (-2, 32), (-7, 35), (2, 16), (-7, 5)]
    arrayList.append(array7)
    arrayList.append(array8)
    
    array9 = [(-6, 13), (4, 13), (2, 24), (-2, 25), (3, 45), (-7, 55), (6, 66)]
    array10 = [(6, 57), (-4, 57), (-2, 46), (2, 45), (-3, 25), (7, 15), (-6, 4)]
    arrayList.append(array9)
    arrayList.append(array10)
    
    array11 = [(-1, 11), (-6, 22), (3, 21), (-1, 44), (7, 42), (4, 57), (-3, 64)]
    array12 = [(1, 59), (6, 48), (-3, 49), (1, 26), (-7, 28), (-4, 13), (3, 6)]
    arrayList.append(array11)
    arrayList.append(array12)
    
    array13 = [(-2 ,17), (-7, 26), (2, 33), (6, 46), (3, 53), (-1, 66), (-3, 45)]
    array14 = [(2, 53), (7, 44), (-2, 37), (-6, 24), (-3, 17), (1, 4), (3, 25)]
    arrayList.append(array13)
    arrayList.append(array14)
    
    array15 = [(2, 17), (4, 24), (-1, 25), (-4, 32), (4, 38), (-4, 52), (4, 54)]
    array16 = [(-2, 53), (-4, 46), (1, 45), (4, 38), (-4, 32), (4, 18), (-4, 16)]
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
    
    logic.globalDict["positions"] = finalRandList
    logic.globalDict["game_start"] = True
    logic.globalDict["trial_number"] = 0
    logic.globalDict["prev_time"] = 0
    logic.globalDict["prev_pos"] = (0,0)
    logic.globalDict["hacky_bool"] = True
    logic.globalDict["freeze"] = True
    
    print("hello")
    trial()
    
def trial():
    logic.globalDict["freeze"] = True
    s = logic.globalDict["saveString"]
    if not "game_start" in logic.globalDict:
        return
    if not logic.globalDict["hacky_bool"]:
        logic.globalDict["hacky_bool"] = True
        return
    logic.globalDict["hacky_bool"] = False
    if logic.globalDict["trial_number"] == 0:
        logic.globalDict["hacky_bool"] = True
    else:
        s = s[:-1]
        s += ']'
    logic.globalDict["trial_number"] += 1
    if logic.globalDict["trial_number"] > 2:
        s += '}]}'
        f = open('output'+str(logic.globalDict["randNum"]) + '.json', 'a')
        f.write(s)
        f.close()
        logic.endGame()
        return
    controller = logic.getCurrentController()
    obj = controller.owner
    print("here! trial " + str(logic.globalDict["trial_number"])) 
    if logic.globalDict["trial_number"] != 1:
        s += '},'
    logic.globalDict["saveString"] = ""
    logic.globalDict["saveString"] += '{"number":' + str(logic.globalDict["trial_number"]) + ','
    logic.globalDict["saveString"] += '"obstacles": ['
    
    # get the current scene
    scene = logic.getCurrentScene()
    
    # and use it to get a list of the objects in the scene
    objList = scene.objects
    
    currPositions = logic.globalDict["positions"]
    currPositions = currPositions[logic.globalDict["trial_number"]]
    
    for i in range(7):
        string = "Cylinder" + str(i+1) 
        curr = objList[string]
        (x,y) = currPositions[i]
        curr.position = [x,y,0]
        curr.visible = False
        logic.globalDict["saveString"] += '{"number": ' + str(i+1) + ',"location": [' + str(x) + ',' + str(y) + ']}'
        if i != 6:
            logic.globalDict["saveString"] += ','
        test = "meow"       
	
    test = "woof"
    logic.globalDict["saveString"] += '],'
    logic.globalDict["saveString"] += '"output":['
        
    #objList["A1"].visible = False
    #print(objList["A1"].visible)
    objList["Bounds"].position = [0,0,3]
    objList["Body"].position = [0,0,7]
    objList["Body"].orientation = [0,0,0]
    camera = objList["Camera"]
    camera.orientation = [1.57,0,0]
        
    logic.globalDict["prev_time"] = 0
    logic.globalDict["prev_pos"] = (0,0)
    camera["timer"] = 0
    f = open('output' + str(logic.globalDict["randNum"]) + '.json','a')
    f.write(s)
    f.close()
    logic.globalDict["trial_start"] = True
        
