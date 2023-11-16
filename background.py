import pygame
from game_parameters import *
from log import logs, Log
import random
from player import frog_frames




def draw_background(surf):
    water = pygame.image.load("../Final/sprites/water.png").convert()
    road = pygame.image.load("../Final/sprites/road.png").convert()
    grass = pygame.image.load("../Final/sprites/grass.png").convert()
    lillypad = pygame.image.load("../Final/sprites/lillypad.png").convert()

    water.set_colorkey((0,0,0))
    road.set_colorkey((0, 0, 0))
    grass.set_colorkey((0,0,0))
    lillypad.set_colorkey((0, 0, 0))

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
            surf.blit(water, (x,screen_height-(height*3)))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(grass, (x,screen_height-height*4))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(water, (x,screen_height-height*5))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(road, (x,screen_height-height*6))

    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            surf.blit(grass, (x,screen_height-height*7))

    for x in range(len(frog_frames)):
        surf.blit(frog_frames[x], (x * 75, 0))

    custom_font = pygame.font.Font("../Final/fonts/RoughenCornerRegular-7RjV.ttf", 70)
    text = custom_font.render("Frogger",True,(200,0,0))
    surf.blit(text, ((screen_width/2-text.get_width()/2), screen_height-height*7))
# def functions to add a random number of objects to eventually be blitted
def add_log(num_log):
    for _ in range(num_log):
        logs.add(Log(0, random.randint(0, screen_height), random.randint(1,3)))




#def add_lilly(num_lilly):
    #for _ in range(num_lilly):
        #logs.add(Log(random.randint(screen_width, screen_height * 2), random.randint(0, screen_height - tile_size)))

#def add_truck(num_truck):
    #for _ in range(num_truck):
        #logs.add(Log(random.randint(screen_width, screen_height * 2), random.randint(0, screen_height - tile_size)))

    pygame.display.flip()



