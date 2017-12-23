import pigpio
PI = pigpio.pi()
PIN = 18
def set_throttle(speed=1500, arg1=None, report_errors=False):
    '''sets ESC to desired throttle'''
    presets = ["forward", "backward", "neutral"]
    if arg1 == "base":
        PI.set_servo_pulsewidth(PIN, speed + 1500)
    if isinstance(speed, str) and speed in presets:
        pwm = [1600, 1400, 1500]
        PI.set_servo_pulsewidth(PIN, pwm[presets.index(speed)])
    elif isinstance(speed, int) and speed in range(1000, 2001):
        pwm = speed
        PI.set_servo_pulsewidth(PIN, pwm)
    #Error Handler
    else:
        if report_errors:
            print("speed is invalid or incorrect type %s" % type(speed))
def get_throttle(arg1=None):
    '''gets current ESC throttle in PWM or base'''
    if arg1 == "base":
        return PI.get_servo_pulsewidth(PIN) - 1500
    elif arg1 is None:
        return PI.get_servo_pulsewidth(PIN)
  