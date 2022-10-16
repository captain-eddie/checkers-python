
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
    my_board = gameboard.Board()
    print(my_board)


if __name__ == "__main__":
    main()
