# Tic-Tac-Toe Game with AI using Minimax and Alpha-Beta Pruning in Python

import random
board = [" " for _ in range(9)]

#board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

#check win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# board full
def check_draw():
    return " " not in board

# available move
def available_moves():
    return [i for i, x in enumerate(board) if x == " "]

# minmax algorithm
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_win("O"):
        return 1
    elif check_win("X"):
        return -1
    elif check_draw():
        return 0

    if maximizing_player:
        max_eval = -float("inf")
        for move in available_moves():
            board[move] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in available_moves():
            board[move] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
# ai move
def ai_move():
    best_move = -1
    best_eval = -float("inf")
    alpha = -float("inf")
    beta = float("inf")
    for move in available_moves():
        board[move] = "O"
        eval = minimax(board, 0, False, alpha, beta)
        board[move] = " "
        if eval > best_eval:
            best_eval = eval
            best_move = move
        alpha = max(alpha, eval)
    return best_move

# play again
def play_again():
    while True:
        try:
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice not in ["y", "n"]:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please enter 'y' or 'n'.")
            continue

        if choice == "y":
            return True
        else:
            return False


while True:
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board()

        if current_player == "X":
            try:
                move = int(input("Enter a position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    raise ValueError
            except (ValueError, IndexError):
                print("Invalid move. Try again.")
                print("Enter the position between 1 to 9")
                continue
        else:
            print("AI is thinking...")
            move = ai_move()

        board[move] = current_player

        if check_win(current_player):
            print_board()
            if current_player == "X":
                print("Player X wins!")
            else:
                print("AI wins!")
            break
        elif check_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    if not play_again():
        break
