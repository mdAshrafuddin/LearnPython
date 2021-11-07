"""
The game is as follows.
Computer has a list of words.
Computer chooses a random word from the list.
The player gets 10 wrong guesses (10 turns).
The game follows this loop
Computer prints the word character by character replacing with underscore those not guessed yet (initial no characters has been guessed).
Player guesses a character.
If character is not in word, a turn is withdrawn
If no turns left, computer wins.
If player has guessed all characters, player wins
An initial word list could be: ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
"""
import random 

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(words)

guesses = ''

truns = 10

while truns > 0:
    print(f"You have {truns} truns left")

    guessed_all = True
    for c in  word:
        if c in guesses:
            print(c, end='')
        else:
            print('_', end='')
            guessed_all = False
    print()

    if not guessed_all:
        guess = input('Guess a char: ')
        guesses = guesses + guess
        if guess not in word:
            truns = truns - 1
    else:
        truns = 0