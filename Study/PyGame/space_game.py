import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Space invaders")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    controls.create_army(screen, aliens)
    stats = Stats()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, aliens, bullets)
        controls.update_bullets(screen, aliens, bullets)
        controls.update_alien_position(stats, screen, gun, aliens, bullets)


run()
