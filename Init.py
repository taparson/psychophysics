from bge import logic
from random import randrange


def init():
    logic.globalDict["saveString"] = '{"trials":['
    positions = []
    arrayList = []
    array1 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array2 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array1)
    arrayList.append(array2)
    
    array3 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array4 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array3)
    arrayList.append(array4)
    
    array5 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array6 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array5)
    arrayList.append(array6)
    
    array7 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array8 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array7)
    arrayList.append(array8)
    
    array9 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array10 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array9)
    arrayList.append(array10)
    
    array11 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array12 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array11)
    arrayList.append(array12)
    
    array13 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array14 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
    arrayList.append(array13)
    arrayList.append(array14)
    
    array15 = [(1,50),(-5,47),(.5,15),(-3,60),(-7,20),(6,35),(1,55)]
    array16 = [(-1,20),(5,23),(-0.5,55),(3,10),(7,50),(-6,35),(-1,15)]
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
    logic.globalDict["randNum"] = randrange(0,1000)
    
    print("hello")
    trial()
    
def trial():
    logic.globalDict["freeze"] = True
    if not logic.globalDict["hacky_bool"]:
        logic.globalDict["hacky_bool"] = True
        return
    logic.globalDict["hacky_bool"] = False
    if logic.globalDict["trial_number"] == 0:
        logic.globalDict["hacky_bool"] = True
    else:
        s = logic.globalDict["saveString"]
        logic.globalDict["saveString"] = s[:-1]
        logic.globalDict["saveString"] += ']'
    if not "game_start" in logic.globalDict:
        return
    logic.globalDict["trial_number"] += 1
    if logic.globalDict["trial_number"] > 2:
        logic.globalDict["saveString"] += '}]}'
        f = open('output'+str(logic.globalDict["randNum"]) + '.json', 'a')
        f.write(logic.globalDict["saveString"])
        f.close()
        logic.endGame()
        return
    controller = logic.getCurrentController()
    obj = controller.owner
    print("here! trial " + str(logic.globalDict["trial_number"])) 
    if logic.globalDict["trial_number"] != 1:
        logic.globalDict["saveString"] += '},'
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
    f.write(logic.globalDict["saveString"])
    f.close()
    logic.globalDict["saveString"] = ""
        