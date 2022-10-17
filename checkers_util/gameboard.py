
'''
Checkers game board module
10-15-2022
'''

import pygame as pg

class Board():
    #   constructor
    def __init__(self, rows, cols):
        #   game window constants
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = cols * 50, rows * 50
        self.GRIDSIZE = 50
        self.GRID_WIDTH = self.SCREEN_HEIGHT / self.GRIDSIZE
        self.GRID_HEIGHT = self.SCREEN_WIDTH / self.GRIDSIZE
        self.DARK_BROWN, self.CREAMY_BEIGE = (84, 75, 52), (219, 199, 151)

        #   list representaion of game window
        #   1 represents red pieces
        #   0 represents black pieces
        #   -1 represents empty pieces
        self.boardlist = [[0] * cols for r in range(0, rows)]
        for indexr, row in enumerate(self.boardlist):
            for indexc, col in enumerate(row):
                if indexc < 2:
                    self.boardlist[indexr][indexc] = 1
                elif indexc in range(len(self.boardlist[indexr]) - 2, len(self.boardlist)):
                    self.boardlist[indexr][indexc] = 0
                else:
                    self.boardlist[indexr][indexc] = -1
                

    #   draws game board with specified rows x cols dimensions
    def draw_board(self, surface):
        #   should draw creamy biege on even positions and dark brown on odd positions
        for y in range(0, int(self.GRID_HEIGHT)):
            for x in range(0, int(self.GRID_WIDTH)):
                    if (x + y) % 2 == 0:
                        rl = pg.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
                        pg.draw.rect(surface, self.CREAMY_BEIGE, rl)
                    else:
                        rd = pg.Rect((x * self.GRIDSIZE, y * self.GRIDSIZE), (self.GRIDSIZE, self.GRIDSIZE))
                        pg.draw.rect(surface, self.DARK_BROWN, rd)
