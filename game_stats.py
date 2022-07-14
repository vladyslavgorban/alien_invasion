class GameStats():
    """log statistics of ai game"""

    def __init__(self, ai_game):
        """initialize staisitics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # game starts in active status
        self.game_active = False

    def reset_stats(self):
        """reset statistics"""
        self.ship_left = self.settings.ship_limit