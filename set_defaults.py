#!/usr/bin/python3
# file can be executed at startup to calm  down the electronics
# note that the file can move because it will no longer be able to import the module 'car'
# to execute on startup, nano .bashrc and at the very bottom place:
# sudo pigpiod
# python3 /home/pi/Desktop/goin*/extra/set_defaults.py
import car
car.set_defaults()
