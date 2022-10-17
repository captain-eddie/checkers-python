
'''
Checkers game board module
10-15-2022
'''

import pygame

#   game window constants
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
GRIDSIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_HEIGHT / GRIDSIZE, SCREEN_WIDTH / GRIDSIZE
DARK_BROWN, CREAMY_BEIGE = (84, 75, 52), (219, 199, 151)

#   draws game board with specified rows x cols dimensions
def draw_board(rows, cols, surface):
    
    #   should draw creamy biege on even positions and dark brown on odd positions
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
                if (x + y) % 2 == 0:
                    rl = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, CREAMY_BEIGE, rl)
                else:
                    rd = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, DARK_BROWN, rd)

