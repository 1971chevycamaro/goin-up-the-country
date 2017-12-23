'''a module designed to control an RC car's speed with PWM signals corresponding to how fast and what direction the motor is spinning'''
import pigpio
PI = pigpio.pi()
PIN = 18
PWM_PRESETS = [1600, 1400, 1500]
def set_throttle(speed="neutral", arg1=None, report_errors=True):
    '''sets ESC to desired throttle'''
    presets = ["forward", "backward", "neutral"]
    if arg1 == "base":
        PI.set_servo_pulsewidth(PIN, speed + 1500)
    if speed in presets:
        PI.set_servo_pulsewidth(PIN, PWM_PRESETS[presets.index(speed)])
    elif speed in range(1000, 2001):
        pwm = speed
        PI.set_servo_pulsewidth(PIN, pwm)
    #Error Handler
    else:
        if report_errors:
            print("speed is invalid or incorrect type %s" % type(speed))
def get_throttle(arg0=None):
    '''gets current ESC throttle in PWM or base'''
    if arg0 == "base":
        return PI.get_servo_pulsewidth(PIN) - 1500
    elif arg0 is None:
        return PI.get_servo_pulsewidth(PIN)
def set_aux(aux_pin=15, aux_pwm=1000):
    '''sets aux wire state in PWM signals'''
    if aux_pwm in range(1000, 1901):
        PI.set_servo_pulsewidth(aux_pin, aux_pwm)
