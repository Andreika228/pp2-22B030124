#imports
import pygame, random, sys, snakecl
pygame.init()
FPS=pygame.time.Clock()

#screen
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('SNAKEGAME')
pygame.display.set_icon(pygame.image.load(r'Snake/image/snake.jpg'))

#loading fonts
font=pygame.font.Font(r'snake/font/ChangaOne-Regular.ttf',60)
font_small=pygame.font.Font(r'snake/font/ChangaOne-Regular.ttf',20)

#score
score=0

#level
level=1

#creatin snakeclass
snake=snakecl.Snake()

#snake increase
snake_list=[]
snake_length=1

#food
apple_x=random.randrange(0,500 - 60,20)
apple_y=random.randrange(0,500 - 60,20)

#catching food
def catch_food():
    global apple_x,apple_y, snake_length, score,level
    if (snake.x==apple_x and snake.y==apple_y) or (snake.x==apple_x-snake.speed and snake.y==apple_y-snake.speed) or (snake.x==apple_x+snake.speed and snake.y==apple_y+snake.speed) or (snake.x==apple_x+snake.speed and snake.y==apple_y-snake.speed) or (snake.x==apple_x-snake.speed and snake.y==apple_y+snake.speed):
        apple_x=random.randrange(0,500 - 60,20)
        apple_y=random.randrange(0,500 - 60,20)
        snake_length+=1
        score+=1
        if score%3==0:
            level+=1
        
        #sound of eating food
        pygame.mixer.Sound(r'snake/sound/applesound.mp3').play()

#gameover
game=True
def gameover():
    global snake,game
    if snake.x<0 or snake.x>500 or snake.y<0 or snake.y>500:
        game=False

        #sound of failing
        pygame.mixer.Sound(r'Snake/sound/fail.mp3').play()

#adding fonts
gg=font.render('GAME OVER',True,'white')
gg_button=font_small.render('press ESC to quit           press SPACE to restart',True,'white')

#game
while True:
    if game:
        #bg
        screen.fill('white')

        #food spawning
        pygame.draw.rect(screen,'blue',[apple_x,apple_y,20,20])

        #increaing snake and lose if eat tail
        snake_head=[]
        snake_head.append(snake.x)
        snake_head.append(snake.y)
        snake_list.append(snake_head)
        for i in snake_list[:-1]:
            if i==snake_head:
                game=False
                #sound of failing
                pygame.mixer.Sound(r'Snake/sound/fail.mp3').play()
        if len(snake_list)>snake_length:
            del snake_list[0]
        snake.draw(screen,snake_list)
        snake.change()

        #catching food
        catch_food()

        #levels continues
        
        lvl=font_small.render(f'LEVEL: {str(level)}',True,'black')
        screen.blit(lvl,(400,10))

        #score
        size=font_small.render(f'SIZE: {str(score)}',True,'black')
        screen.blit(size,(10,10))

        #checking if gameover
        gameover()

        #getting events
        for event in pygame.event.get():
            #exit
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            #movement of snake
            if event.type==pygame.KEYDOWN:
                snake.move(event)
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        #updating screen
        pygame.display.update()

        #FPS
        FPS.tick(20)

    
    #gameover screen
    if not game:

        #gameoverscreenbg
        screen.fill('black')
        screen.blit(gg,(105,200))
        screen.blit(gg_button,(90,265))

        #updating screen after failing
        pygame.display.update()

        #getting events
        for event in pygame.event.get():

            #exit
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            #restart
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    snake.refresh()
                    snake_list=[]
                    snake_length=1
                    level=1
                    checker=0
                    lvl_counter=3
                    score=0
                    game=True

                #new exit
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

