import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship'd current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set correct position 
        #create bullet rect attriibute, build from the pygtame,rect class and requires x and y coordinates 
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        #we set the bullet's midtop attribute to matche the ship's mid-top attribute 
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a decimal value 
        # we store a decimal value for the bullet's y-coordinates, so we can make final adjustments to the bullet's speed 
        self.y = float(self.rect.y)

        

  