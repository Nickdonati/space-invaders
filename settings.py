import pygame
from pygame import mixer
class Settings:
    """A class to store all settings for Alien Invaders."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.image = pygame.image.load('images/background.bmp')
        self.alien_health = 1

        #background music
        mixer.music.load('sound/back_sound.wav')
        mixer.music.play(-1)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings  
        self.bullet_speed = 10.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 999

        # Bullet 2 settings  
        self.bullet_ship_2_speed = 12.5
        self.bullet_ship_2_width = 5
        self.bullet_ship_2_height = 16
        self.bullet_ship_2_color = (246, 0, 0)
        self.bullets_ship_2_allowed = 999


        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly game speeds up
        self.speedup_scale = 2

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game. """
        self.ship_speed = 1.5
        self.ship_2_speed = 1.5
        self.bullet_speed = 5.0
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self, ai_game):
        """ Increase speed settings and alien point values """
        self.ship_speed *= self.speedup_scale
        self.ship_2_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_health += 1
        for alien in ai_game.aliens:
            alien.hitpoints = self.alien_health

        self.alien_points = int(self.alien_points * self.score_scale)
