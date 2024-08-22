import random  # Import the random module to select a random word from the list

from hangman_words import word_list  # Import the list of words for the game
from hangman_art import logo, stages  # Import the logo and stages for the game visuals

# Display the game's logo at the start
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)  # Get the length of the chosen word

end_of_game = False  # Variable to check if the game has ended
lives = 6  # Number of lives the player has

# For testing purposes, print the solution to the console
print(f'Pssst, the solution is {chosen_word}.')

# Create a list of blanks "_" representing each letter in the chosen word
display = []
for _ in range(word_length):
    display += "_"

# Main game loop that continues until the game ends
while not end_of_game:
    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the player has already guessed the letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter  # Replace the blank with the correct letter

    # If the guessed letter is not in the word, decrease the player's lives
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True  # End the game if the player runs out of lives
            print("You lose.")

    # Display the current state of the word with blanks and guessed letters
    print(f"{' '.join(display)}")

    # Check if the player has guessed all the letters
    if "_" not in display:
        end_of_game = True  # End the game if the player guesses the word
        print("You win.")

    # Display the current stage of the hangman based on remaining lives
    print(stages[lives])
