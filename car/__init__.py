'''contains modules with means of altering state of RC car'''
import car.esc as ESC
import car.steering as STRG
def set_defaults():
    '''sets all signals to default'''
    ESC.set_aux()
    ESC.set_throttle()
    STRG.set_steering()
