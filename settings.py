class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the game's setting"""
        # Screen setting
        self.screen_width =1000
        self.screen_height =600
        self.bg_color = (200,200,200)
        # Adding Bullet settings
        self.bullet_speed= 2.5
        self.bullet_width= 3
        self.bullet_height= 15
        self.bullet_color= (60,60,60)
        self.bullets_allowed= 5
        self.ship_limit = 3

        # Ship settings
        self.ship_speed = 2.5
        # Alien settings
        self.alien_speed =2
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """Initialize the game's dynamic settings."""
        self.ship_speed= 2.5
        self.bullet_speed= 3
        self.alien_speed= 2
        # Scoring settings

        self.alien_points = 50

        # fleet_direction of 1 represents right ,  -1 represents left
        self.fleet_drop_speed= 1


    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)