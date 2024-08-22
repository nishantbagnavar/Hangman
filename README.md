# Hangman Game

## Description
This project is a Python implementation of the classic Hangman game. The game randomly selects a word from a predefined list, and the player has to guess the word letter by letter. The player is given 6 lives, and each incorrect guess reduces the number of lives. If the player guesses all the letters correctly before running out of lives, they win. Otherwise, they lose. The game also provides visual feedback on the number of remaining lives through ASCII art.

## Features
- A list of words for the game, making each game unique.
- ASCII art that visually represents the hangman as the game progresses.
- User-friendly prompts and messages throughout the game.
- Basic error handling to notify the player if they repeat a guess.

## How to Run
1. Ensure you have Python installed on your machine.
2. Download or clone the repository.
3. Make sure the `hangman_words.py` and `hangman_art.py` files are in the same directory as the main script.
4. Run the script using the command:
   ```bash
   python hangman.py
