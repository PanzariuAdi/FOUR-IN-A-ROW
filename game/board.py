import pygame

from game.constants import BLACK, GREY, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from game.piece import Piece

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        
    def draw_squares(self, win):
         win.fill(BLACK)
         for row in range(ROWS):
             for col in range (row % 2, ROWS, 2):
                 pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def add_piece(self, win, row, col, color):
        self.draw_squares(win)
        self.board[row][col] = Piece(row, col, color)
        piece = self.board[row][col]