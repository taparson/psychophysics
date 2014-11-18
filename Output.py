from bge import logic
from random import randrange

def outputData():
    f = open("output.txt",'a')
    control = logic.getCurrentController()
    camera = control.owner
    #print(camera.position)
    #print(camera.y)
    #print("next")
    f.write(str(camera.position.x) + "," + str(camera.position.y)+'\n')
    f.close()