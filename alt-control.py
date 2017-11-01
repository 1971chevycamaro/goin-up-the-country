import pigpio, time # learn more: https://python.org/pypi/pigpio
from pygame as pg
pg.init()
maintimer = pg.clock.Clock()
maintimer.tick(24)
scr = pg.display.set_mode((100,100))
pwm = 1600
last_press = 0
if pg.key.get_pressed()[K_w]:
  span = time.time() - last_press
  last_press = time.time()
  if span < 0.5:
    pwm += 100
    throttle(pwm)
