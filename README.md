# Tic Tac Toe Game

This repository contains a simple, interactive, console-based Tic Tac Toe game written in Python.

## Features

- **Single-player Mode (against AI)**: Play against the AI. The AI selects moves randomly but can detect and prioritize blocking or winning moves.
- **Two-player Mode**: Play with another person locally.
- **Save and Load Game**: Save your game progress at any time and resume from where you left off.

## How to Play

1. **Run the Tic Tac Toe Game**:
   - Run the game using the command:
     ```bash
     python main.py
     ```

2. **Choose the Game Mode**:
   - **Single-player (against AI)**: You play as Player 1 (`X`), and the AI plays as Player 2 (`O`).
   - **Two-player**: Both players alternate turns.

3. **Make a Move**:
   - Enter a number between 1 and 9 to place your mark on the board:
     ```
     1 | 2 | 3
     ---+---+---
     4 | 5 | 6
     ---+---+---
     7 | 8 | 9
     ```

4. **Save the Game**:
   - Type `'s'` during your turn to save your progress and exit.
   - The game saves to a file named `game_state.txt`.

5. **Resume a Saved Game**:
   - If a saved game exists, it will load automatically the next time you start the program.

## Game Rules

- The game is played on a 3x3 grid, where players alternate placing their marks (`X` or `O`) in an empty space.
- The first player to align three marks in a row (horizontally, vertically, or diagonally) wins.
- If all positions are filled without a winner, the game ends in a draw.

## Author

- **Nitin Dhiman**
