"""Define the Sprite class."""

import pygame


class Sprite(object):
    """Define um objeto Sprite."""

    def __init__(self, image, pos):
        """Inicializa o objeto com uma imagem e a posicao inicial."""
        self.image = pygame.image.load(image)
        self.pos = pos

    def draw(self, screen):
        """Desenha o objeto na tela (screen)."""
        screen.blit(self.image, self.pos)
