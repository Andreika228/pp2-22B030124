import pygame
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x=500/2-10
        self.y=500/2-10
        self.x_change=0
        self.y_change=-10
        self.speed=10
        self.color=200
    def move(self,event):
        if event.key==pygame.K_a:
                self.x_change=-self.speed
                self.y_change=0
        elif event.key==pygame.K_d:
                self.x_change=self.speed
                self.y_change=0
        elif event.key==pygame.K_w:
                self.x_change=0
                self.y_change=-self.speed
        elif event.key==pygame.K_s:
                self.x_change=0
                self.y_change=self.speed
    def draw(self,screen,snakelist):
        for i in snakelist:
            pygame.draw.rect(screen,'green',[i[0],i[1],20,20])
    def change(self):
        self.x+=self.x_change
        self.y+=self.y_change
    def refresh(self):
        self.x=500/2-10
        self.y=500/2-10
        self.x_change=0
        self.y_change=-10
          

            
                
    
    

