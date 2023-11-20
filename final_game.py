import pygame
import sys
from game_parameters import *
from background import draw_background, add_log, add_car
from log import logs
from player import frog_frames, Player
from truck import cars
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

add_log(2)
add_car(2)

player = Player(screen_width/2, screen_height/2)

while running:
    #exists the game
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('You pressed the up key')
                player.move_up()
            if event.key == pygame.K_DOWN:
                print('You pressed the down key')
                player.move_down()
            if event.key == pygame.K_LEFT:
                print('You pressed the left key')
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print('You pressed the right key')
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()

    screen.blit(background,(0,0))

    logs.update()

    player.update()

    cars.update()

    for log in logs:
        if log.rect.x > tile_size+screen_width:
            logs.remove(log)
            add_log(1)

    for car in cars:
        if car.rect.x > tile_size+screen_width:
            cars.remove(car)
            add_car(1)



    logs.draw(screen)

    player.draw(screen)

    cars.draw(screen)

    pygame.display.flip()

    clock.tick(30)










#for event in pygame.event.get():
    #if event.type == pygame.QUIT:
        #pygame.quit()
        #sys.exit()
