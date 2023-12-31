import pygame
from game_parameters import *
import random
from truck import Truck, cars
from TruckFlip import TruckFlip, cars1


clock = pygame.time.Clock()



def draw_background(surf):
    water = pygame.image.load("../Final/sprites/water.png").convert()
    road = pygame.image.load("../Final/sprites/road.png").convert()
    grass = pygame.image.load("../Final/sprites/grass.png").convert()


    water.set_colorkey((0,0,0))
    road.set_colorkey((0, 0, 0))
    grass.set_colorkey((0,0,0))


#drawing the backgrounds dimensions

    height = water.get_height()

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(grass, (x,screen_height-height))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(road, (x,screen_height-(height*2)))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(road, (x,screen_height-(height*3)))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(grass, (x,screen_height-height*4))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(road, (x,screen_height-height*5))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(road, (x,screen_height-height*6))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(grass, (x,screen_height-height*7))




    custom_font = pygame.font.Font("../Final/fonts/RoughenCornerRegular-7RjV.ttf", 70)
    text = custom_font.render("Crossy",True,(200,0,0))
    surf.blit(text, ((screen_width/2-text.get_width()/2), screen_height-height*7))


# def functions to add a random number of objects to eventually be blitted

def add_car_1(num_car, min, max):
    road = pygame.image.load("../Final/sprites/road.png").convert()
    height = road.get_height()
    for _ in range(num_car):
        cars.add(Truck(0, (screen_height-(height*2)), random.randint(0, 5), min, max))

def add_car_2(num_car, min, max):
    road = pygame.image.load("../Final/sprites/road.png").convert()
    height = road.get_height()
    for _ in range(num_car):
        cars1.add(TruckFlip(screen_width, (screen_height-(height*3)), random.randint(0, 5), min, max))

def add_car_3(num_car, min, max):
    road = pygame.image.load("../Final/sprites/road.png").convert()
    height = road.get_height()
    for _ in range(num_car):
        cars.add(Truck(0, (screen_height-(height*5)), random.randint(0, 5), min, max))



def add_car_4(num_car, min, max):
    road = pygame.image.load("../Final/sprites/road.png").convert()
    height = road.get_height()
    for _ in range(num_car):
        cars1.add(TruckFlip(screen_width, (screen_height - (height * 6)), random.randint(0, 5), min, max))





    pygame.display.flip()