import pygame
import sys
from spaceship import Spaceship


def beg():
    
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Давай,стреляй,если сможешь")
    spaceship = Spaceship(screen)

    running =True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        screen.fill((0,0,0))
        spaceship.out()
        pygame.display.flip()
            

beg()

   