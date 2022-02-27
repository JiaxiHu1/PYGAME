#update method to manage the ship's position and blitme method to draw the ship to the screen 


import pygame 
from pygame.sprite import Sprite 

class Ship: 
    """A class to manage the ship."""

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position"""
        super().__init__() #displaying the number of ships 
        #assign the screen to an attribute of ship, so we can access it easily in all the methods in the class 
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 

        #we access the screen's rect attribut to use the get_rect() method and assign it to self.screen_rect()
        #doing so allows us to place the ship in the correct location on the screen 
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect 
        # we call pygame.image.load() and give it the location of our ship image 
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen 
        #position of the ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom 

        #store a decimal value of the ship's horizon position 
        self.x = float(self.rect.x)

        #movement flag 
        #initially set it to false 
        self.moving_right = False 
        self.moving_left = False 

    
    def update(self):
        """Update the ship's position based on the movement flag."""
        """Update the ship's x value, not the rect."""
        #also limit the ship's range 
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed 
        
        if self.moving_left and self.rect.left > 0: 
            self.x -=  self.settings.ship_speed 
        
        #update rect object from self.x 
        self.rect.x = self.x 





        #define the blitme() method, which draws the image to the screen at the position specified by self.rect 
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        """center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
