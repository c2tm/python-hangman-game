# import string
# import random


# def load_words():
#     '''
#     return: list of valid words: words are strings of lower case letters
#     '''

#     with open('/usr/share/dict/words') as infile:
#         word_list = infile.read().splitlines()

#     return word_list


# def choose_word(word_list):
#     '''
#     return: Random selection from word_list, a list of strings
#     '''

#     return random.choice(word_list)


# def is_word_guessed(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word to guess
#     letters_guessed: list, letters the user has guessed so far

#     return: a boolean True if letters guessed == secret_word, false if otherwise
#     '''

#     for char in secret_word:
#         if char not in letters_guessed:
#             return False
#         else:
#             return True


# def get_available_letters(letters_guessed):
#     '''
#     letters_guesses: list, what letters have been guessed so far
#     return: string, comprised of letters that have not yet guessed
#     '''

#     letter_not_guessed = ''.join(
#         [i for i in string.ascii_lowercase if i not in letters_guessed])

#     return letter_not_guessed


# def get_guessed_word(secret_word, letters_guessed):
#     '''
#     secret_word: string, the word to guess
#     letters_guessed: list, what letters have been guessed so far

#     return: string of letters and underscores that represent what letters in secret_word have been guessed
#     '''

#     progress = ['_'] * len(secret_word)
#     secret_word_list = list(secret_word)
#     counter = 0

#     while counter < len(secret_word_list):

#         if secret_word_list[counter] in letters_guessed:
#             progress[counter] = secret_word_list[counter]

#         counter += 1
#         return ''.join(progress)


# def hangman(secret_word):
#     '''
#     secretWord: string, the word to guess

#     Start a game of Hangman

#     * At the start of the game, let the user know hoe many lettersd the secret_word
#     contains

#     *As the user to supply one guess (ie letter) per round

#     *The user shoudl recieve feedback immediately after each guess after each guess about whether their
#     guess appears in the randomly generated word

#     *after each round, you should display to the user the partially guessed word, as well as letters
#     that the user has not yet guessed

#     '''

#     remaining_guesses = 8
#     letters_guessed = []

#     print("Lets play Hangman")
#     print('I am thinking of a word that is',
#           str(len(secret_word)), 'letters long.')

#     while remaining_guesses > 0:
#         print('You have', remaining_guesses, 'guesses left.')
#         print('Avaiable letters: ', get_available_letters(letters_guessed))
#         user_guess = input('Please guess a letter: ').lower()

#         if user_guess in letters_guessed:
#             print('Oops! You have already guessed that letter',
#                   get_guessed_word(secret_word, letters_guessed))
#         else:
#             letters_guessed.append(user_guess)

#             if user_guess in secret_word:
#                 print("Good guess", get_guessed_word(
#                     secret_word, letters_guessed))
#             else:
#                 print("Incorrect guess", get_guessed_word(
#                     secret_word, letters_guessed))
#                 remaining_guesses -= 1
#         if is_word_guessed(secret_word, letters_guessed):
#             print("Congrats. You won!")
#             return

#     print('Sorry, You ran out of guesses. The word was', secret_word)


# word_list = load_words()
# secret_word = choose_word(word_list).lower()
# hangman(secret_word)


import string
import random

all_possible_guesses = list(string.ascii_lowercase)
answer_list = ['happy', 'sunny', 'fly', 'eaten', 'driver', 'monster']
# answer = list(random.choice(answer_list))
answer = list('happy')
progress = ['_'] * len(answer)
space = ' '
guesses_left = 9

print("\nLets play Hangman!")

while guesses_left > 0:
    print("\nGuesses remaining:", guesses_left)
    print("\nLetters remaining:", space.join(all_possible_guesses))
    print("\nYour progress:\n\n", space.join(progress))
    userGuess = input("\n\nPlease guess a letter!\n")

    guesses_left -= 1

    if userGuess not in all_possible_guesses:
        print("\n ***OOPS! You've already gueesed this letter!***\n")
        continue

    if userGuess in answer:
        print("\n", userGuess, " is in the word!\n")

        indexes = [i for i, char in enumerate(answer) if char == userGuess]

        indexes_length = len(indexes)
        counter = indexes_length - 1

        # progress is an empty list []
        # [2, 3]
        while counter >= 0:
            progress[indexes[counter]
                     ] = answer[indexes[counter]]

            if counter == 0:
                break

            counter = counter - 1

        asciiIndex = all_possible_guesses.index(userGuess)
        all_possible_guesses.pop(asciiIndex)

    if userGuess not in answer:
        print("\nIncorrect! ", guesses_left, " guesses remaining!\n")
        asciiIndex = all_possible_guesses.index(userGuess)
        all_possible_guesses.pop(asciiIndex)

    if progress == answer:
        print("\nThe word was '", ''.join(answer),
              "'!\nYou guessed the word with", guesses_left, "guesses left!\n")
        break

    if guesses_left == 0:
        print("\nGame Over\n")
        break
