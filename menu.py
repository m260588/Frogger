import pygame, sys
from button import Button
from game_parameters import *
from TruckFlip import cars1
from truck import cars
from final_game import run_game

pygame.init()

SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

background = pygame.image.load("../Final/sprites/Background.png")


def get_font(size):  # Returns the font in the desired size
    return pygame.font.Font("../Final/fonts/RoughenCornerRegular-7RjV.ttf", size)

#methods to be called in the menu loop
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos() # get mouse position

        SCREEN.fill("black")


        PLAY_BACK = Button(image=None, pos=(screen_width/2, screen_height/2),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)  # changes the color based on mouse position
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def instructions():
    while True:
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        INSTRUCTIONS_TEXT = get_font(30).render("Use the arrowkeys to move", True, "Black")
        INSTRUCTIONS_TEXT_2 = get_font(30).render("The goal is to reach the other side of the road!", True, "Black")
        INSTRUCTIONS_RECT = INSTRUCTIONS_TEXT.get_rect(center=(screen_width/2, screen_height/2))
        INSTRUCTIONS_RECT_2 = INSTRUCTIONS_TEXT.get_rect(center=(screen_width / 3.25, screen_height / 1.75))
        SCREEN.blit(INSTRUCTIONS_TEXT, INSTRUCTIONS_RECT)
        SCREEN.blit(INSTRUCTIONS_TEXT_2, INSTRUCTIONS_RECT_2)

        INSTRUCTIONS_BACK = Button(image=None, pos=(screen_width/2, screen_height/1.5),
                              text_input="BACK", font=get_font(20), base_color="Black", hovering_color="Green")

        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # clicking back to go to main menu
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

#main loop/function for the whole menu
def main_menu(): #this method is the main source of creating the entire menu
    while True:
        SCREEN.blit(background, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CROSSY", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width/2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../Final/sprites/Play Rect.png"), pos=(screen_width/2, 200),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        INSTRUCTIONS_BUTTON = Button(image=pygame.image.load("../Final/sprites/Options Rect.png"), pos=(screen_width/2, 300),
                                text_input="INSTRUCTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../Final/sprites/Quit Rect.png"), pos=(screen_width/2, 400),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS) #changes the color of the button based on mouse position, edits the class
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): #when play is clicked it clears the classes of sprites
                    cars.empty()
                    cars1.empty()
                    run_game()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): # runs instrcutions when mouse clicks on the button
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
