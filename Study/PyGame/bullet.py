import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """new bullet in gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 30, 230, 86
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
