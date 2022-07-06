class Settings():
    """class for all settings in Alien Invasion"""

    def __init__(self):
        """initializy game settings"""
        # screen parameters
        self.screen_width = 1024
        self.screen_height = 600
        self.bg_color = (0,181,226)

        # ship settings
        self.ship_speed = 1.5