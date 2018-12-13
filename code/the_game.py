"""Estrutura basica de um jogo com PyGame."""

from starfield import create_star, draw_star

import sys
import pygame
pygame.init()

# inicializacao
SIZE = WIDTH, HEIGHT = (640, 480)
FPS = 30
fullscreen = pygame.FULLSCREEN if ("-fs" in sys.argv) else 0
screen = pygame.display.set_mode(SIZE, fullscreen)
running = True

starfield = [create_star(WIDTH, HEIGHT) for _ in range(300)]

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
    # Se o jogo ainda continua...
    if running:
        # desenha objetos
        for star in starfield:
            draw_star(screen, star)
        pygame.display.flip()
        # manipula objetos

# finalizar o sistema
print("Nao desista! Volte!")
