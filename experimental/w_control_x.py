import pigpio, threading
import time as tm
from pygame import *
def timer(str):
    if str == "start":
        global start
        start = tm.time()
    elif str == "stop":
        return tm.time() - start
def throttle(ms):
  if ms in range(1000,2000):
    #pigpio.pi().set_servo_pulsewidth(18,ms)
    print(ms)
def loop():
  while True:
    throttle(pwm)
    tm.sleep(1)
display.init()
scr = display.set_mode((100,100))
run = True
timer("start")
pwm = 1500
t1 = threading.Thread(target=loop, args=())
t1.start()
while run:
  for e in event.get():
    if e.type == KEYDOWN:
      if e.key == K_w:
        if timer("stop") < 0.5:
          pwm += 100
        else:
          pwm = 1500
      elif e.key == K_ESCAPE:
          run = False
    if e.type == KEYUP:
      if e.key == K_w:
        timer("start")
        #throttle(pwm)
  time.wait(1)    
