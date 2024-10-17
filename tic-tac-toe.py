# Step 1: Display the Board
def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Step 2: Player Input
def player_input(board, player):
    while True:
        try:
            choice = int(input(f"Player {player}, choose your move (1-9): ")) - 1
            if board[choice] == " ":
                board[choice] = player
                break
            else:
                print("This spot is already taken!")
        except (IndexError, ValueError):
            print("Invalid input! Choose a number between 1 and 9.")

# Step 3: Check for Win or Tie
def check_win(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def check_tie(board):
    return " " not in board

# Step 4: Main Game Loop
def tic_tac_toe():
    board = [" "] * 9  # Empty board
    current_player = "X"
    
    while True:
        display_board(board)
        player_input(board, current_player)
        
        # Check if the player has won
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Play the game
tic_tac_toe()
