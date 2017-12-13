import time, threading, pigpio#, ease
pi = pigpio.pi()
pin = 18
def setThrottle(speed = 1500, arg1 = None, arg2 = None, reportErrors = False):
  presets = ["forward","backward","neutral"]
  if arg1 == "base":
    #print(pin, speed + 1500)
    pi.set_servo_pulsewidth(pin, speed + 1500)
  if isinstance(speed, str) and speed in presets:
    pwm = [1600,1400,1500]
    #print(pin, pwm[presets.index(speed)])
    pi.set_servo_pulsewidth(pin, pwm[presets.index(speed)])
  elif isinstance(speed, int) and speed in range(1000,2001):
    pwm = speed
    #print(pin, pwm)
    pi.set_servo_pulsewidth(pin, pwm)
  #Error Handler
  else:
    if reportErrors:
      print("speed is invalid or incorrect type %s" % type(speed))
def getThrottle(arg1 = None):
  if arg1 == "base":
    #print("pi.get_servo_pulsewidth(%s) - 1500" % pin)
    return pi.get_servo_pulsewidth(pin)
  elif arg1 == None:
    #print("pi.get_servo_pulsewidth(pin)")
    return pi.get_servo_pulsewidth(pin)
  
