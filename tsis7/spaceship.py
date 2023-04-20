import pygame

class Spaceship():
    
    
    def __init__(self,screen):
        
        self.screen = screen
        self.image = pygame.image.load("image/Звездный кораблик.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center=float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moveright = False
        self.moveleft = False
    
    
    
    def out(self):
        
        self.screen.blit(self.image,self.rect)
        
        
    def update_spaceship(self):
        if self.moveright and self.rect.right < self.screen_rect.right:
            self.center +=2
        if self.moveleft and self.rect.left > 0:
            self.center -=2
        
        self.rect.centerx = self.center
        
    def create_spaceship(self):
        self.center = self.screen_rect.centerx