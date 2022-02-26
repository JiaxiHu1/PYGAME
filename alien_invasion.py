

import sys 
from time import sleep 
import pygame 
#import sys and pygame module 

from settings import Settings 
from game_stats import GameStats
from button import Button 
from ship import Ship #update - create a ship and calls the ship's blitme() method 
from bullet import Bullet #Firing bullets - import bullet 
from alien import Alien 


class AlienInvasion:
    """Overall clas to manage game assets and behavior.""" 

    def __init__(self):
        """initialize the game, and create game resources."""
        # 1 pygame.init() function is to initialize the background settings
        pygame.init()
        #import from Settings.py 
        self.settings = Settings()

        #running the game in fullscreen mode 
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height


        # 2 dimension of the game window 1200 pixels wide by 800 pixels high
        #after import the settings, we do not need to hard code the numbers 
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #create an instance to store game statistics 
        self.stats = GameStats(self)

        #from ship.py 
        self.ship = Ship(self)

        #storing bullets in a group 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #make the play button 
        self.play_button=Button(self,"Play")

        #setting the background color 
        #(255,0,0) is red (0,255,0) is green and (0,0,255) is blue 
        #and black is the mix of the three colors 
        #after import the settings, we do not need to hard code the colors anymore 
        self.screen.fill(self.settings.bg_color)


    def run_game(self):
        """Start the main loop for the game."""
            # 3  runs continually 
        while True: 
                #make a new _check_events() methods and move the lines that check wheather the player has clicked to close the window into this new method 
            self._check_events()
            #redraw the screen during each pass through the loop 
            if self.stats.game_active:
                self.ship.update()
            #the group automatically calls update for each spirit in the goup 
                self._update_bullets()

                self._update_aliens()

            self._update_screen()
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""

        if self.stats.ships_left > 0:
            # decrement ships_left
            self.stats.ships_left -= 1
            # 更新记分牌
            self.scoreboard.prep_ships()

            # get rid of any remaining aliens and bullets 
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # pause 
            sleep(0.5)
        else: 
            self.stats.game_active = False 

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        """Check if the fleet is at an edge, then update the positions of all aliens in the fleet"""
        self.aliens.update()
        self._check_fleet_edges()
        #detecting alien and ship collisions 
        #look for alien-ship collisions 
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            #print("Ship hit!!!")
            self._ship_hit()
        
        #look for aliens hitting the bottom of the screen 
        self._check_aliens_bottom()
    
    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of the screen """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                #treat this the same as if the ship got hit 
                self._ship_hit()  
                break 
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


        #get rid of bullets that have disappeared 
        #disappear off the top of the screen 
    #create the update_bullets method 
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        # update bullet positions 
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions"""
        #remove any bullets and aliens that have collided 

        #check for any bullets that have hit aliens 
        #if so, get rid of the bullet and the alien 
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if not self.aliens:
            #destroy existing bullets and create new fleet 
            #repopulating the fleet
            self.bullets.empty()
            self._create_fleet()
    
    #refactoring _create_fleet()
    def _create_fleet(self):
        """create the fleet of aliens"""
        # make an alien 
        #create an alien and find the number of aliens in a row 
        # spacing between each alien is equal to one alien width 
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size 
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2 * alien_width) 
    
        #determine the number of rows of aliens that fit on the screen 
        ship_height = self.ship.rect.height 
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #create the full fleet of aliens 
        # create the first row of aliens 
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x): 
                self._create_alien(alien_number,row_number)
        
    def _create_alien(self,row_number,alien_number):
            #create an alien and palce it in the row 
            alien = Alien(self)
            alien_width,alien_height = alien.rect.size 
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x 
            alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
            self.aliens.add(alien)
            


            

    def _check_events(self): #call a mwethod from within a class 
        """Respond to keypresses and mouse events"""

                #Watch for keyboard and mouse events. 
                # 4 this for loop is an event loop 
        for event in pygame.event.get():
                # 5 call sys.exit() to exit the game 
            if event.type == pygame.QUIT:
                #use the tools in the sys module to exit the game when the player quits
                sys.exit()
            elif event.type == pygame.mouse.get_pos():
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN: 
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: #release the right arrow key 
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """start a new game when the player clicks play"""
        
        if self.play_button.rect.collidepoint(mouse_pos):
            #reset the game statistics 
            self.stats.reset_stats()
            self.stats.game.active = True 

            #get rid of any remaining aliens and bullets 
            self.aliens.empty()
            self.bullets.empty()

            #create a new fleet and center the ship 
            self._create_fleet()
            self.ship.center_ship()

            

    def _check_keydown_events(self, event): #when you press the key 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        #press Q to quit 
        elif event.key == pygame.K_q:
            sys.exit()
        #press space key to fire bullet 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event): #when you release the key 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullet_allowed: #when less than three, we create a new bullet 
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet) 

    def _update_screen(self):
        """Update images on the screen, and dlip to the new screen"""      
        #redraw the screen during each pass through the loop 
        #fill the screen with the background color using the fill() method 
        self.screen.fill(self.settings.bg_color)

        #by calling this function, the ship appears on the top of the background 
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet() #to draw all fired bullets to the screen 
        
        self.aliens.draw(self.screen)

        #Draw the play button if the game is inactive 
        if not self.stats.game_active:
            self.play_button.draw_button()
                
        #make the most recently drawn screen visible 
        # 6 tells pygame to make the most recently drawn screen visible 
        pygame.display.flip()



if __name__ =='__main__':
            #make a game instance, and run the game 
    ai = AlienInvasion()
    ai.run_game()
