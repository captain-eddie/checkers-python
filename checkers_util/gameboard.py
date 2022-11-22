
'''
Checkers game board module
10-15-2022
'''

import pygame
from checkers_util import piece as p

class Board:
    def __init__(self, size):
        self.board = []
        self.ROWS, self.COLS = size, size
        self.red_left = self.black_left = 0
        self.red_kings = self.black_kings = 0
        self.create_board()

    def draw_squares(self, screen):
        screen.fill((84, 75, 52))
        for row in range(self.ROWS):
            for col in range(row % 2, self.COLS, 2):
                pygame.draw.rect(screen, (219, 199, 151), (row * 50, col * 50, 50, 50))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == self.ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == (255, 0, 0):
                self.red_kings += 1
            else:
                self.black_kings += 1 

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(self.ROWS):
            self.board.append([])
            for col in range(self.COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(p.Piece(row, col, (0, 0, 0)))
                        self.black_kings += 1
                    elif row > 4:
                        self.board[row].append(p.Piece(row, col, (255, 0, 0)))
                        self.red_kings += 1
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    def draw(self, screen):
        self.draw_squares(screen)
        for row in range(self.ROWS):
            for col in range(self.COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == (255, 0, 0):
                    self.red_left -= 1
                else:
                    self.black_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return (255, 0, 0)
        elif self.black_left <= 0:
            return (0, 0, 0)
        
        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == (255, 0, 0) or piece.king:
            moves.update(self._traverse_left(row -1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row - 3, -1), -1, piece.color, right))
        if piece.color == (0, 0, 0) or piece.king:
            moves.update(self._traverse_left(row +1, min(row + 3, self.ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row + 3, self.ROWS), 1, piece.color, right))
    
        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, left - 1,skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, left + 1,skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= self.COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, self.ROWS)
                    moves.update(self._traverse_left(r + step, row, step, color, right - 1,skipped = last))
                    moves.update(self._traverse_right(r + step, row, step, color, right + 1,skipped = last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves
