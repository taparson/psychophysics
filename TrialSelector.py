from bge import logic
from random import randrange

def choose():
    control = logic.getCurrentController()
    #string = 'VisA1'
    #trial = control.actuators[string]
    #control.activate(control.actuators['Edit Object'])
    #control.activate(trial)
    # get the current scene
    scene = logic.getCurrentScene()
    
    # and use it to get a list of the objects in the scene
    objList = scene.objects
    
    objList["Bounds"].position = [0,5,-3]
    for i in range(7):
        curr = objList["Cylinder" + str(i+1)]
        curr.visible = True