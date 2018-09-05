#!/usr/bin/python
# -*- coding: utf-8 -*-

'''controls RC car'''

import atexit
import os
import threading
from time import sleep

import pygame

import car

ESC = car.esc
STRG = car.steering

RUN = True


def auto_stop(hostname):
    '''pings a hostname and stops the car if it fails'''

    while RUN:
        if not os.system('ping -c 1 -w2 ' + hostname
                         + ' > /dev/null 2>&1') == 0:
            ESC.brake(30) 
        sleep(0.5) # Wait half second before pinging hostname again.


def some_func(num, change=1, threshold=0):
    '''adds change if num is positive, subtracts change if num is negative'''

    return (num - change if num <= threshold else num + change)


car.set_defaults()

atexit.register(car.set_defaults)

# Initiate pygame display to capture keyboard inputs

pygame.display.init()
SCR = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Start a thread that checks for replies from googles ip, if none are recieved set the car to defaults.

t0 = threading.Thread(target=auto_stop, args=('8.8.8.8', ))
t0.start()

while RUN:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:

                # Steer left if the "a" key was pressed.

                STRG.set_steering(STRG.LEFT)
            elif e.key == pygame.K_d:

                # Steer right if the "d" key was pressed.

                STRG.set_steering(STRG.RIGHT)

            # Adjust steering trim.
            
            elif e.key == pygame.K_e:
                STRG.CENTER -= 20
            elif e.key == pygame.K_q:
                STRG.CENTER += 20

            elif e.key == pygame.K_w:

                # Go forward if the "w" key was pressed.

                ESC.set_throttle(ESC.FORWARD)
            elif e.key == pygame.K_s:

                # Go backward if the "s" key was pressed.

                ESC.set_throttle(ESC.BACKWARD)
            elif e.key == pygame.K_LSHIFT:

                # Magnify current throttle speed

                ESC.set_throttle(some_func(ESC.get_throttle(), 20,
                                           ESC.NEUTRAL))
            elif e.key == pygame.K_ESCAPE:

                # Stop this and t0's while loops if the "ESC" key was pressed.

                RUN = False

        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_a, pygame.K_d, pygame.K_e, pygame.K_q]:

                # Set steering to center position if the "a" or "d" key was pressed

                STRG.set_steering(STRG.CENTER)
            elif e.key in [pygame.K_w, pygame.K_s]:

                # Set current throttle to neutral if the "w" or "s" key was pressed

                ESC.set_throttle(ESC.NEUTRAL)

    pygame.time.wait(1)

t0.join()
