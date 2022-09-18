import pygame


class Alien(pygame.sprite.Sprite):
    """class of 1 alien"""

    def __init__(self, screen):
        """initialization of first position of alien"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """draw alien on screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move of alien"""
        self.y += 0.1
        self.rect.y = self.y
