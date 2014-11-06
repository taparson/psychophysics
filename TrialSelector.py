from bge import logic
from random import randrange

def choose():
    control = logic.getCurrentController()
    string = 'VisA'+str(randrange(1,3))
    trial = control.actuators[string]
    control.activate(control.actuators['Edit Object'])
    control.activate(trial)
