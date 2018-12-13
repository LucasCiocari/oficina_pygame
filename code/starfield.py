"""Funcoes para manipulacao do campo de estrelas."""

from random import choice, randrange


def create_star(width, height):
    """Cria uma tupla representando uma estrela."""
    x = randrange(0, width-1)
    y = randrange(0, height-1)
    speed = randrange(1, 3)
    size = randrange(1, 3)
    color = [choice([100, 200, 250])] * 3
    return (x, y, speed, size, color)


def draw_star(screen, star):
    """Desenha uma 'estrela' na tela (screen)."""
    x, y, speed, size, color = star
    rect = (x, y, size, size)
    screen.fill(color, rect)


def move_star(star):
    """Move uma estrela."""
    x, y, speed, size, color = star
    return (x - speed, y, speed, size, color)
