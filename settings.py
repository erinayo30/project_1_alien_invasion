class Settings:
    """A class to store all settings for Alen Invasion"""
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

        # Ship settings
        self.ship_speed = 2
        # Alien settings
        self.alien_speed =1.5
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represent right; -1 represents left
        self.fleet_direction = 1
