class GameStats:
    """Tracking Statistics for Alien Invasion"""
    def __init__(self, ai_game):
        """initialize the game statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True


    def reset_stats(self):
        """reset the game statistics"""
        self.ships_left = self.settings.ship_limit
