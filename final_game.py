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

#clock object
clock = pygame.time.Clock()

add_log(5)

while running:
    #exists the game
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))

    logs.update()

    for log in logs:
        if log.rect.x > tile_size+screen_width:
            logs.remove(log)
            add_log(1)




    logs.draw(screen)

    pygame.display.flip()

    clock.tick(30)










#for event in pygame.event.get():
    #if event.type == pygame.QUIT:
        #pygame.quit()
        #sys.exit()
