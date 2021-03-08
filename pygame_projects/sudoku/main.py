''' Game Configuration '''
import pygame
import random
import math
import time
import numpy as np

pygame.init()
LINE_COLOR = (0, 0, 0)
LINE_WIDTH_THICK = 4
LINE_WIDTH_THIN = 2
BG_COLOR = (211, 201, 206)
FILL_COLOR = (183, 166, 173)
HIGHLIGHT_COLOR = (213, 196, 161)


screen = pygame.display.set_mode( (600, 450) )

pygame.display.set_caption("Sudoku")
icon = pygame.image.load('sudoku.png')
pygame.display.set_icon(icon)

screen.fill((211, 201, 206))



def draw_board():
    ''' Created Board '''
    for i in range(20, 400, 40):
        if ((i-20)%3 == 0):
            pygame.draw.line(screen, LINE_COLOR, (20, i), (380, i), LINE_WIDTH_THICK)
            pygame.draw.line(screen, LINE_COLOR, (i, 20), (i, 380), LINE_WIDTH_THICK)
        else:
            pygame.draw.line(screen, LINE_COLOR, (20, i), (380, i), LINE_WIDTH_THIN)
            pygame.draw.line(screen, LINE_COLOR, (i, 20), (i, 380), LINE_WIDTH_THIN)

def draw_sudoku():
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
    print(board)
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
    print(row23)
    board[2][:] = board[1][:]
    print(row23)
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

def check_if_correct(c):
    count = 0
    for i in range(1, 10):
        if i in c:
            count += 1
    if count == 9:
        return True
    else: 
        return False
        
# f = [1, 2, 3,4, 5, 6, 7, 8, 8]
# g = [2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(check_if_correct(f))
# print(check_if_correct(g))

def check_sudoku(sudoku):
    # check rows
    for i in range(9):
        row = []
        column = []
        count = 0
        for j in range(9):
            row.append(sudoku[i][j])
            column.append(sudoku_board[j][i])
        for k in range(1, 10):
            if k in row:
                count += 1
        if count == 9:
            print("row " + str(i) + " correct")
        else:
            print("row " + str(i) + "incorrect")
            


draw_board()
sudoku_board = draw_sudoku()
# print(sudoku_board)
# check_sudoku(sudoku_board)

player_board = np.zeros((9,9))
for i in range(3):
    for j in range(3):
        box = sudoku_board[(i*3):(i*3+3), (j*3):(j*3+3)]
        numberArray = []
        while (len(numberArray) < 3):
            number = random.randint(1, 9)
            if number not in numberArray:
                numberArray.append(number)
                index = np.argwhere(box == number)
                player_board[(i*3):(i*3+3), (j*3):(j*3+3)] [index[0][0], index[0][1]] = number
        
    print(player_board)

font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 48)

def show_number(value, x, y):
    number = font.render(str(value), True, (0, 0, 0))
    screen.blit(number, (x*40+30, y*40+30))

def show_number2(value, x, y):
    number = font2.render(str(value), True, (0, 0, 0))
    screen.blit(number, (x+13, y+7))

def color_rect(x, y, color):
    ry = y*40 + 22
    rx = x*40 + 22
    pygame.draw.rect(screen, color, pygame.Rect(rx, ry, 38, 38))

def format_time(time):
    minutes = math.floor(time/60)
    seconds = time - minutes*60
    if seconds < 9:
        return str(minutes) + ":0" + str(seconds)
    else:
        return str(minutes) + ":" + str(seconds)

for i in range(9):
    for j in range(9):
        if player_board[i][j] != 0:
            color_rect(j, i, FILL_COLOR)
            show_number(int(player_board[i][j]), j, i)

# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(420, 20, 55, 55))
# show_number2(1, 420, 20)
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(500, 20, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(420, 95, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(500, 95, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(420, 170, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(500, 170, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(420, 245, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(500, 245, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(420, 320, 55, 55))
# pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(500, 320, 55, 55))

for i in range(1, 10, 2):
    x = 420
    y = 20 + (math.floor(i/2))*75
    pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(x, y, 55, 55))
    show_number2(i, x, y)

for i in range(2, 11, 2):
    
    x = 500
    y = 20 + ((i/2)-1)*75
    pygame.draw.rect(screen, (183, 166, 173), pygame.Rect(x, y, 55, 55))
    if i < 10:
        show_number2(i, x, y)

eraser = pygame.image.load('eraser.png')
screen.blit(eraser, (495, 315))
    




# show_number(1, 30, 30)
# show_number(2, 70, 30)
# show_number(3, 110, 30)
# show_number(4, 150, 30)

running = True

    
    

startTime = time.time()

while running:
    draw_board()
    pygame.draw.rect(screen, BG_COLOR, pygame.Rect(200, 400, 100, 100))
    label = font.render(str(format_time(int(time.time() - startTime))), True, (0, 0, 0))
    screen.blit(label, (200, 400))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            print(mouseX, mouseY)
            if (mouseX > 20 and mouseX < 380) and (mouseY > 20 and mouseY < 380):
                try:
                    color_rect(clicked_col, clicked_row, BG_COLOR)
                except NameError:
                    clicked_col = None
                clicked_col = math.floor((mouseX-20)/40)
                clicked_row = math.floor((mouseY-20)/40)
                if player_board[clicked_col][clicked_row] == 0:
                    color_rect(clicked_col, clicked_row, HIGHLIGHT_COLOR)
            try:
                if (mouseX > 420 and mouseX < 475) and (mouseY > 20 and mouseY < 75):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(1, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 1

                if (mouseX > 500 and mouseX < 555) and (mouseY > 20 and mouseY < 75):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(2, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 2
                        

                if (mouseX > 420 and mouseX < 475) and (mouseY > 95 and mouseY < 150):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(3, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 3

                if (mouseX > 500 and mouseX < 555) and (mouseY > 95 and mouseY < 150):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(4, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 4

                if (mouseX > 420 and mouseX < 475) and (mouseY > 170 and mouseY < 225):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(5, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 5

                if (mouseX > 500 and mouseX < 555) and (mouseY > 170 and mouseY < 225):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(6, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 6

                if (mouseX > 420 and mouseX < 475) and (mouseY > 245 and mouseY < 300):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(7, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 7

                if (mouseX > 500 and mouseX < 555) and (mouseY > 245 and mouseY < 300):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(8, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 8

                if (mouseX > 420 and mouseX < 475) and (mouseY > 320 and mouseY < 375):
                    if (player_board[clicked_col][clicked_row]) == 0:
                        show_number(9, clicked_col, clicked_row)
                        player_board[clicked_col][clicked_row] = 9

                if (mouseX > 500 and mouseX < 555) and (mouseY > 320 and mouseY < 375):
                    if (player_board[clicked_col][clicked_row]) != 0:
                        color_rect(clicked_col, clicked_row, BG_COLOR)
                        player_board[clicked_col][clicked_row] = 0
            except NameError:
                clicked_col = None

            
                #print(clicked_row, clicked_col)
                
    pygame.display.update()

