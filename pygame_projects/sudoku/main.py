''' Game Configuration '''
import pygame
import random
import math
import numpy as np

pygame.init()
LINE_COLOR = (0, 0, 0)
LINE_WIDTH_THICK = 4
LINE_WIDTH_THIN = 2


screen = pygame.display.set_mode( (600, 600) )

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
        
f = [1, 2, 3,4, 5, 6, 7, 8, 8]
g = [2, 3, 4, 5, 6, 7, 8, 9, 1]
print(check_if_correct(f))
print(check_if_correct(g))

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
print(sudoku_board)
check_sudoku(sudoku_board)
running = True

while running:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            print(mouseX, mouseY)
            if (mouseX > 20 and mouseX < 380) and (mouseY > 20 and mouseY < 380):
                clicked_col = math.floor((mouseX-20)/40)
                clicked_row = math.floor((mouseY-20)/40)

                print(clicked_row, clicked_col)
                
    pygame.display.update()