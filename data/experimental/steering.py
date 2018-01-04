import pigpio
reportErrors = False
def setSteering(direction):
  pin = 17
  presets = ["left","right","center"]
  if isinstance(speed, str) and speed in presets:
    pwm = [1800,1200,1500]
    pigpio.set_servo_pulsewidth(pin,pwm[presets.index(speed)])
  elif isinstance(speed, int) and speed in range(1000,2001):
    pwm = speed
    pigpio.set_servo_pulsewidth(pin,pwm)
  #Error Handler
  else:
    if reportErrors:
      print("direction is invalid or incorrect type %s" % type(direction))
