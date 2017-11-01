print("importing modules...")
import pigpio
import pygame
from time import sleep
print("initiating window...")
pygame.init()
maintimer = pygame.clock.Clock()
maintimer.tick(24)
screen = pygame.display.set_mode((100,100))
quit = False
pi = pigpio.pi()
if not pi.connected:
    exit()
else:
    print("connected")
print("executing script...")
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                pi.set_servo_pulsewidth(17,1800)
            elif event.key == pygame.K_d:
                pi.set_servo_pulsewidth(17,1200)
            elif event.key == pygame.K_w:
                pi.set_servo_pulsewidth(18,1600)
            elif event.key == pygame.K_s:
                pi.set_servo_pulsewidth(18,1400)
            elif event.key == pygame.K_ESCAPE:
                pi.set_servo_pulsewidth(17,0)
                quit = True        
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_a, pygame.K_d]:
                pi.set_servo_pulsewidth(17,1500)
            if event.key in [pygame.K_w, pygame.K_s]:
                pi.set_servo_pulsewidth(18,1500)

pi.stop()
