import pygame
from game_parameters import *
from player import frog_frames

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frog Moving")

clock = pygame.time.Clock()

RGB = (10,150,150)
color =(247,247,247)


while True:

    screen.fill(RGB)

    for x in range(len(frog_frames)):
        screen.fill(RGB)
        screen.blit(frog_frames[x], (75, 0))
        pygame.display.flip()
        clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
pygame.quit()