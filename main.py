#JHammit 

#Sample minimax program using straightforward tic-tac-toe board in python

#define winning moves in tic-tac-toe
def is_winner(board, player):
    win_conditions = [
        # Win by rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Wins by columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        # Win by diagonals
        (0, 4, 8), (2, 4, 6) 
    ]

    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

#define situation if there are no winners (draw)
def is_draw(board):
    return ' ' not in board

#define the minimax algorithm
def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, 'X'):
        return 10 - depth
    if is_winner(board, 'O'):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_val = float('-infinity')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                value = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                best_val = max(best_val, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
        return best_val
        
    else:
        min_val = float('infinity')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                value = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_val = min(min_val, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
        return min_val

#define the best move
def best_move(board):
    best_val = float('-inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False, float('-inf'), float('inf'))
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

# Current board state
board = [' ', ' ', ' ', 
         'O', ' ', ' ', 
         ' ', ' ', ' ']

#define board with current moves
def print_board(board):
    print("Current board state:")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

#define position board to explain potential moves
def print_positions():
    positions = ['0', '1', '2', 
                 '3', '4', '5', 
                 '6', '7', '8']
    print("Move Diagram:")
    print(positions[0] + " | " + positions[1] + " | " + positions[2])
    print("--+---+--")
    print(positions[3] + " | " + positions[4] + " | " + positions[5])
    print("--+---+--")
    print(positions[6] + " | " + positions[7] + " | " + positions[8])

# Print the current board state
print_board(board)
print()

# Print the position chart in a human-friendly format
print_positions()
print()

# Check for draw or determine the best move
if is_winner(board, 'X'):
    print("Player 'X' has won!")
elif is_winner(board, 'O'):
    print("Player 'O' has won!")
elif is_draw(board):
    print("The game is a draw.")
else:
    move = best_move(board)
    row, col = divmod(move, 3)
    print(f"The best move is at position {move}")

#end of program
