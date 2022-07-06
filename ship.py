import pygame

class Ship():
    """ship movement class"""

    def __init__(self, ai_game):
        """initiates ship and sets start position"""
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
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        #update rect attribure based on self.x
        self.rect.x = self.x