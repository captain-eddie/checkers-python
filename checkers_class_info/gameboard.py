
'''
Checkers game board class
10-15-2022
'''

class Board:
    '''
    In standard american checkers the game is played on an 8x8 board
    Here is the board
    '''
    def __init__(this):

        #   intializes game board as 2d array, -1 is defualt val for each element
        #   1 is value for black, 0 is value for red
        this.game_board = [[-1] * 8 for i in range(8)]

    def __str__(this):
        ret = ""

        for row in this.game_board:
            ret += str(row) + "\n"

        return ret
