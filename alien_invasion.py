import sys

import pygame

from settings import Settings
from ship import Ship

class AlienInsavion:
    """manage resources and game behavior class"""

    def __init__(self):
        """initialize game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """rum main game route"""
        while True:
            # track mouse and keyboard behaviour
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # renew screen in every loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # display last screen
            pygame.display.flip()

if __name__ == '__main__':
    # create an instance and run a game
    ai = AlienInsavion()
    ai.run_game()