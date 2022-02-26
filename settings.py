#control the game's appearance and the ship's speed 


class Settings: 
    """A class to store all settings from Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        #screen settings 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230,230,230)

        #ship settings 
        self.ship_speed = 1.5 
        self.ship_limit = 3 

        #bullet settings 
        self.bullet_speed = 1.5
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 #limiting the number of bullets 

        #Alien Settings 
        self.alien_speed = 1.0 
        self.fleet_drop_speed = 10 
        #fleet_direction of 1 represents right; -1 = left 

        #how quickly the game speed up 
        self.speedup_scale = 1.1 
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        #fleet direction of 1 = right and -1 = left 
        self.fleet_direction = 1  
        #self.alien_points = 50 
    
    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        #self.alien_points = int(self.alien_points * self.score_scale)

