import pygame,controller
import sys
from bullet import Bullet
from evil import Evil
import time 
def events(screen,spaceship,bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    spaceship.moveright = True
                elif event.key == pygame.K_a:
                    spaceship.moveleft = True
                elif event.key == pygame.K_SPACE:
                    newbullet= Bullet (screen ,spaceship)
                    bullets.add(newbullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    spaceship.moveright = False
                elif event.key == pygame.K_a:
                    spaceship.moveleft = False
def update(screen,stats,sc,spaceship,evils, bullets):
    screen.fill((0,0,0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.out()
    evils.draw(screen)
    pygame.display.flip()

def spaceship_kill(stats,screen, spaceship,evils,bullets):
    if stats.helth >0:
        stats.helth -= 1
        evils.empty()
        bullets.empty()
        create_evils(screen,evils)
        spaceship.create_spaceship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()
    
   
def update_bullets(screen,stats,sc,evils,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets,evils,True,True)
    if collisions:
        for evils in collisions.values():
            stats.score += 10* len(evils)
            sc.image_score()
    if len(evils) == 0:
        bullets.empty()
        create_evils(screen,evils)
        

def update_evils(stats,screen,spaceship,evils,bullets):
    evils.update()
    if pygame.sprite.spritecollideany(spaceship, evils):
        spaceship_kill(stats,screen,spaceship,evils,bullets)
    evils_check(stats,screen,spaceship,evils,bullets)

def evils_check(stats,screen,spaceship,evils,bullets):
    screen_rect =screen.get_rect()
    for evil in evils.sprites():
        if evil.rect.bottom >= screen_rect.bottom:
            spaceship_kill(stats,screen,spaceship,evils,bullets)
            break     

def create_evils(screen, evils):
    evil = Evil(screen)
    evil_width = evil.rect.width
    number_evil_x=int((800 - 2*evil_width)/evil_width)
    evil_height = evil.rect.height
    number_evil_y=int((600-2*evil_height)/evil_height)
    
    for row_number in range(number_evil_y):
        for number_evil in range(number_evil_x):
            evil = Evil(screen)
            evil.x = evil_width + evil_width * number_evil
            evil.y =evil_height +evil_height * row_number
            evil.rect.x = evil.x
            evil.rect.y = evil.rect.height + evil.rect.height * row_number
            evils.add(evil)  

def check_hight_score(stats,sc):
    if  stats.score >stats.hight_score:
        stats.hight_score = stats.score  
        sc.image_hight_score()
    
    
    