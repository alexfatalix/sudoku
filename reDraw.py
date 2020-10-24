import pygame
from grid import Grid

# initialize grid class
grid = Grid()
# initialize rects array
rects = []

# initialize font
pygame.init()
font = pygame.font.Font('2006.ttf', 80)


class ReDraw:
    def __init__(self):
        # start sudoku
        self.sudokuDefault = [[3, 2, 5, 8, 6, 4, 9, 1, 0],  # 1
                              [1, 9, 4, 3, 2, 7, 8, 6, 5],  # 2
                              [8, 6, 7, 5, 9, 1, 3, 4, 2],  # 3
                              [7, 0, 3, 1, 4, 9, 6, 2, 8],  # 4
                              [2, 4, 9, 6, 5, 8, 1, 7, 3],  # 5
                              [6, 8, 1, 2, 7, 0, 5, 9, 4],  # 6
                              [4, 7, 8, 9, 1, 5, 2, 3, 6],  # 7
                              [5, 1, 2, 0, 3, 6, 7, 8, 9],  # 8
                              [9, 3, 6, 7, 8, 2, 4, 5, 1]]  # 9
        self.sudokuNext = self.sudokuDefault.copy()

    # detect collidening rect with point on click and creates rects[]list
    def rectCollides(self, pos):
        for y in range(0, 720, 80):
            for x in range(0, 720, 80):
                rect = pygame.Rect((x, y, x + 80, y + 80))
                rects.append(pygame.Rect((x, y, x + 80, y + 80)))
                if rect.collidepoint(pos):
                    rectTemp = rect
        return rectTemp

    # counts num of rects from 1 to 81 and returnt it
    def returningNumsOfRects(self, rect):
        counterRects = 0
        rectTemp = (rect[0], rect[1], rect[2], rect[3])
        for y in range(0, 720, 80):
            for x in range(0, 720, 80):
                if rectTemp == (x, y, x + 80, y + 80):
                    counterRects1 = counterRects
                else:
                    pass
                counterRects += 1
        return counterRects1 + 1

    # found i,j coords of rect in double array sudokuDefault
    def returningDoubleNumsOfRects(self, fin):
        for i in range(0, 9):
            for j in range(0, 9):
                fin -= 1
                if fin == 0:
                    iTemp = i
                    jTemp = j
        return iTemp, jTemp

    # fill screen black, draw grid, draw numbers
    def drawSudokuGridWithNums(self, surface, soluted):
        surface.fill((0, 0, 0))
        grid.draw(surface)
        pygame.display.update()
        counter = 0
        for iter1 in range(0, 9):
            for iter2 in range(0, 9):
                if self.sudokuNext[iter1][iter2] != 0:
                    text = font.render(str(self.sudokuNext[iter1][iter2]), True, (255, 255, 255))
                    surface.blit(text, (rects[counter][2] - 55, rects[counter][3] - 95))
                    pygame.display.update()
                counter += 1
        if soluted:
            font1 = pygame.font.Font('2006.ttf', 100)
            textS = font1.render("S", True, (0, 0, 0))
            textU = font1.render("U", True, (0, 0, 0))
            textC1 = font1.render("C", True, (0, 0, 0))
            textC2 = font1.render("C", True, (0, 0, 0))
            textE = font1.render("E", True, (0, 0, 0))
            textS1 = font1.render("S", True, (0, 0, 0))
            textS2 = font1.render("S", True, (0, 0, 0))
            surface.blit(textS, (761, -15))
            surface.blit(textU, (761, 85))
            surface.blit(textC1, (761, 185))
            surface.blit(textC2, (761, 285))
            surface.blit(textE, (761, 385))
            surface.blit(textS1, (761, 485))
            surface.blit(textS2, (761, 585))
            pygame.display.flip()
        else:
            font1 = pygame.font.Font('2006.ttf', 100)
            textW = font1.render("W", True, (0, 0, 0))
            textR = font1.render("R", True, (0, 0, 0))
            textO = font1.render("O", True, (0, 0, 0))
            textN = font1.render("N", True, (0, 0, 0))
            textG = font1.render("G", True, (0, 0, 0))
            surface.blit(textW, (761, -15))
            surface.blit(textR, (761, 85))
            surface.blit(textO, (761, 185))
            surface.blit(textN, (761, 285))
            surface.blit(textG, (761, 385))
            pygame.display.flip()
