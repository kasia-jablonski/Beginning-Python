import pygame
import random
import math
import numpy as np
from constants.colors import BACKGROUND_COLOR, HIGHLIGHT_COLOR
from classes.Box import Box
from classes.Buttons import Button
from utils.gameSetup import create_sudoku_puzzle, draw_board, draw_number_buttons, create_initial_sudoku_board

pygame.init()

screen = pygame.display.set_mode( (600, 450) )
pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 48)

screen.fill(BACKGROUND_COLOR)

# Game Setup
button_list = draw_number_buttons(screen, font2)
boxes = create_initial_sudoku_board(screen, font)

button_number_clicked =  Button(-50, -50, '') # off screen blank button

running = True
while running:
    draw_board(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            for box in boxes:
                box_clicked = box.clicked_box(screen, mouse_x, mouse_y)
                box.highlight_box(screen, font, BACKGROUND_COLOR)
                if box_clicked:
                    box.highlight_box(screen, font, HIGHLIGHT_COLOR)
                    if button_number_clicked.type == 'numeric':
                        box.on_click(screen, font, button_number_clicked.button_number)
                    elif button_number_clicked.type == 'eraser':
                        box.erase_number(screen, font)

            for button in button_list:
                button_clicked = button.clicked_button(mouse_x, mouse_y)
                if button.type == 'numeric':
                    button.draw_button(screen, font2)
                elif button.type == 'eraser':
                    button.draw_button(screen)
                if button_clicked:
                    button_number_clicked = button
                    button.select_button(screen)
            
            if button_number_clicked.selected is False:
                button_number_clicked.select_button(screen)

    pygame.display.update()