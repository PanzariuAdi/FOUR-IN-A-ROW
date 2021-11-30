import pygame
from game.board import Board
from game.constants import RED, ROWS, WHITE

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED

    def reset(self):
        self._init()

    def make_move(self, row, col):
        if self.board.get_piece(row, col) == 0:
            self.board.add_piece(self.win, row, col, self.turn)
            self.change_turn()

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
    
    def check_winner(self, row, col):
        pass