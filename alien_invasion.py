import sys
from time import sleep
import json
import pygame


from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInsavion:
    """manage resources and game behavior class"""

    def __init__(self):
        """initialize game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # create instance for game statistics and result panel
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # create Play button
        self.play_button = Button(self, "Play")

    def run_game(self):
        """run main game loop"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()

    def start_game(self):
        """starts new game"""

        # reset game sats
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()

        # clean aliens and bullets
        self.aliens.empty()
        self.bullets.empty()

        # create new fleet and place ship in the middle
        self._create_fleet()
        self.ship.center_ship()

        # hide mouse pointer
        pygame.mouse.set_visible(False)

    def _check_events(self):
        """manage mouse and keyboard events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open(self.settings.filename, 'w') as f:
                    json.dump(self.stats.high_score, f)
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self,mouse_pos):
        """run new game if 'play' button pushed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # reset game settings
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.start_game()
        
    def _check_keydown_events(self, event):
        """respond to key down"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            with open(self.settings.filename, 'w') as f:
                json.dump(self.stats.high_score, f)
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.start_game()

    def _check_keyup_events(self, event):
        """respond to key up"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """create new bullet and add it to Group bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update bullets postition and delete old bullets"""
        # bullets position update
        self.bullets.update()
            
        # delete bullets after they gone screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_allien_collisions()

    def _check_bullet_allien_collisions(self):
        """proceed collisions"""
        # check if alien shoot
        # if yes, remove bullet and alien
        collisions = pygame.sprite.groupcollide(
                    self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # check if all aliens gone
        if not self.aliens:
            # delete all bullets and crate new aliens fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()
        
    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
          then update the positions of all aliens in the fleet.
        """ 
        self._check_fleet_edges()
        self.aliens.update()

        # check ship alien collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # check if aliens come to the screen bottom
        self._check_aliens_bottom()

    def _create_fleet(self):
        """create aliens fleet"""
        # create an alien and calculate number of aliens in line
        # space between aliens equals aline's width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """define numbers of rows with current screen size"""
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - 
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # create alien fleet
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        # create alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """respond if one of the aliens touches the end of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """proceed ship is hit by alien"""
        if self.stats.ship_left > 0:
            # reduce ships_left
            self.stats.ship_left -= 1
            self.sb.prep_ships()

            # clean aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # create new fleet and place ship in the middle
            self._create_fleet()
            self.ship.center_ship()

            # pause
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """check if aliens come to bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # the same as ship is hit
                self._ship_hit()
                break

    def _update_screen(self):
        """update screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # draw the score information.
        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # create an instance and run a game
    ai = AlienInsavion()
    ai.run_game()