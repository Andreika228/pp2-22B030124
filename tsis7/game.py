import pygame,controller
from spaceship import Spaceship
from pygame.sprite import Group 
from stats import Stats
from score import Score
def beg():
    
    pygame.init()
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption("Давай,стреляй,если сможешь")
    spaceship = Spaceship(screen)
    icon =pygame.image.load(r"image/icon_for_spaceship.png")
    pygame.display.set_icon(icon)
    bullets = Group()
    evils = Group()
    controller.create_evils(screen,evils)
    stats = Stats()
    sc = Score(screen,stats)

    while True:
        controller.events(screen, spaceship, bullets) 
        if stats.run_game:
            spaceship.update_spaceship()
            controller.update(screen,stats,sc,spaceship,evils,bullets)
            controller.update_bullets(screen,stats,sc,evils,bullets)
            controller.update_evils(stats,screen,spaceship,evils,bullets)
            

beg()

   