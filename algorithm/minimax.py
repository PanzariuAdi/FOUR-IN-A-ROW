from copy import deepcopy
from game.constants import RED, WHITE, ROWS, COLS
import pygame
from game.piece import Piece
from game.board import Board


def minimax(position, depth, max_player, game):
    if depth == 0 or game.check_winner(position) != None:
        return position.evaluate(), position
    
    if max_player:
        max_eval = float('-inf')
        best_move = None    
        for board in get_all_boards(position):
            evaluation = minimax(board, depth - 1, False, game)[0]
            max_eval = max(max_eval, evaluation)
            if max_eval == evaluation:
                best_move = board
        return max_eval, best_move  
    else:
        min_eval = float('inf')
        best_move = None
        for board in get_all_boards(position):
            evaluation = minimax(board, depth - 1, True, game)[0]
            min_eval = min(min_eval, evaluation)
            if min_eval == evaluation:
                best_move = board
        return min_eval, best_move


def get_all_boards(board):
    boards = []

    for move in board.get_all_moves():
        temp_board = deepcopy(board)
        temp_board.simulate_move(move[0], move[1])
        boards.append(temp_board)
    return boards