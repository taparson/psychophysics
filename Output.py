from bge import logic
from random import randrange

def outputData():
    if not "game_start" in logic.globalDict:
        return
    
    control = logic.getCurrentController()
    camera = control.owner
    #print(camera.position)
    #print(camera.y)
    #print("next")
    
    scene = logic.getCurrentScene()
    objList = scene.objects
    body = objList["Body"]
    
    if logic.globalDict["freeze"]:
        if camera["timer"] > 3:
            logic.globalDict["freeze"] = False
            camera["timer"] = 0
        body.position = [0,0,.7]
        body.orientation = [0,0,0]
        camera.orientation = [1.57,0,0]
        return
    
    #camera = objList["Camera"]
    orr = camera.orientation
    #print(orr)
    x = -1.0*orr[1][0]
    y = -1.0*orr[1][1]
    z = -1.0*orr[1][2]
    
    deltTime = camera["timer"] - logic.globalDict["prev_time"]
    if deltTime == 0:
        return
    (xPrev,yPrev) = logic.globalDict["prev_pos"]
    deltX = camera.position.x - xPrev
    deltY = camera.position.y - yPrev
    velocity = [deltX/deltTime, deltY/deltTime]
    
    logic.globalDict["saveString"] += '{"time":' + str(camera["timer"]) + ','
    logic.globalDict["saveString"] += '"position":[' + str(camera.position.x) + "," + str(camera.position.y) + '],'
    logic.globalDict["saveString"] += '"look":[' + str(x) + ',' + str(y) + ',' + str(z) + '],'
    logic.globalDict["saveString"] += '"velocity":[' + str(velocity[0]) + ',' + str(velocity[1]) + ']}'
    
    logic.globalDict["prev_time"] = camera["timer"]
    logic.globalDict["prev_pos"] = (camera.position.x,camera.position.y)
    logic.globalDict["saveString"] += ','