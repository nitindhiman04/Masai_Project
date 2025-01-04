#Tic-Tac-Toe
def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("Current Board:")

def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def is_draw(board):
    return all(cell != " " for cell in board)

def save_game(board, current_player):
    """Saves the current game state to a file."""
    with open("game_state.txt", "w") as f:
        f.write("".join(board) + "\n")
        f.write(current_player)

def load_game():
    """Loads the game state from a file."""
    try:
        with open("game_state.txt", "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                board = list(lines[0].strip())
                current_player = lines[1].strip()
                if len(board) == 9:
                    return board, current_player
                else:
                    return [" " for _ in range(9)], 'X'
            else:
                return [" " for _ in range(9)], 'X'
    except FileNotFoundError:
        return [" " for _ in range(9)], 'X'

import random
def random_move(board):
    """AI makes a random move based on a simple strategy."""
    for i in range(9):
        if board[i] == " ":
            board[i] = 'O'
            if check_winner(board, 'O'):
                board[i] = " "
                return i
            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = 'X'
            if check_winner(board, 'X'):
                board[i] = " "
                return i
            board[i] = " "

    empty_cells = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_cells)

def main():
    """Main function to run the Tic Tac Toe game."""
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")

    board = [" " for _ in range(9)]
    current_player = 'X'

    loaded_game = load_game()
    if loaded_game[0] and loaded_game[1]:
        board, current_player = loaded_game
        print("Game loaded from file.")

    mode = input("Choose game mode (1: Single-player Mode (against AI), 2: Two-player Mode): ")

    while True:
        print_board(board)

        if current_player == 'O' and mode == '1':
            move = random_move(board)
            print(f"AI chooses position {move + 1}")
        else:
            try:
                user_input = input(f"Player {current_player}, enter your move (1-9 or 's' to save and exit): ")
                if user_input.lower() == 's':
                    save_game(board, current_player)
                    print("Game saved. Exiting.")
                    break
                move = int(user_input) - 1
                if not 0 <= move <= 8 or board[move] != ' ':
                    raise ValueError("Invalid move.")
            except ValueError as e:
                print(e)
                continue

        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
