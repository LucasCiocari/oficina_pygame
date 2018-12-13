"""Define the Sprite class."""

import pygame


class Sprite(object):
    """Define a game sprite."""

    def __init__(self, image, pos, **kwargs):
        """Initialize a sprite object."""
        self.pos = pos
        self.image = pygame.image.load(image)
        self.speed = kwargs.get('speed', 1)
        self.movement = (0, 0)

    def draw(self, screen, **kwargs):
        """Draw the sprite to the screen."""
        screen.blit(self.image, self.pos)

    def update(self):
        """Update sprite position."""
        x, y = self.pos
        dx, dy = self.movement
        speed = self.speed
        self.pos = (x + dx*speed, y + dy*speed)

    def limits(self, window):
        """Ensure sprite in within limits."""
        w, h = window
        a, b = self.image.get_size()
        x, y = self.pos
        x = 0 if x < 0 else w-a if x > w-a else x
        y = 0 if y < 0 else h-b if y > h-b else y
        self.pos = (x, y)
