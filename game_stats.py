import json

class GameStats():
    """log statistics of ai game"""

    def __init__(self, ai_game):
        """initialize staisitics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # game starts in active status
        self.game_active = False

        # game record should not reset
        with open(self.settings.filename) as f:
           self.high_score = json.load(f)

    def reset_stats(self):
        """reset statistics"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1