import pygame
from copy import deepcopy
from game.constants import BLACK, GREY, ROWS, COLS, RED, SQUARE_SIZE, WHITE
from game.piece import Piece
import enum

class Board():
    def __init__(self):
        self.board = []
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

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

    def get_all_moves(self):
        moves = []
        correct_row = -1
        for col in range(COLS):
            for row in range(ROWS):
                if self.get_piece(row, col) == 0:
                    correct_row = row
            if correct_row != -1:
                moves.append((correct_row, col))
        return moves

    def simulate_move(self, row, col):
        self.board[row][col] = Piece(row, col, WHITE)
        return self.board


    def evaluate(self):
        score = 0
        for row in range(ROWS):
            for col in range (COLS):
                if row > 0:
                    if col > 0:
                        if self.get_piece(row, col) != 0 and self.get_piece(row, col) == self.get_piece(row - 1, col - 1): # UP LEFT
                            if self.get_piece(row, col).color == WHITE:
                                score += 10
                            else:
                                score -= 20
                    if col < COLS - 1:
                        if self.get_piece(row, col) == self.get_piece(row - 1, col + 1) and self.get_piece(row, col) != 0: # UP RIGHT
                            if self.get_piece(row, col).color == WHITE:
                                score += 10
                            else:
                                score -= 20
                if col > 0:
                    if self.get_piece(row, col) == self.get_piece(row, col - 1) and self.get_piece(row, col) != 0: # LEFT
                        if self.get_piece(row, col).color == WHITE:
                            score += 10
                        else:
                            score -= 20
                if col < COLS - 1:
                    if self.get_piece(row, col) == self.get_piece(row, col + 1) and self.get_piece(row, col) != 0: # RIGHT
                        if self.get_piece(row, col).color == WHITE:   
                            score += 10
                        else:
                            score -= 20
        if score != 0:
            print (f'Score is : {score}')
        return score

    def show(self):
        for row in range(ROWS):
            for col in range(COLS):
                print (f'{self.board[row][col]} ', end="")
            print ()
        print("\n\n")