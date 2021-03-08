import pygame
import math
import random
import numpy as np
from constants.colors import BLACK_COLOR
from classes.Buttons import Numeric_Button, Erase_Button
from classes.Box import Box
LINE_WIDTH_THICK = 4
LINE_WIDTH_THIN = 1

def draw_board(screen):
    ''' Created Board '''
    for i in range(20, 400, 40):
        if ((i-20)%3 == 0):
            pygame.draw.line(screen, BLACK_COLOR, (20, i), (380, i), LINE_WIDTH_THICK)
            pygame.draw.line(screen, BLACK_COLOR, (i, 20), (i, 380), LINE_WIDTH_THICK)
        else:
            pygame.draw.line(screen, BLACK_COLOR, (20, i), (380, i), LINE_WIDTH_THIN)
            pygame.draw.line(screen, BLACK_COLOR, (i, 20), (i, 380), LINE_WIDTH_THIN)

def create_sudoku_puzzle():
    board = np.zeros((9,9))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(8, -1, -1):
        num = random.randint(0, x)
        board[0][x-1] = numbers.pop(num)
    for i in range(9):
        if i in [0, 1, 2]:
            board[2][i] = board[0][i+6]
        else:
            board[2][i] = board[0][i-3]
    for i in range(9):
        if i in [6, 7, 8]:
            board[1][i] = board[0][i-6]
        else:
            board[1][i] = board[0][i+3]

    for i in range(9):
        if (i+1) % 3 != 0 :
            board[3][i] = board[0][i+1]
            board[4][i] = board[1][i+1]
            board[5][i] = board[2][i+1]
        else:
            board[3][i] = board[0][i-2]
            board[4][i] = board[1][i-2]
            board[5][i] = board[2][i-2]
    for i in range(9):
        if (i+1) % 3 != 0 :
            board[6][i] = board[3][i+1]
            board[7][i] = board[4][i+1]
            board[8][i] = board[5][i+1]
        else:
            board[6][i] = board[3][i-2]
            board[7][i] = board[4][i-2]
            board[8][i] = board[5][i-2]
    # swap column 1(i0) with 2(i1)
    col01 = []
    for i in range(9):
        col01.append(board[i][1])
        board[i][1] = board[i][0]
        board[i][0] = col01[i]

    # swap column 5(i4) with 6(i5)
    col45 = []
    for i in range(9):
        col45.append(board[i][5])
        board[i][5] = board[i][4]
        board[i][4] = col45[i]

    # swap column 7(i6) with 9(i8)
    col68 = []
    for i in range(9):
        col68.append(board[i][8])
        board[i][8] = board[i][6]
        board[i][6] = col68[i]

    # swap row 2(i1) with 3(i2)
    row23 = []
    for i in range(9):
        row23.append(board[2][i])
    board[2][:] = board[1][:]
    board[1][:] = row23

    #swap row 4(i3) with 6(i5)
    row46 = []
    for i in range(9):
        row46.append(board[5][i])
    board[5][:] = board[3][:]
    board[3][:] = row46

    #swap row 7(i6) with 8(i7)
    row78 = []
    for i in range(9):
        row78.append(board[7][i])
    board[7][:] = board[6][:]
    board[6][:] = row78

    return board

def create_initial_sudoku_board(screen, font):
    sudoku_board_solved = create_sudoku_puzzle()
    boxes = []
    player_board = np.zeros((9,9))
    for i in range(3):
        for j in range(3):
            box = sudoku_board_solved[(i*3):(i*3+3), (j*3):(j*3+3)]
            numberArray = []
            while (len(numberArray) < 3):
                number = random.randint(1, 9)
                if number not in numberArray:
                    numberArray.append(number)
                    index = np.argwhere(box == number)
                    player_board[(i*3):(i*3+3), (j*3):(j*3+3)] [index[0][0], index[0][1]] = number

    for x in range(0, 9):
        for y in range(0, 9):
            boxes.append(
                Box(
                    screen,
                    font,
                    40 * x + 20, 40 * y + 20,
                    player_board[y][x]
                )
            )
    return boxes

def draw_number_buttons(screen, font):
    number_list = []
    for i in range(1, 10, 2):
        x = 420
        y = 20 + (math.floor(i/2))*75
        number_list.append(
            Numeric_Button(screen, font, x, y, i)
        )
        # show_number2(i, x, y)

    for i in range(2, 11, 2):
        x = 500
        y = 20 + ((i/2)-1)*75

        if i < 10:
            number_list.append(
                Numeric_Button(screen, font, x, y, i)
            )
        if i == 10:
            number_list.append(
                Erase_Button(screen, x, y)
            )
    return number_list