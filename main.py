
'''
Checkers non gui
Edward Abel Guobadia
10-15-2022
'''
from checkers_class_info import gameboard
import logging
import pygame
import sys

def main():
    #   set defualt logging level to DEBUG
    #   logging.basicConfig(level = logging.DEBUG)
    
    #   sets up game board
    #   my_board = gameboard.Board()
    #   print(my_board)

    while True:
        gameboard.make_board(8, 8)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                logging.debug("Quit game")
                sys.exit()


if __name__ == "__main__":
    main()
