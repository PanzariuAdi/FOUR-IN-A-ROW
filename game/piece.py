import pygame
from game.constants import GREY, SQUARE_SIZE

class Piece:
    PADDING = 20
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_pos()


    def calc_pos(self):
        '''
        Calculate the position in the board after the coords from the mouse.
        '''
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2


    def draw(self, win):
        '''
        Draw the piece
        '''
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)


    def __repr__(self):
        return str(self.color)


    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()


    def __eq__(self, other):
        if not isinstance(other, Piece):
            return False
        return self.color == other.color