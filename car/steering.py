import pigpio
PI = pigpio.pi()
PIN = 17
def set_steering(direction="neutral", arg1=None, report_errors=False):
    '''sets steering to desired angle according to servo PWM'''
    presets = ["left", "right", "center"]
    if arg1 == "base":
        PI.set_servo_pulsewidth(PIN, direction + 1500)
    if isinstance(direction, str) and direction in presets:
        pwm = [1800, 1200, 1500]
        PI.set_servo_pulsewidth(PIN, pwm[presets.index(direction)])
    elif isinstance(direction, int) and direction in range(1000, 2001):
        pwm = direction
        PI.set_servo_pulsewidth(PIN, pwm)
    #Error Handler
    else:
        if report_errors:
            print("direction is invalid or incorrect type %s" % type(direction))
def get_steering(arg1=None):
    '''gets current steering angle in servo PWM'''
    if arg1 == "base":
        return PI.get_servo_pulsewidth(PIN) - 1500
    elif arg1 is None:
        return PI.get_servo_pulsewidth(PIN)
