"""Estrutura basica de um jogo com PyGame."""

import sys
import pygame
pygame.init()

# inicializacao
SIZE = (640, 480)
FPS = 30
fullscreen = pygame.FULLSCREEN if ("-fs" in sys.argv) else 0
screen = pygame.display.set_mode(SIZE, fullscreen)
running = True

# loop do jogo
while running:
    # Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    # Se o jogo ainda continua...
    if running:
        # desenha objetos
        pygame.display.flip()
        # manipula objetos

# finalizar o sistema
print("Nao desista! Volte!")
