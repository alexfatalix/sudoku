import pygame


class CheckSolution:
    def __init__(self):
        self.listBlock = []
        self.soluted = False

    def checkLineSuccess(self, defaultSet, sudokuNext):
        counterSuccessLines = 0
        for i in range(0, 9):
            if set(sudokuNext[i]) == defaultSet:
                counterSuccessLines += 1
        return counterSuccessLines

    def checkColsSuccess(self, defaultSet, sudokuNext):
        counterSuccessColumns = 0
        x = list(map(list, zip(*sudokuNext)))
        for i in range(0, 9):
            if set(x[i]) == defaultSet:
                counterSuccessColumns += 1
        return counterSuccessColumns

    def checkBlockSuccess(self, defaultSet, sudokuNext):
        self.sudokuBlockCheck(sudokuNext)
        counterSuccessBlocks = 0
        for i in range(0, 9):
            if self.listBlock[i] == defaultSet:
                counterSuccessBlocks += 1
        return counterSuccessBlocks

    def sudokuBlockCheck(self, sudokuNext):
        isCalculating = True
        i = 0
        j = 0
        counterBlockRows = 0
        counterBlockCols = 0
        while isCalculating:
            j = counterBlockCols * 3
            i = counterBlockRows * 3
            if counterBlockRows == 3:
                isCalculating = False
                break

            listBlockNums = [sudokuNext[i][j], sudokuNext[i][j + 1], sudokuNext[i][j + 2],
                             sudokuNext[i + 1][j], sudokuNext[i + 1][j + 1], sudokuNext[i + 1][j + 2],
                             sudokuNext[i + 2][j], sudokuNext[i + 2][j + 1], sudokuNext[i + 2][j + 2]]
            self.listBlock.append(set(listBlockNums))
            counterBlockCols += 1
            if counterBlockCols == 3:
                counterBlockRows += 1
                counterBlockCols = 0

    def sudokuCheckSolution(self, soluted, sudokuNext):
        defaultSet = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        if self.checkLineSuccess(defaultSet, sudokuNext) == 9:
            if self.checkColsSuccess(defaultSet, sudokuNext) == 9:
                if self.checkBlockSuccess(defaultSet, sudokuNext) == 9:
                    soluted = True
        return soluted



