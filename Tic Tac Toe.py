#Tic-Tac-toe

import random

# The game board
board = [' ' for _ in range(9)]

# To insert a letter (X or O) at a given position on the board
def insert_letter(letter, pos):
    if pos < 0 or pos > 8:
        print("Invalid position!")
        return
    board[pos] = letter

# To check if the space is free
def space_is_free(pos):
    return board[pos] == ' '

# To print the board
def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# To check if the board is full
def is_board_full(board):
    return board.count(' ') == 0

# To check for a win
def is_winner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return -10
    elif is_winner(board, 'O'):
        return 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if space_is_free(i):
                insert_letter('O', i)
                score = minimax(board, depth + 1, False, alpha, beta)
                insert_letter(' ', i)
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if space_is_free(i):
                insert_letter('X', i)
                score = minimax(board, depth + 1, True, alpha, beta)
                insert_letter(' ', i)
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

# AI agent's move
def ai_move():
    best_score = -1000
    best_move = 0
    for i in range(9):
        if space_is_free(i):
            insert_letter('O', i)
            score = minimax(board, 0, False, -1000, 1000)
            insert_letter(' ', i)
            if score > best_score:
                best_score = score
                best_move = i
    insert_letter('O', best_move)
    print("\n AI's turn: \n")
    return

# Human player's move
def human_move():
    run = True
    while run:
        move = input("\n Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move - 1):
                    run = False
                    insert_letter('X', move - 1)  # Indent this line
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Main game loop
def play_game():
    print_board(board)
    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            human_move()
            print_board(board)
            if is_winner(board, 'X'):
                print("\n You win!! \n")
                break
            if is_board_full(board):
                break
            ai_move()
            print_board(board)
            if is_winner(board, 'O'):
                print("\n AI wins!! \n")
                break
        else:
            break

    if not(is_winner(board, 'O')) and not(is_winner(board, 'X')) and is_board_full(board):
        print('It\'s a tie!')

# Start the game
play_game()