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

    def update(self):
        """move alien right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x