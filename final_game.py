import pygame
import sys
from game_parameters import *
from background import draw_background, add_log, add_car_begin, add_car_end #height
from log import logs
from player import frog_frames, Player
from truck import cars


#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Frogger')

#create background
running = True
background = screen.copy()
draw_background(background)

#clock object
clock = pygame.time.Clock()

#add objects
add_log(1)
add_car_begin(1)
add_car_end(1)

#initialize counter
lives = NUM_LIVES

#player's initial position
player = Player(screen_width/2,screen_height-tile_size)

font = pygame.font.Font("../Final/fonts/RoughenCornerRegular-7RjV.ttf", 48)

# main loop
while lives > 0:
    for event in pygame.event.get():
        #print(event)
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


    car_result = pygame.sprite.spritecollide(player, cars, True)

    #severson code
    log_result = pygame.sprite.spritecollide(player, logs, False)
    for collided_logs in log_result:
        rect_params = collided_logs.rect  # Access the rect parameters of the collided sprite
        print("Collision occurred with log at:", rect_params.x, rect_params.y)
        player.x = rect_params.x
        player.y = rect_params.y

    # what happens on collision
    if car_result:
        if 553 < player.rect.y < 200:
            for _ in range(len(car_result)):
                lives -= 1
                player.update_center()
                add_car_begin(1)
        else:
            for _ in range(len(car_result)):
                lives -= 1
                player.update_center()
                add_car_end(1)




    #if log_result:
        #player.collision_with_log()
        #for _ in range(len(log_result)):
            #for event in pygame.event.get():
                #if event.type == pygame.KEYDOWN:
                    #player.x = log.x
                    #player.y = log.y

    # removes and adds objects when they go off the screen
    for log in logs:
        if log.rect.x > tile_size+screen_width:
            logs.remove(log)
            #add_log(1)


    for car in cars:
        if (car.rect.x > tile_size+screen_width) and (car.y > 200):
            cars.remove(car)
            add_car_begin(1)

    for car in cars:
        if (car.rect.x > tile_size+screen_width) and (car.y < 200):
            cars.remove(car)
            add_car_end(1)


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
