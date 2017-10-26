import pigpio, pygame, time # learn more: https://python.org/pypi/pigpio
pwm = 1600
if pygame.key.get_pressed()[pygame.K_w]:
  endtime = time.time()
  if endtime-starttime < 0.5:
    pwm = pwm + 100
  else:
    pwm = 1600
  pigpio.pi().set_servo_pulsewidth(18,pwm)
else:
  starttime = time.time()
