
'''
Checkers game board module
10-15-2022
'''

import pygame

screen = pygame.display.set_mode(size = (500, 500))
dark_brown = (84, 75, 52)
creamy_beige = (219, 199, 151)

#   makes game board with specified rows x cols dimensions
def make_board(rows, cols):
    board_array = [[] *cols for r in range(0, rows)]

    #   loop over the array, if the index is odd, draw and color the block dark brown
    #   else, draw and color the block creamy beige
    for r in board_array:
        for c in r:

            #   color creamy beige
            #   if board_array.index(board_array[r][c]) % 2 == 0:
            pygame.draw.rect(screen, creamy_beige, pygame.Rect(30, 30, 60, 60))
            pygame.display.flip()

            #   color dark brown
            #   else:
            pygame.draw.rect(screen, dark_brown, pygame.Rect(30, 30, 60, 60))
            pygame.display.flip()

#   sets starting position of pieces on board
def set_board(board):
    #   board = set_board(board) or is there a faster more memory efficent way
    pass
