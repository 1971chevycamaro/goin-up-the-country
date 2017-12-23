'''a module designed to control an RC car's steering with PWM signals corresponding to servo angles'''
import pigpio
PI = pigpio.pi()
PIN = 17
PWM_PRESETS = [1800, 1200, 1500]
def set_steering(direction="center", arg1=None, report_errors=True):
    '''sets steering to desired angle according to servo PWM'''
    presets = ["left", "right", "center"]
    if arg1 == "base":
        PI.set_servo_pulsewidth(PIN, direction + 1500)
    if direction in presets:
        PI.set_servo_pulsewidth(PIN, PWM_PRESETS[presets.index(direction)])
    elif direction in range(1000, 2001):
        pwm = direction
        PI.set_servo_pulsewidth(PIN, pwm)
    #Error Handler
    else:
        if report_errors:
            print("direction is invalid or incorrect type %s" % type(direction))
def get_steering(arg0=None):
    '''gets current steering angle in servo PWM'''
    if arg0 == "base":
        return PI.get_servo_pulsewidth(PIN) - 1500
    elif arg0 is None:
        return PI.get_servo_pulsewidth(PIN)
