from bge import render as r
import math

cont = bge.logic.getCurrentController()
own = cont.owner
mouse = cont.sensors["Mouse"]
parent = own.parent

#set speed for camera movement
sensitivity = 0.05

#set camera rotation limits
high_limit = 180
low_limit = 0

h = r.getWindowHeight()//2
w = r.getWindowWidth()//2
x = (h - mouse.position[0])*sensitivity
y = (w - mouse.position[1])*sensitivity

if own["startup"]:
    r.setMousePosition(h, w)
    own ["startup"] = False
else:
    rot = own.localOrientation.to_euler()
    pitch = abs(math.degrees(rot[0]))
    if high_limit > (pitch+y) > low_limit:
        pitch += y
    elif (pitch+y) < low_limit:
        pitch = low_limit
    elif (pitch+y) > high_limit:
        pitch = high_limit
    rot[0] = math.radians(pitch)
    own.localOrientation = rot.to_matrix()

    parentRot = parent.localOrientation.to_euler()
    yaw = math.degrees(parentRot[2]) + x
    parentRot[2] = math.radians(yaw)
    parent.localOrientation = parentRot.to_matrix()

    r.setMousePosition(h, w)