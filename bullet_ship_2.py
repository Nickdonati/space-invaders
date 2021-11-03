import pygame
from pygame.sprite import Sprite


class Bullet_2(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super(Bullet_2, self).__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_ship_2_color

        # Create a bullet rect at (0, 0) and then set current position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_ship_2_width, self.settings.bullet_ship_2_height)
        self.rect.midtop = ai_game.ship_2.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_ship_2_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
