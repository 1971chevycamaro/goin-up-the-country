'''a module designed to control an RC car's speed with PWM signals corresponding to how fast and
what direction the motor is spinning'''
import pigpio
PI = pigpio.pi()
PIN = 18
PWM_PRESETS = ["forward", 1600, "backward", 1400, "neutral", 1500]
def set_throttle(speed="neutral", report_errors=True):
    '''sets ESC to desired throttle'''
    if speed in range(1000, 2001):
        pwm = speed
        PI.set_servo_pulsewidth(PIN, pwm)
    elif speed in PWM_PRESETS:
        PI.set_servo_pulsewidth(PIN, PWM_PRESETS[PWM_PRESETS.index(speed) + 1])
    #Error Handler
    else:
        if report_errors:
            print("speed is invalid or incorrect type %s, speed: %s" % (type(speed), speed))
def get_throttle():
    '''gets current ESC throttle in PWM'''
    return PI.get_servo_pulsewidth(PIN)
def set_aux(aux_pin=15, aux_pwm=1000):
    '''sets aux wire state in PWM signals'''
    if aux_pwm in range(1000, 1901):
        PI.set_servo_pulsewidth(aux_pin, aux_pwm)
