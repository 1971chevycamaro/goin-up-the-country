# goin-up-the-country

Go anywhere with a raspberry-pi onboard a hobby-class remote control car.

### Setup
---
requirements:
- raspberrypi with internet connection (raspberrypi zero w used here)
- VNC viewer

#### wiring

note:

- all pins are being reffered to by their Broadcom numbers
- the pins to control the devices can be reassigned in the included settings.json file

GPIO18 is is for the ESC **by default**
GPIO17 is for the steering servo **by default**
GPIO15 is an auxiliary wire designed for use in Castle Creations ESC's when applicable, don't plug anything in there other than that.

Each 5v and GND(Ground/Negative) wire on the servo connectors belongs to the corresponding pin on the raspberrypi, see raspberrypi pinout below.
![alt text](https://pinout.xyz/resources/raspberry-pi-pinout.png "raspberrypi pinout")

**software**
Extract [goin-up-the-country.zip](https://github.com/1971chevycamaro/goin-up-the-country/archive/master.zip) to your Raspbian desktop. To run just go into a terminal - make sure you're in /home/pi by doing `cd ~`, type `sh Desktop/goin*/run.sh` and you can start moving! use the controls to move.

### Controls
---
controls are typical to any video game:
controls are 'w' to move forward, 'a' to turn left, 's' to move backwards, and 'd' to turn right. Press the Escape key to exit the program.

mashing 'shift' will increase throttle, release 'w' to reset to default speed

#### Adjustments

There is a settings.json file which can be used to tune the movement of the car. To fix a car that accelerates to quickly you would reduce the ESC "FORWARD" value preferably in 10 microsecond increments. Values closer to 1500 express lower power output or servo extension.

## If you want to contribute:
Go ahead! Although I must say that I'm new to this and I'm trying to learn how to use GitHub, please help me out I can't do this myself, it's taking to long. 

Check out the issues to see what needs to be done.
