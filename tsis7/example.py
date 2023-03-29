import pygame

pygame.init()
screen = pygame.display.set_mode((800,700))
screen.fill((0,0,0))
running = True
is_green = True
x=40
y=40
clock= pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            is_green=not is_green
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -=5
    if pressed[pygame.K_DOWN]: y +=5
    if pressed[pygame.K_LEFT]: x -=5
    if pressed[pygame.K_RIGHT]: x +=5
    
    screen.fill((0,0,0))
    if is_green:
        color=(0,255,0)
    else:
        color=(255,100,0)
    pygame.draw.rect(screen,color,pygame.Rect(x,y,100,100))
    
    pygame.display.flip() 
    clock.tick(60)       
