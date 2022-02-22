import pygame 

class Ship: 
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        #assign the screen to an attribute of ship, so we can access it easily in all the methods in the class 
        self.screen = ai_game.screen 
        #we access the screen's rect attribut to use the get_rect() method and assign it to self.screen_rect()
        #doing so allows us to place the ship in the correct location on the screen 
        self.screen_rect = ai_game.get_rect()

        #load the ship image and get its rect 
        # we call pygame.image.load() and give it the location of our ship image 
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen 
        #position of the ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom 

        #define the blitme() method, which draws the image to the screen at the position specified by self.rect 
        def blitme(self):
            """Draw the ship at its current location"""
            self.screen.blit(self.image,self.rect)
