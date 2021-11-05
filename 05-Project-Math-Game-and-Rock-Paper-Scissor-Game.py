"""
Math Game
First, import random
Get a random inteteger from the range 1 to 10 (both inclusive)
Get another random inteteger from the range 1 to 10 (both inclusive)
Prompt the user for what the two integers multiplied is
Print if correct or not. If not corrrect, print the correct answe
"""

import random

a = random.randint(1, 10)
b = random.randint(1, 10)

answer = input(f"What is {a} times {b} ")
answer = int(answer)

if(answer == a*b):
    print(f"Correct {a} times {b} is {answer}")
else:
    print(f"inCorrect {a} times {b} is {answer}")

# Rock, Paper, Scissors Game
print("Enter choice: 1 : Rock 2 : Paper 3 : Scissor")
choice = input('Choice (1/2/3 : ')
choice = int(choice)

computer_choice = random.randint(1, 3)
print(f"Computer {computer_choice}")

if choice == computer_choice:
    print('Draw')
elif choice == 1: # Rock
    if computer_choice == 2: # Paper
        print('Computer wins')
    else:
        print('You wins')
elif choice == 2: # Paper
    if computer_choice == 1: #Rock
        print('You wins')
    else:
        print('Computer wins')
elif choice == 3:
    if computer_choice == 1:
        print('Computer wins')
    else:
        print('You Wins')



