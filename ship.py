import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ship movement class"""

    def __init__(self, ai_game):
        """initiates ship and sets start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship picture, gat rectangle
        self.image = pygame.image.load('images/ship_2.bmp')
        self.rect = self.image.get_rect()
        # each new ship appears bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # save ship coordinate as a float
        self.x = float(self.rect.x)

        # ship moving flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """draw a ship in current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update ship position using flag status"""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        #update rect attribure based on self.x
        self.rect.x = self.x

    def center_ship(self):
        """palce ship in the center of the bottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)