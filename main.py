from copy import deepcopy
import pygame
import pygame_menu
from game.board import Board
from game.constants import ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, RED, WHITE
from game.game import Game
from algorithm.minimax import minimax
from tkinter import *
from tkinter import messagebox


FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
ai_dificulty = 2
ai_player = False
pygame.init()
pygame.display.set_caption('4 in a row')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def set_dificulty(dificulty, value):
    global ai_dificulty
    ai_dificulty = value


def set_player(player, value):
    global ai_player
    ai_player = value


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    print (ai_player)
    while run:
        clock.tick(FPS)
        if ai_player:
            if game.turn == WHITE:
                value, new_board = minimax(game.board, ai_dificulty, False, game)
                game.ai_move(new_board)
        
        if game.check_winner(game.board) != None:
            Tk().wm_withdraw() #to hide the main window
            if game.check_winner(game.board) == RED:
                messagebox.showinfo('Game end !','RED PLAYER WON')
            else:
                messagebox.showinfo('Game end !','WHITE PLAYER WON')
            print(game.check_winner(game.board))
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.make_move(row, col)

        game.update()
    
    menu.mainloop(WIN)

'''
Main menu
'''
menu = pygame_menu.Menu('Welcome', 500, 500,
                       theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Play', main)
menu.add.selector('Enemy :', [('Player', False), ('AI', True)], onchange=set_player)
menu.add.selector('AI level :', [('Normal', 2), ('Good', 3)], onchange=set_dificulty)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(WIN)
main()