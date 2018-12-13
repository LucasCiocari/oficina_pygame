"""Estrutura basica de um jogo com PyGame."""

from starfield import create_star, move_star, draw_star
from sprite import Sprite

from random import randrange
import sys
import pygame
pygame.init()

# inicializacao
SIZE = WIDTH, HEIGHT = (640, 480)
FPS = 60
fullscreen = pygame.FULLSCREEN if ("-fs" in sys.argv) else 0
screen = pygame.display.set_mode(SIZE, fullscreen)
running = True
clock = pygame.time.Clock()

protagonista = Sprite('media/images/f18.png', (50, HEIGHT//2), speed=3)

starfield = [create_star(randrange(0, WIDTH-1), randrange(0, HEIGHT-1))
             for _ in range(300)]

# loop do jogo
while running:
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Evento de "fechar aplicacao"
            running = False
            break
        elif event.type in [pygame.KEYUP, pygame.KEYDOWN]:  # Evento de teclado
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.key == pygame.K_LEFT:
                dx, dy = protagonista.movement
                dx = -1 if event.type == pygame.KEYDOWN else 0
                protagonista.movement = (dx, dy)
            elif event.key == pygame.K_RIGHT:
                dx, dy = protagonista.movement
                dx = 1 if event.type == pygame.KEYDOWN else 0
                protagonista.movement = (dx, dy)
            if event.key == pygame.K_UP:
                dx, dy = protagonista.movement
                dy = -1 if event.type == pygame.KEYDOWN else 0
                protagonista.movement = (dx, dy)
            elif event.key == pygame.K_DOWN:
                dx, dy = protagonista.movement
                dy = 1 if event.type == pygame.KEYDOWN else 0
                protagonista.movement = (dx, dy)
    # Se o jogo ainda continua...
    if running:
        # desenha objetos
        screen.fill((0, 0, 0))  # preenche a tela com uma cor.

        for star in starfield:
            draw_star(screen, star)
        protagonista.draw(screen)

        pygame.display.flip()
        # manipula objetos
        starfield = [move_star(star)
                     if star[0] > 0
                     else create_star(WIDTH-1, randrange(0, HEIGHT-1))
                     for star in starfield]
        protagonista.update()
        # controla o tempo de atualizacao da tela.
        clock.tick(FPS)

# finalizar o sistema
print("Nao desista! Volte!")
