# Wordle
Like the popular game Wordle, try to guess the secret word!

This game is to be copied and pasted into a IDE which can be played in the terminal. The words.txt file must be in the folder with the game.py file as well.

# General Description of the Game
The correct word can be of any length (not just 5 letters).
The user input will still need to be the same length as the correct word; that is, we will tell the user the length of the secret word.
After three invalid inputs, the user will lose a guess, and will continue losing a guess for each subsequent invalid input.

The user submits one “word” of the correct length at a time.
Each letter in the word that is in the correct place will be capitalized (same as green in the original wordle game). Each letter in the word that is in the incorrect place will be made lowercase (same as yellow in the original wordle game). If it’s not in the word at all, it will remain as an underscore.
The user's past guesses will be displayed in the format above, in addition to an alphabet hint which shows the user's current correct vs. incorrect letters.

The game will repeat until either (1) the user is out of guesses; or (2) the user correctly guesses the secret word.
If the user guesses the word correctly, a score will be calculated. The score is equal to the user's guesses remaining multiplied by the number of unique letters in the secret word.

Have fun!
