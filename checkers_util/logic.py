
import pygame
from checkers_util import gameboard as gb

class Logic:
    def __init__(self, screen, game_size):
        #self._init()
        self.screen = screen
        self.game_size = game_size
        self.selected = None
        self.board = gb.Board(self.game_size)
        self.turn = (255, 0, 0)
        self.valid_moves = {}
    
    def update(self):
        self.board.draw(self.screen)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    '''
    def _init(self):
        print("Here")
        self.selected = None
        self.board = gb.Board(self.game_size)
        self.turn = (255, 0, 0)
        self.valid_moves = {}
    '''

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, (0, 0, 255), (col * 50 + 50 // 2, row * 50 + 50 // 2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == (255, 0, 0):
            self.turn = (0, 0, 0)
        else:
            self.turn = (255, 0, 0)
