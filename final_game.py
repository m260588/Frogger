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

add_log(1)
add_car(1)

lives = NUM_LIVES

player = Player(screen_width/2, screen_height/2)

font = pygame.font.Font("../Final/fonts/RoughenCornerRegular-7RjV.ttf", 48)

while lives > 0:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
            player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
        if event.type == pygame.KEYUP:
            player.stop()


    screen.blit(background,(0,0))

    logs.update()

    player.update()

    cars.update()

    #log_result = pygame.sprite.spritecollide(player, logs, False)

    car_result = pygame.sprite.spritecollide(player, cars, True)

    if car_result:
        for _ in range(len(car_result)):
            lives -= 1
            player.rect.x = 0
            player.rect.y = 0
            player.update_center()
            add_car(1)

    #if log_result:
        #player.rect = log.rect

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

    text = font.render(f"Lives: {lives}", True, (225, 29, 0))
    screen.blit(text, (text.get_width()-120, screen_height-text.get_height()))

    pygame.display.flip()

    clock.tick(30)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
