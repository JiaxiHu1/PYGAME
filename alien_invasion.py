

import sys 
import pygame 
#import sys and pygame module 

from settings import Settings 
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

        #from ship.py 
        self.ship = Ship(self)

        #storing bullets in a group 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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
            self._update_screen()

            self.ship.update()
            #the group automatically calls update for each spirit in the goup 
            self._update_bullets()

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
        print(len(self.bullets))
    
    def _create_fleet(self):
        """create the fleet of aliens"""
        # make an alien 
        alien = Alien(self)
        self.aliens.add(alien)
        '''
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        available_space_x = self.settings.screen_width - alien_width
        available_space_y = self.settings.screen_height - 3 * alien_height - self.ship.rect.height
        num_aliens_x = available_space_x // (2 * alien_width)
        num_aliens_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(num_aliens_rows):
            for alien_number in range(num_aliens_x):
                self._create_alien(alien_number, row_number, alien_width, alien_height)

        '''

            

    def _check_events(self): #call a mwethod from within a class 
        """Respond to keypresses and mouse events"""

                #Watch for keyboard and mouse events. 
                # 4 this for loop is an event loop 
        for event in pygame.event.get():
                # 5 call sys.exit() to exit the game 
            if event.type == pygame.QUIT:
                #use the tools in the sys module to exit the game when the player quits
                sys.exit()
            elif event.type == pygame.KEYDOWN: 
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP: #release the right arrow key 
                self._check_keyup_events(event)


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
        
        self.aliens.daw(self.screen)
                
        #make the most recently drawn screen visible 
        # 6 tells pygame to make the most recently drawn screen visible 
        pygame.display.flip()



if __name__ =='__main__':
            #make a game instance, and run the game 
    ai = AlienInvasion()
    ai.run_game()
