
'''
Checkers non gui
Edward Abel Guobadia
10-15-2022
'''
from checkers_class_info import gameboard
import logging

def main():
    #   set defualt logging level to DEBUG
    logging.basicConfig(level = logging.DEBUG)
    
    #   sets up game board
    rows, cols = int(input("Number of rows: ")), int(input("Number of cols: "))
    my_board = gameboard.Board(rows, cols)
    #   logging.debug(f"\n{rows}x{cols} checkers game-board is ->\n")
    print(my_board)


if __name__ == "__main__":
    main()
