import pygame
from car import steering, esc
pygame.display.init()
SCR = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
RUN = True
esc.set_throttle()
steering.set_steering()
while RUN:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                steering.set_steering(steering.get_steering() + 200)
            elif e.key == pygame.K_d:
                steering.set_steering(steering.get_steering() - 200)
            elif e.key == pygame.K_w:
                esc.set_throttle(esc.get_throttle() + 10)
            elif e.key == pygame.K_s:
                esc.set_throttle(esc.get_throttle() - 10)
            elif e.key == pygame.K_LSHIFT:
                esc.set_throttle(esc.get_throttle("base") * 2, "base")
            elif e.key == pygame.K_ESCAPE:
                RUN = False
        if e.type == pygame.KEYUP:
            if e.key in [pygame.K_a, pygame.K_d]:
                steering.set_steering("center")
            elif e.key in [pygame.K_w, pygame.K_s]:
                esc.set_throttle("neutral")
    pygame.time.wait(1)
esc.set_throttle()
steering.set_steering()
