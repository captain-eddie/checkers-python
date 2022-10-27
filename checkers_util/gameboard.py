
'''
Checkers game board module
10-15-2022
'''

import pygame as pg
from checkers_util import piece
import logging as lg

lg.basicConfig(level = lg.DEBUG)

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

        #   empty 2D list
        col_list = [] * cols
        self.boardlist = [col_list for r in range(0, rows)]

        #   dead code
        #   self.boardlist = [[] * cols for r in range(0, rows)]

        #   puts pieces in appropiate position in boardlist
        for row in self.boardlist:
            row_index = self.boardlist.index(row)
            for col in row:
                col_index = row.index(col)

                #   grid position
                grid_pos = (row_index + col_index) % 2

                #   puts red man in proper locations
                if col_index < 3 and grid_pos != 0:
                    red_man = piece.Piece(col_index, row_index, (255, 0, 0))
                    self.boardlist[col_index][row_index] = red_man
                
                #   puts black man in proper locations
                elif col_index in range(len(self.boardlist[col_index]) - 3, len(self.boardlist)) and grid_pos != 0:
                    black_man = piece.Piece(col_index, row_index, (0, 0, 0))
                    self.boardlist[col_index][row_index]

                else:
                    pass

        #   for indexr, row in enumerate(self.boardlist):
            #   for indexc, col in enumerate(row):
                #   gridpos = (indexc + indexr) % 2
                #   if indexc < 3 and gridpos != 0:
                    #   man = piece.Piece(indexc, indexr, (255, 0, 0))
                    #   self.boardlist[indexc][indexr] = man
                #   elif indexc in range(len(self.boardlist[indexc]) - 3, len(self.boardlist)) and gridpos != 0:
                    #   man = piece.Piece(indexc, indexr, (0, 0, 0))
                    #   self.boardlist[indexc][indexr] = man
                #   else:
                    #   pass
                    #   man = piece.Piece(indexc, indexr, (1, 1, 1))
                    #   self.boardlist[indexc][indexr] = -1
                    #   self.boardlist[indexc][indexr] = man
                

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

        # draws pieces
        for indexr, row in enumerate(self.boardlist):
            for indexc, col in enumerate(row):
                if self.boardlist[indexr][indexc] != -1:
                    #   lo.debug(f"\n(indexr, indexc) -> ({indexr}, {indexc}) = {self.boardlist[indexr][indexc]}")
                    #   lo.debug(f"Type of element -> {type(self.boardlist[indexr][indexc])}")
                    #   man = piece.Piece(indexr, indexc, self.boardlist[indexr][indexc])
                    #   man.draw(surface)
                    #   self.boardlist[indexr][indexc].draw(surface)
                    man = self.boardlist[indexr][indexc]
                    man.draw(surface)

    
    def move(self, piece, row, col):
        #   if self.boardlist[row][col] == -1:
            #   return
            #   self.move_empty()

        self.boardlist[piece.rpos][piece.cpos], self.boardlist[row][col] = self.boardlist[row][col], self.boardlist[piece.rpos][piece.cpos]
        piece.move_piece(row, col)

        #   check to see if you moved to back rank for kinging
        if row == len(self.boardlist) - 1 or row == 0:
            piece.make_king()

    def get_piece(self, row, col):
        return self.boardlist[row][col]

'''    
def move_empty(self, etype):
        #   droping piece
        if etype == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            row, col = piece.get_mouse_pos(pos, self.boardlist)
            piece = self.boardlist.get_piece(row, col)
            self.boardlist.move(piece, row, col)

'''
    
