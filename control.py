import pigpio
from pygame import *
display.init()
scr = display.set_mode((720,480))
run = True
while run:
    for e in event.get():
        if e.type == KEYDOWN:
            if e.key == K_a:
                var = 17, 1800
            elif e.key == K_d:
                var = 17, 1200
            elif e.key == K_w:
                var = 18, 1600
            elif e.key == K_s:
                var = 18, 1400
            elif e.key == K_ESCAPE:
                var = 17, 0
                run = False        
        if e.type == KEYUP:
            if e.key in [K_a, K_d]:
                var = 17, 1500
            if e.key in [K_w, K_s]:
                var = 18, 1500
        pigpio.pi.set_servo_pulsewidth(var)
    time.wait(1)
pigpio.stop()
