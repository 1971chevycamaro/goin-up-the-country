'''a module designed to control an RC car's steering with PWM signals corresponding to servo
angles'''
import pigpio
PI = pigpio.pi()
PIN = 17
PWM_PRESETS = ["left", 1800, "right", 1200, "center", 1500]
def set_steering(direction="center", report_errors=True):
    '''sets steering to desired angle according to servo PWM'''
    if direction in range(1000, 2001):
        pwm = direction
        PI.set_servo_pulsewidth(PIN, pwm)
    elif direction in PWM_PRESETS:
        PI.set_servo_pulsewidth(PIN, PWM_PRESETS[PWM_PRESETS.index(direction) + 1])
    #Error Handler
    else:
        if report_errors:
            print("direction is invalid or incorrect type %s" % type(direction))
def get_steering():
    '''gets current steering angle in servo PWM'''
    return PI.get_servo_pulsewidth(PIN)
