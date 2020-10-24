import pygame
from reDraw import ReDraw
from checkSolution import CheckSolution
import os

os.environ['SDL_WINDOW_VIDEO_POS'] = '400,100'

pygame.init()

WIDTH = 722
HEIGHT = 722

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize screen
surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()
FPS = 60
reDraw = ReDraw()
checkSolution = CheckSolution()
soluted = False

# drawing
posTemp = (0, 0)  # temp position point to initialize start grid
reDraw.rectCollides(posTemp)  # function that initialize start grid and where to draw nums

reDraw.drawSudokuGridWithNums(surface, soluted)  # draws sudoku grid and nums

mousePressed = False

isRun = True
while isRun:
    clock.tick(FPS)
    # event processing
    for event in pygame.event.get():
        # window closing check
        if event.type == pygame.QUIT:
            isRun = False
            # mouse press check
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rect2 = reDraw.rectCollides(event.pos)
                mousePressed = True  # check this to next step press keyboard
            if event.button == 3:  # right button
                # soluted = False             # to check again if somebody want solute again
                if checkSolution.sudokuCheckSolution(soluted, reDraw.sudokuNext):  # if soluted
                    soluted = True
                    WIDTH = 900
                    surface = pygame.display.set_mode((WIDTH, HEIGHT))
                else:
                    WIDTH = 900
                    surface = pygame.display.set_mode((WIDTH, HEIGHT))
                reDraw.drawSudokuGridWithNums(surface, soluted)  # after changing grid - redraw
        # if after mouse pressed keyboard pressed ##it blocks any other try ty check keyboard
        if mousePressed == True:
            if event.type == pygame.KEYDOWN:
                it, jt = reDraw.returningDoubleNumsOfRects(reDraw.returningNumsOfRects(rect2))
                if event.key == pygame.K_1:  # keyboard keys 1..9
                    reDraw.sudokuNext[it][jt] = 1
                elif event.key == pygame.K_2:
                    reDraw.sudokuNext[it][jt] = 2
                elif event.key == pygame.K_3:
                    reDraw.sudokuNext[it][jt] = 3
                elif event.key == pygame.K_4:
                    reDraw.sudokuNext[it][jt] = 4
                elif event.key == pygame.K_5:
                    reDraw.sudokuNext[it][jt] = 5
                elif event.key == pygame.K_6:
                    reDraw.sudokuNext[it][jt] = 6
                elif event.key == pygame.K_7:
                    reDraw.sudokuNext[it][jt] = 7
                elif event.key == pygame.K_8:
                    reDraw.sudokuNext[it][jt] = 8
                elif event.key == pygame.K_9:
                    reDraw.sudokuNext[it][jt] = 9
                reDraw.drawSudokuGridWithNums(surface, soluted)  # after changing grid - redraw
                mousePressed = False
                soluted = False

pygame.quit()