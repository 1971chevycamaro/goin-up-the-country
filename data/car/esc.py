'''a module designed to control an RC car's speed with PWM signals corresponding to how fast and
what direction the motor is spinning'''
import pigpio
import json
PIN = 18 if not ESC['PIN'] else ESC['PIN']
FORWARD = 1600 if not ESC['FORWARD'] else ESC['FORWARD']
BACKWARD = 1400 if not ESC['BACKWARD'] else ESC['BACKWARD']
NEUTRAL = 1500 if not ESC['NEUTRAL'] else ESC['NEUTRAL']
PI = pigpio.pi()
def set_throttle(speed="neutral", report_errors=True):
    '''sets ESC to desired throttle'''
    if speed in range(1000, 2001):
        pwm = speed
        PI.set_servo_pulsewidth(PIN, pwm)
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
