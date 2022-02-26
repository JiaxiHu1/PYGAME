#control the game's appearance and the ship's speed 


class Settings: 
    """A class to store all settings from Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings 
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (230,230,230)

        #ship settings 
        self.ship_speed = 1.5 

        #bullet settings 
        self.bullet_speed = 1.5
        self.bullet_with = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3 #limiting the number of bullets 

        #Alien Settings 
        self.alien_speed = 1.0 
        self.fleet_dop_speed = 10 
        #fleet_direction of 1 represents right; -1 = left 
        self.fleet_direction = 1 

