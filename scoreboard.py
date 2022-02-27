import pygame.font
from pygame.sprite import Group
from ship import Ship


class ScoreBoard:
    """A class to report scoring information"""

    def __init__(self, ai_game):
        """initialize scorekeeping attributes """
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # font settings for scoring information 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 24)

        # prepare the initial score image 
        self.prep_score()
        self.prep_high_score() #the high score will be displayed separately from the score, so we need a new method 
        self.prep_level()

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = round(self.stats.score, -1)  # tell python to round the value of stats.score to the nearest 10
        score_str = "current score: " + "{:,}".format(rounded_score) #insert commas into numbers when converting a numerical value to a string 
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
  
    
    def show_score(self):
        """draw score and level to the screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)


    def prep_high_score(self):
        """turn the high score into a rendered image"""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "highest score: " + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # center the high score at the top of the screen 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """check to see if there's a new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = "level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        