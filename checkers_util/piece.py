
import pygame

class Piece:
    crown = pygame.transform.scale(pygame.image.load("images/crown.png"), (48, 98))
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = 50 * self.col + 50 // 2
        self.y = 50 * self.row + 50 // 2

    def make_king(self):
        self.king = True
    
    def draw(self, screen):
        radius = 50 // 2 - self.PADDING
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        if self.king:
            screen.blit(self.crown, (self.x - self.crown.get_width()//2, self.y - self.crown.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)
