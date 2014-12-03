from bge import logic
from random import randrange

def choose():
    if logic.globalDict["freeze"] is True:
        return
    control = logic.getCurrentController()
    #string = 'VisA1'
    #trial = control.actuators[string]
    #control.activate(control.actuators['Edit Object'])
    #control.a666ctivate(trial)
    # get the current scene
    scene = logic.getCurrentScene()
    
    # and use it to get a list of the objects in the scene
    objList = scene.objects
    
    objList["Bounds"].position = [0,0,-3]
    for i in range(7):
        curr = objList["Cylinder" + str(i+1)]
        curr.visible = True
        
def test():
    print("meow")