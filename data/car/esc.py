#!/usr/bin/python
# -*- coding: utf-8 -*-
'''a module designed to control an RC car's speed with PWM signals corresponding to how fast and
what direction the motor is spinning, can be tethered to a .json file for configuration'''

import json
import os
from time import sleep

import pigpio


SCRIPT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(SCRIPT_DIR, '../../settings.json')
DATA = json.load(open(FILE_PATH))

ESC = DATA['ESC']

PIN = (18 if not ESC['PIN'] else ESC['PIN'])
FORWARD = (1600 if not ESC['FORWARD'] else ESC['FORWARD'])
BACKWARD = (1400 if not ESC['BACKWARD'] else ESC['BACKWARD'])
NEUTRAL = (1500 if not ESC['NEUTRAL'] else ESC['NEUTRAL'])
BRAKES = (False if not ESC['BRAKES'] else ESC['BRAKES'])

PI = pigpio.pi()


def set_throttle(speed=NEUTRAL, report_errors=True):
    '''sets ESC to desired throttle'''

    if speed in range(1000, 2001):
        pwm = speed
        PI.set_servo_pulsewidth(PIN, pwm)
    else:

        # Error Handler

        if report_errors:
            print('speed is invalid or incorrect type %s, speed: %s'
                  % (type(speed), speed))


def get_throttle():
    '''gets current ESC throttle in PWM'''

    return PI.get_servo_pulsewidth(PIN)


def brake(force_percent=25):
    '''brakes a certain force according to force_percent'''

    if all(((force_percent != 0), BRAKES, (force_percent in range(101)))):

        # Do the brake thing if it's enabled, not zero and is a percent.

        PI.set_servo_pulsewidth(PIN, 1600)
        sleep(0.01)  # Sleep to make sure that the ESC doesn't think that it's noise
        PI.set_servo_pulsewidth(PIN, (-1 * (force_percent / 100) * 500) + 1500)
    elif force_percent == 0:

        # If percent is zero coast. Doesn't work in main if statement because it will breifly move forward and potentially cause damage.

        pass


def set_aux(aux_pin=15, aux_pwm=1000):
    '''sets aux wire state in PWM signals'''

    if aux_pwm in range(1000, 1901):
        PI.set_servo_pulsewidth(aux_pin, aux_pwm)
