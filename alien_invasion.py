import sys 
import pygame 
#import sys and pygame module 

from settings import Settings 
from ship import Ship #update - create a ship and calls the ship's blitme() method 

class AlientInvation:
    """Overall clas to manage game assets and behavior.""" 

    def __init__(self):
        """initialize the game, and create game resources."""
        # 1 pygame.init() function is to initialize the background settings
        pygame.init()
        #import from Settings.py 
        self.settings = Settings()


        # 2 dimension of the game window 1200 pixels wide by 800 pixels high
        #after import the settings, we do not need to hard code the numbers 
        self.screen = pygame.display.set_model((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #from ship.py 
        self.ship = Ship(self)

        #setting the background color 
        #(255,0,0) is red (0,255,0) is green and (0,0,255) is blue 
        #and black is the mix of the three colors 
        #after import the settings, we do not need to hard code the colors anymore 
        self.bg_color(self.settings.bg_color)


        def run_game(self):
            """Start the main loop for the game."""
            # 3  runs continually 
            while True: 
                #make a new _check_events() methods and move the lines that check wheather the player has clicked to close the window into this new method 
                self._check_events()
                self._update_screen()

                #redraw the screen during each pass through the loop 

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
                        if event.key == pygame.K_RIGHT: #right arrow key - then move the ship to the right  
                            #Move the ship to the right 
                            self.ship.rect.x += 1 



        def _update_screen(self):
            """Update images on the screen, and dlip to the new screen"""      
                #redraw the screen during each pass through the loop 
                #fill the screen with the background color using the fill() method 
                self.screen.fill(self.bg_color)

                #by calling this function, the ship appears on the top of the background 
                self.ship.blitme()
                
                #make the most recently drawn screen visible 
                # 6 tells pygame to make the most recently drawn screen visible 
                pygame.display.flip()

        if __name__ =='__main__':
            #make a game instance, and run the game 
            ai = AlienInvasion()
            ai.run_game()
