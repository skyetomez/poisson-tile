import pygame, sys
from pygame.locals import *


SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GREY = (211,211,211)


pygame.init
pygame.display.init

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)


running = True

clock = pygame.time.Clock()



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    
    
    

    pygame.display.flip
    clock.tick(60)

