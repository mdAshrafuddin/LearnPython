"""
A word jumble is a word puzzle game that presents the player with a bunch of mixed up letters and requires them to unscramble the letters to find the hidden word.
The computer will take word and jumble it (mix up the letters).
Then the player will guess what the word is
An initial word list could be: ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
"""
import random

words = ['father', 'enterprise', 'science', 'programming', 'resistance', 'fiction', 'condition', 'reverse', 'computer', 'python']
word = random.choice(words)

jumble = ''.join(random.sample(word, len(word)))
print(f"The Jumple word is {jumble}")
guess = input("Write your guess: ")

if guess == word:
    print('Correct')
else:
    print(f"Incorrect: the word is {word}")