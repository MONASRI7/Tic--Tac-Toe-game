board = [" "] * 9

def show_board():
    print("\n")
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print("\n")

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    return None

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    show_board()
    players = ["X", "O"]
    turn = 0

    while " " in board:
        try:
            move = int(input(f"Player {players[turn % 2]}, pick a spot (0-8): "))
            if 0 <= move < 9 and board[move] == " ":
                board[move] = players[turn % 2]
                show_board()
                winner = check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    return
                turn += 1
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number.")

    print("It's a draw!")

play_game()