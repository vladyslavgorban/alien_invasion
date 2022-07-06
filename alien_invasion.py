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
        """rum main game loop"""
        while True:
            self._check_events()
            self._update_screen()

            # # renew screen in every loop
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()

            # # display last screen
            # pygame.display.flip()

    def _check_events(self):
        """manage mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # move ship right
                    self.ship.rect.x += 1

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    # create an instance and run a game
    ai = AlienInsavion()
    ai.run_game()