import pygame

class Spaceship():
    
    
    def __init__(self,screen):
        
        self.screen = screen
        self.image = pygame.image.load("image/Звездный кораблик.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    
    
    def out(self):
        
        self.screen.blit(self.image,self.rect)