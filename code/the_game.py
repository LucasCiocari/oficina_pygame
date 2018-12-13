"""Estrutura basica de um jogo com PyGame."""

from starfield import create_star, move_star, draw_star

from random import randrange
import sys
import pygame
pygame.init()

# inicializacao
SIZE = WIDTH, HEIGHT = (640, 480)
FPS = 30
fullscreen = pygame.FULLSCREEN if ("-fs" in sys.argv) else 0
screen = pygame.display.set_mode(SIZE, fullscreen)
running = True
clock = pygame.time.Clock()

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
    # Se o jogo ainda continua...
    if running:
        # desenha objetos
        screen.fill((0, 0, 0))  # preenche a tela com uma cor.
        for star in starfield:
            draw_star(screen, star)
        pygame.display.flip()
        # manipula objetos
        starfield = [move_star(star)
                     if star[0] > 0 else create_star(WIDTH-1,
                                                     randrange(0, HEIGHT-1))
                     for star in starfield]
        # controla o tempo de atualizacao da tela.
        clock.tick(FPS)

# finalizar o sistema
print("Nao desista! Volte!")
