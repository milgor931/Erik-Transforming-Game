import pygame
import sys
from pygame.locals import QUIT
from game import Game

pygame.init()

WIDTH = 700
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
FPS = 8
game = Game(SCREEN, WIDTH, HEIGHT)

running = True
while running:


    #event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed() #returns list of certain booleans of what keys are pressed.
    if pressed_keys[pygame.K_a]: game.scroll("left")
    elif pressed_keys[pygame.K_d]: game.scroll("right")

    #drawing on the screen
    SCREEN.fill((0,0,0))
    game.PLAY_DA_GAME()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()