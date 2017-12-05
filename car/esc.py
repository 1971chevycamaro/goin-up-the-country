import pigpio
reportErrors = True
def setThrottle(speed):
  pin = 18
  presets = ["forward","backward","neutral"]
  if isinstance(speed, str) and speed in presets:
    pwm = [1600,1400,1500]
    pigpio.set_servo_pulsewidth(pin,pwm[presets.index(speed)])
  elif isinstance(speed, int) and speed in range(1000,2001):
    pwm = speed
    pigpio.set_servo_pulsewidth(pin,pwm)
  #Error Handler
  else:
    if reportErrors:
      print("speed is invalid or incorrect type %s" % type(speed))
def getThrottle():
  return pigpio.get_servo_pulsewidth(18)
