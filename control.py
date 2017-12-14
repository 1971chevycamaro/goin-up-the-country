import pygame
from car import steering, esc

pygame.display.init()
scr = pygame.display.set_mode((720,480))
run = True
while run:
  for e in pygame.event.get():
     if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_a:
          steering.setSteering(steering.getSteering() + 200)
        elif e.key == pygame.K_d:
          steering.setSteering(steering.getSteering() - 200)
        elif e.key == pygame.K_w:
          esc.setThrottle(esc.getThrottle() + 10)
        elif e.key == pygame.K_s:
          esc.setThrottle(esc.getThrottle() - 10)
        elif e.key == pygame.K_LSHIFT:
          esc.setThrottle(esc.getThrottle("base") * 2, "base")
        elif e.key == pygame.K_ESCAPE:
          run = False
     if e.type == pygame.KEYUP:
            if e.key in [pygame.K_a, pygame.K_d]:
                steering.setSteering("center")
            if e.key in [pygame.K_w, pygame.K_s]:
                esc.setThrottle("neutral")
  pygame.time.wait(1)
esc.setThrottle()
steering.setSteering()
