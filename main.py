
'''
Checkers non gui
Edward Abel Guobadia
10-15-2022
'''
from re import M
from checkers_util import gameboard as gb
import logging
import pygame
import sys


def get_mouse_pos(pos, board):
    x, y = pos
    row = y // board.GRIDSIZE
    col = x // board.GRIDSIZE
    return row, col

#   main function
def main():
    #   set defualt logging level to DEBUG
    logging.basicConfig(level = logging.DEBUG)

    #   board object that holds game info
    board = gb.Board(8, 8)
    
    #   initialize the game window
    pygame.init()

    #   game clock and game screen
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((board.SCREEN_WIDTH, board.SCREEN_HEIGHT))

    #   game surface
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    #   draw the grid
    logging.debug(f"\nGame Board\n{board.boardlist}")

    #   tpiece = board.get_piece(6, 1)
    #   board.move(tpiece, 4, 3)

    #   main game loop
    while True:
        clock.tick(25)
        board.draw_board(surface)

        #   update screen when ever there is an event
        screen.blit(surface, (0, 0))
        pygame.display.update()

        #   event handler
        for event in pygame.event.get():

            #   handles quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                logging.debug("Quit game")
                sys.exit()

            #   picking piece up with mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos, board)
                piece = board.get_piece(row, col)

                #   droping piece
                if event.type == pygame.MOUSEBUTTONDOWN:
                    next_pos = pygame.mouse.get_pos()
                    next_row, next_col = get_mouse_pos(next_pos, board)
                    next_piece = board.get_piece(next_row, next_col)
                    #   just move piece to next pos and move piece at next pos to original pos
                    if board.boardlist[next_row][next_col].color == (1, 1, 1):
                        board.boardlist[row][col] = piece
                        break
                    #   piece = board.get_piece(row, col)
                    board.move(piece, next_row, next_col)


#   call main
if __name__ == "__main__":
    main()
