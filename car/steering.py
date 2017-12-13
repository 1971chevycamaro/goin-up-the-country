import pigpio
pi = pigpio.pi()
pin = 17
def setSteering(direction, arg1 = None, reportErrors = False):
  presets = ["left","right","center"]
  if arg1 == "base":
    #print(pin, direction + 1500)
    pi.set_servo_pulsewidth(pin, direction + 1500)
  if isinstance(direction, str) and direction in presets:
    pwm = [1800,1200,1500]
    #print(pin, pwm[presets.index(direction)])
    pigpio.set_servo_pulsewidth(pin,pwm[presets.index(direction)])
  elif isinstance(direction, int) and direction in range(1000,2001):
    pwm = direction
    #print(pin, pwm)
    pigpio.set_servo_pulsewidth(pin,pwm)
  #Error Handler
  else:
    if reportErrors:
      print("direction is invalid or incorrect type %s" % type(direction))
def getSteering(arg1 = None):
  if arg1 == "base":
    #print("pi.get_servo_pulsewidth(%s) - 1500" % pin)
    return pi.get_servo_pulsewidth(pin)
  elif arg1 == None:
    #print("pi.get_servo_pulsewidth(%s)" % pin)
    return pi.get_servo_pulsewidth(pin)
