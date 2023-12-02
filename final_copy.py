import pygame
import sys
from game_parameters import *
from background_copy import draw_background, add_car_1, add_car_2, add_car_3, add_car_4
from player import Player
from truck_copy import cars
from flip_copy import cars1



#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Crossy')

#create background
running = True
background = screen.copy()
draw_background(background)

#clock object
clock = pygame.time.Clock()

#add objects

min = MIN_SPEED
max = MAX_SPEED

add_car_1(1, min, max) # TODO fix car 1 & 3
add_car_2(1, min, max)
add_car_3(1, min, max)
add_car_4(1, min, max)



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
#while lives < 0:



    player.update()

    cars.update()

    cars1.update()

    screen.blit(background, (0, 0))

    car_result = pygame.sprite.spritecollide(player, cars, True)
    car1_result = pygame.sprite.spritecollide(player, cars1, True)

    #what happens if u win
    if player.y < 10:
        SCORE += 1
        for car in cars1:
            car.increase_speed(2)
        for car in cars:
            car.increase_speed(2)
        min += 2
        max += 2
        player.update_center()
        cars1.update()
        cars.update()

    # what happens on collision
    if car_result:
        if player.rect.y > 300:
            for _ in range(len(car_result)):
                lives -= 1
                player.update_center()
                add_car_1(1, min, max)
        else:
            for _ in range(len(car_result)):
                lives -= 1
                player.update_center()
                add_car_3(1, min, max)

    if car1_result:
        if player.rect.y > 300:
            for _ in range(len(car1_result)):
                lives -= 1
                player.update_center()
                add_car_2(1, min, max)
        else:
            for _ in range(len(car1_result)):
                lives -= 1
                player.update_center()
                add_car_4(1, min, max)

# if cars go off screen
    for car in cars:
        if (car.rect.x > tile_size+screen_width) and (car.y > 200):
            cars.remove(car)
            add_car_1(1, min, max)

    for car in cars1:
        if (car.rect.x < -tile_size*1.5) and (car.y > 200):
            cars1.remove(car)
            add_car_2(1, min, max)

    for car in cars:
        if (car.rect.x > tile_size+screen_width) and (car.y < 200):
            cars.remove(car)
            add_car_3(1, min, max)

    for car in cars1:
        if (car.rect.x < -tile_size*1.5) and (car.y < 200):
            cars1.remove(car)
            add_car_4(1, min, max)

    cars.draw(screen)

    player.draw(screen)

    cars1.draw(screen)

    text = font.render(f"Lives: {lives}", True, (225, 29, 0))
    screen.blit(text, (text.get_width()-120, screen_height-text.get_height()))

    score = font.render(f"Score: {SCORE}", True, (225, 29, 0))
    screen.blit(score, (screen_width-text.get_width()-120, screen_height-text.get_height()))

    pygame.display.flip()

    clock.tick(30)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()