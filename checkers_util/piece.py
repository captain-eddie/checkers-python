
from distutils.debug import DEBUG
import pygame as pg
import logging
from checkers_util import gameboard as gb

'''
Since pygame has postieve x and y axis to be left edge going down
and top edge goinf right (of window). The pieces at the top have +1 direction downwards
and the pieces at the bottom have -1 direction upwards.
Red is on top
Black is on bottom
'''

logging.basicConfig(level = DEBUG)
crown = pg.transform.scale(pg.image.load("images/crown.png"), (48, 98))

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

    #   make a man a king
    def make_king(self):
        self.king = True

    #   draws piece, 18 is radius in pixels of the circle
    def draw(self, screen):
        #   draws outline
        pg.draw.circle(screen, (255, 255, 255), (self.x, self.y), 18)
        #   draws piece as a circle
        pg.draw.circle(screen, self.color, (self.x, self.y), 17)

        if self.king:
            screen.blit(crown, (self.x - 24, self.y - 54))

    #   object representation
    def __repr__(self):
        return str(self.color)

    def move_piece(self, row, col):
        self.rpos = row
        self.cpos = col
        self.calc_pos()

    #   is the piece clicked by mouse
'''    def is_clicked(self):
        if pg.MOUSEBUTTONDOWN == 1:
            logging.debug("1")
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
        return pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos())
'''