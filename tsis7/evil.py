import pygame


class Evil(pygame.sprite.Sprite):
    
    def __init__(self, screen):
        super(Evil,self).__init__()
        self.screen = screen
        self.image = pygame.image.load("image/evil.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def draw(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.y += 0.1
        self.rect.y = self.y
        