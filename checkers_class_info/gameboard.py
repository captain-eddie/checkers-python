
'''
Checkers game board class
10-15-2022
'''

class Board:
    def __init__(this, rows, cols):
        this.rows = rows
        this.cols = cols
        # intializes game board as 2d array
        this.game_board = [[c for c in range(cols)] for r in range(rows)]

    def __str__(this):
        ret = ""

        for row in this.game_board:
            ret += str(row) + "\n"

        return ret
        #return str(this.game_board)
