#!/usr/bin/python3
import pygame
import car
ESC = car.esc
STRG = car.steering
car.set_defaults()
pygame.display.init()
SCR = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
RUN = True
while RUN:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                STRG.set_steering(STRG.get_steering() + 200)
            elif e.key == pygame.K_d:
                STRG.set_steering(STRG.get_steering() - 200)
            elif e.key == pygame.K_w:
                ESC.set_throttle(ESC.get_throttle() + 100)
            elif e.key == pygame.K_s:
                ESC.set_throttle(ESC.get_throttle() - 100)
            elif e.key == pygame.K_LSHIFT:
                ESC.set_throttle(ESC.get_throttle("base") + 20, "base")
            elif e.key == pygame.K_ESCAPE:
                RUN = False
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_a, pygame.K_d]:
                STRG.set_steering("center")
            elif e.key in [pygame.K_w, pygame.K_s]:
                ESC.set_throttle("neutral")
    pygame.time.wait(1)
