import pygame
import datetime
now=datetime.datetime.now()
now_sec=int(now.second)
now_min=int(now.minute)
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((700,525))
icon=pygame.image.load(r'image/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Часы')
bg=pygame.image.load(r'image/bg.png').convert_alpha()
s=pygame.image.load(r'image/bigarm1.png').convert_alpha()
m=pygame.image.load(r'image/miniarm1.png').convert_alpha()
angle_sec=(-1)*now_sec*6
angle_min=(-1)*now_min*6
running=True
m_true=True
while running:
    angle_min-=0.1
    angle_sec-=6
    rotated_sec=pygame.transform.rotate(s,angle_sec)
    rotated_sec_rect=rotated_sec.get_rect(center=(350,262.5))
    rotated_min=pygame.transform.rotate(m,angle_min)
    rotated_min_rect=rotated_min.get_rect(center=(350,262.5))
    screen.blit(bg,(0,0))
    screen.blit(rotated_sec,rotated_sec_rect)
    screen.blit(rotated_min,rotated_min_rect)
    
    
    




    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
