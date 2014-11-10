from bge import logic
from random import randrange

def choose():
    control = logic.getCurrentController()
    string = 'VisA1'
    trial = control.actuators[string]
    control.activate(control.actuators['Edit Object'])
    control.activate(trial)
