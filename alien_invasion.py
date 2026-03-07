import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from  alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()


        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # create Ship
        self.ship = Ship(self)

        # create group to bullet
        self.bullets = pygame.sprite.Group()
    #     create the alien fleet
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
    #     set the background color
    #     self.bg_color =(230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


            self.clock.tick(60)

        # Watch for keyboard and mouse events.
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)


    def _create_fleet(self):
        """Create a fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.setting.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
            # new_alien = Alien(self)
            # new_alien.x = current_x
            # new_alien.rect.x = current_x
            # self.aliens.add(new_alien)
            # current_x += 2 * alien_width
            self._create_alien(current_x)
            current_x += alien_width

    def _create_alien(self, x_position):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right= False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    #          Move the ship to the right
    #         self.ship.rect.x =+ 1

    def _fire_bullet(self):
        """Create a bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet =Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        """Update position of bullets and get rid of old bullets"""
    #     update bullet positions
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            # print(len(self.bullets))


    def _update_screen(self):
        """Update image on the screen, and flip to the new screen"""
        # redraw the screen during each pass th rough the loop
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitime()
        self.aliens.draw(self.screen)
        pygame.display.flip()
                # self.clock.tick(60)
if __name__ == "__main__":
        # make a game instance, and run the game
    ai= AlienInvasion()
    ai.run_game()