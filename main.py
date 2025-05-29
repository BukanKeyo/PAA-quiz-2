import pygame, sys
from button import Button
import subprocess
import os
import random

pygame.init()
SCREEN = pygame.display.set_mode((928, 672))
BG = pygame.image.load("asset/main_menu.png")
    
def run_game(level_code):
    subprocess.call([sys.executable, level_code])

def exit_confirmation():
    while True:
        EXIT_CONFIRMATION_MOUSE_POS = pygame.mouse.get_pos()
        pygame.display.set_caption("Are you sure you want to exit?")
        FILL = pygame.image.load("asset/exit_confirmation.png")
        SCREEN.blit(FILL, (0, 0))
        
        EXIT_NO = Button(image=pygame.image.load("asset/no_button.png"), pos=(550, 400))
        EXIT_YES = Button(image=pygame.image.load("asset/yes_button.png"), pos=(380, 400))

        EXIT_NO.update(SCREEN)
        EXIT_YES.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXIT_NO.checkForInput(EXIT_CONFIRMATION_MOUSE_POS):
                    main_menu()
                if EXIT_YES.checkForInput(EXIT_CONFIRMATION_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def main_menu():
    while True:
        pygame.display.set_caption("Menu")
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_BUTTON = Button(image=pygame.image.load("asset/play_button.png"), pos=(465, 350))
        EXIT_BUTTON = Button(image=pygame.image.load("asset/exit_button.png"), pos=(465, 430))

        for button in [PLAY_BUTTON, EXIT_BUTTON]:
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    run_game("gameView.py")
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    exit_confirmation()

        pygame.display.update()

main_menu()
