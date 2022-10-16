
'''
Checkers game board class
10-15-2022
'''

class Board:
    '''
    In standard american checkers the game is played on an 8x8 board
    Here is the board
    '''
    #   constructor
    def __init__(this):

        #   intializes game board as 2d array, -1 is defualt val for each element
        #   1 is value for black, 0 is value for red
        this.game_board = [[None] * 8 for i in range(8)]
        for row in this.game_board:
            for col in row:
                if this.game_board.index(row) % 2 == 0 and this.game_board.index(col) % 2 == 0:
                    this.game_board[row][col] = "- "
                else:
                    this.game_board[row][col] = "O "

    #   to string
    def __str__(this):
        ret = ""

        for row in this.game_board:
            ret += str(row) + "\n"

        return ret

    #   player movement
