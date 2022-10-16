
'''
Checkers game board class
10-15-2022
'''

class Board:
    def __init__(this, rows, cols):
        this.rows = rows
        this.cols = cols

        this.game_board = [[r for r in range(rows)] for c in range(cols)]
        
        for row in this.game_board:
            for col in this.game_board:
                this.game_board[row][col] = "_"

    def __str__(this):
        ret = ""

        for row in this.game_board:
            ret += str(row) + "\n"

        return ret
        #return str(this.game_board)
