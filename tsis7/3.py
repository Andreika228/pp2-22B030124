import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))

circle_x=200
circle_y=200
clock=pygame.time.Clock()

running=True
while running:
    circle=pygame.draw.circle(screen,'red',(circle_x,circle_y),radius=30)
    keyboard=pygame.key.get_pressed()



    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if keyboard[pygame.K_UP] and event.type==pygame.KEYUP and circle_y>40:
            circle_y-=20
        if keyboard[pygame.K_DOWN] and event.type==pygame.KEYUP and circle_y<360:
            circle_y+=20
        if keyboard[pygame.K_RIGHT] and event.type==pygame.KEYUP and circle_x<360:
            circle_x+=20
        if keyboard[pygame.K_LEFT] and event.type==pygame.KEYUP and circle_x>40:
            circle_x-=20
        screen.fill("white")
        clock.tick(60)