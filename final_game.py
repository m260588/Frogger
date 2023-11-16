import pygame
import sys
from game_parameters import *
from background import draw_background, add_log
from log import logs

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Frogger')

running = True
background = screen.copy()
draw_background(background)

add_log(5)

while running == True:
    #exists the game
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    logs.update()

    logs.draw(screen)

    pygame.display.flip()










#for event in pygame.event.get():
    #if event.type == pygame.QUIT:
        #pygame.quit()
        #sys.exit()
