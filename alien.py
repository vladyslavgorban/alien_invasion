import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to define one alien"""

    def __init__(self, ai_game):
        """initialize alien and define start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien pic and set rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # each new alien appears in left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # safe alien's exact horisontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return True if alien touch the end of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """move alien right or left"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

