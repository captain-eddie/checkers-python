
import pygame as pg
from checkers_util import gameboard as gb

'''
Since pygame has postieve x and y axis to be left edge going down
and top edge goinf right (of window). The pieces at the top have +1 direction downwards
and the pieces at the bottom have -1 direction upwards.
Red is on top
Black is on bottom
'''

class Piece():
    def __init__(self, rpos, cpos, color):
        self.rpos = rpos
        self.cpos = cpos
        self.color = color
        self.king = False

        #   red pieces
        if self.color == (255, 0, 0):
            self.direction = 1

        #   black pieces
        else:
            self.direction = -1

        self.x, self.y = 0, 0
        self.calc_pos()

    #   position of piece
    def calc_pos(self):
        self.x = 50 * self.cpos + 50 // 2
        self.y = 50 * self.rpos + 50 // 2
        #   self.x = 25
        #   self.y = 25

    #   make a man a king
    def make_king(self):
        self.king = True;

    #   draws piece, 18 is radius in pixels of the circle
    def draw(self, screen):
        #   draws outline
        pg.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)
        #   draws piece as a circle
        pg.draw.circle(screen, self.color, (self.x, self.y), 18)

    #   object representation
    def __repr__(self):
        return str(self.color)
