import pygame
from game.board import Board
from game.constants import COLS, RED, ROWS, WHITE

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
        correct_row = -1
        for i in range (0, ROWS):
            if self.board.get_piece(i, col) == 0:
                correct_row = i
        if correct_row != -1:    
            self.board.add_piece(self.win, correct_row, col, self.turn)
            possible_winner = self.check_winner(correct_row, col)
            if  possible_winner != None:
                return possible_winner
            self.change_turn()  
        return None

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
    
    def check_winner(self, row, col):
        # COLUMN : LEFT <- CURRENT POSITION
        score , count = 0, 0
        for i in range(col, col - 4, -1):
            if i >= 0 and i < COLS:
                score, count = self._calculate_score_count(row, i, score, count)
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # COLUMN : CURRENT POSITION -> RIGHT
        score, count = 0, 0
        for i in range(col, col + 4):
            if i >= 0 and i < COLS:
                score, count = self._calculate_score_count(row, i, score, count)
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # ROW : CURRENT POSITION -> DOWN
        score, count = 0, 0
        for i in range (row, row + 4):
            if i >= 0 and i < ROWS:
                score, count = self._calculate_score_count(i, col, score, count)
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # DIAGONAL : CURRENT POSITION -> TOP LEFT
        score, count = 0, 0
        correct_col = col
        for i in range(row, row - 4, -1):
            if i > 0 and i < ROWS and correct_col > 0:
                score, count = self._calculate_score_count(i, correct_col, score, count)
                correct_col -= 1
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # DIAGONAL : CURRENT POSITION -> TOP RIGHT
        score, count = 0, 0
        correct_col = col
        for i in range (row, row - 4, -1):
            if i > 0 and i < ROWS and correct_col < COLS:
                score, count = self._calculate_score_count(i, correct_col, score, count)
                correct_col += 1
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # DIAGONAL : CURRENT POSITION -> DOWN LEFT
        score, count = 0, 0
        correct_col = col
        for i in range (row, row + 4):
            if i > 0 and i < ROWS and correct_col > 0:
                score, count = self._calculate_score_count(i, correct_col, score, count)
                correct_col -= 1
        if self._winner(score, count) != None:
            return self._winner(score, count)

        # DIAGONAL : CURRENT POSITION -> DOWN RIGHT
        score, count = 0, 0
        correct_col = col
        for i in range (row, row + 4):
            if i > 0 and i < ROWS and correct_col < ROWS:
                score, count = self._calculate_score_count(i, correct_col, score, count)
                correct_col += 1
        if self._winner(score, count) != None:
            return self._winner(score, count)

        return None

    def _calculate_score_count(self, row, column, score, count):
        piece = self.board.get_piece(row, column)
        if piece != 0:
            count += 1
            if piece.color == RED:
                score += 1
        return score, count

    def _winner(self, score, count):
        if count != 4:
            return None
        else:
            if score == 0:
                return WHITE
            elif score == 4:
                return RED
            else:
                return None