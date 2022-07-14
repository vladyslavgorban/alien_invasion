import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Class for bullets ship shoots"""

    def __init__(self, ai_game):
        """create instance of bullet on current ship position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet in postion (0,0) and appoint correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # save bullet position in float
        self.y = float(self.rect.y)

    def update(self):
        """move bullet up on screen"""
        # update bullet's position in float
        self.y -= self.settings.bullet_speed
        # update rectangle's position
        self.rect.y = self.y

    def draw_bullet(self):
        """display the bulet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)