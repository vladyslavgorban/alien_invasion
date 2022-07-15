class Settings:
    """class for all settings in Alien Invasion"""

    def __init__(self):
        """initialize game settings"""
        # screen parameters
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (0,181,226)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # aliens settings
        self.fleet_drop_speed = 50
       

        # game speed up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings changing during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_directions = 1 means moving right, -1 means moving left
        self.fleet_direction = 1

        #counting score
        self.alien_points = 50

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale