import pygame.font

class Scoreboard():
    """diaplay game info class"""

    def __init__(self, ai_game):
        """initialize score attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # prepare origin inmage
        self.prep_score()

    def prep_score(self):
        """transform text scrore into image"""
        rounded_score = round(self.stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, 
                    self.text_color, self.settings.bg_color)

        # display score in top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """display score on the screen"""
        self.screen.blit(self.score_image, self.score_rect)