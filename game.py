import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def check_user_input(secret_word, user_guess):
    """

    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, the users guess
    :return: False if user_guess does not satisfy at least
	     one of the below conditions, True otherwise.
    1. must consist of only letters (uppercase or lowercase)
    2. must be the same length as secret_word
    3. must be a word found in words.txt
    """
    if len(user_guess) != len(secret_word):
        print("Oops! That word length is not correct.")
        return False

    if str.isalpha(user_guess) == False:
        print("Oops! That is not a valid word.")
        return False

    if str.lower(user_guess) not in wordlist:
        print("Oops! That is not a real word.")
        return False

    else:
        return True
    pass

def get_guessed_feedback(secret_word, user_guess):
    """

    :param secret_word: a string, the word to be guessed
    :param user_guess: a string, a valid user guess
    :return: a string with uppercase and lowercase letters and
	     underscores, each separated by a space (e.g. 'B _ _ S u')
    """
    feedback = ""
    for i in range(len(user_guess)):
        if user_guess[i] == secret_word[i]:
            feedback += (user_guess[i]).upper() + " "
        elif user_guess[i] in secret_word:
            feedback += (user_guess[i]).lower() + " "
        else:
            feedback += "_ "
    feedback = feedback.strip()
    return feedback
    pass

def get_alphabet_hint(secret_word, all_guesses):
    """
    takes in the secret word and a list of all previous guesses and returns a string of hint text
    :param secret_word: a string, the word to be guessed
    :param all_guesses: a list of all the previous valid guesses the user inputed
    :return: a string which replaces letters that were incorrect guesses with underscores and puts
	     semi-correct guesses (correct letter, incorrect place) in /x/
    """
    # we have coded this for you
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    out_list = []
    for char in alphabet:
        out_list.append(" "+char+" ")

    for guess in all_guesses:
        for i, char in enumerate(list(guess)):
            if char not in secret_word:
                out_list[alphabet.find(char)]=" _ "
            elif char != secret_word[i]:
                out_list[alphabet.find(char)] = "/"+char+"/"
            elif char == secret_word[i]:
                if secret_word.count(char) > guess.count(char):
                    out_list[alphabet.find(char)] = "/" + char + "/"
                else:
                    out_list[alphabet.find(char)] = "|" + char.upper() + "|"
    return "".join(out_list)

def wordle(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Wordle.

    * At the start of the game, let the user know how many letters the
      secret_word contains and how many guesses and warnings they start with.

    * The user should start with 6 guesses and 3 warnings

    * Before each round, you should display to the user how many guesses
      they have left.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a valid word!

    * The user should receive feedback immediately after each guess about
      whether their guess is valid, how closely it matches the secret_word,
      and the alphabet hint.

    * After each guess, you should display to the user the progression of
      their partially guessed words so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Wordle!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    warnings = 3
    guesses = 6
    print(f'You have {warnings} warnings remaining.\nYou have {guesses} guesses left.')

    all_guesses = []

    unique = ""
    for chars in secret_word:
        if chars not in unique:
            unique += chars

    while guesses > 0:
        user_guess = input("Please guess a word: ")
        guess = str.lower(user_guess)

        if check_user_input(secret_word, guess) == False:

            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1

            print(f'You have {warnings} warnings remaining.')
            print("-----------------")
            print(f'You have {guesses} guesses left.')

        elif guess != secret_word and check_user_input(secret_word, guess) == True:
            guesses -= 1
            all_guesses.append(guess)
            for i in all_guesses:
                print(get_guessed_feedback(secret_word, i))
            print("Alphabet HINT:")
            print(get_alphabet_hint(secret_word, all_guesses))
            if guesses != 0:
                print("-----------------")
                print(f'You have {guesses} guesses left.')

        elif guess == secret_word:
            guesses -= 1
            print("Congratulations, you won!")
            print(f'You guesses the correct word in {6-guesses} tries!')

            score = guesses * len(unique)
            print(f'Your total score is {score}.')
            break

    if guesses == 0:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


if __name__ == "__main__":
    # pass

    # To test, comment out the `pass` line above and uncomment:
    # - either of the `secret_word = ...` lines below, depending on how you want to set the secret_word
    # - the `wordle(secret_word)` line to run the game

    # uncomment and change the line below to a specific word for testing
    # secret_word = "test"

    # uncomment the line below for a randomly generated word
    # secret_word = choose_word(wordlist)

    # wordle(secret_word)
