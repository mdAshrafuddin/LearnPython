"""
The random module is a built-in module to generate the pseudo-random variables. 
It can be used perform some action randomly such as to get a random number, 
selecting a random elements from a list, shuffle elements randomly, etc.
"""

import random

# The random.randint() method returns a random integer between the specified integers.
print(random.randint(1, 6))

a = random.randint(1, 6)
print(a)

""" 
The random.randrange() method returns a randomly selected element from 
the range created by the start, stop and step arguments. 
The value of start is 0 by default. Similarly, the value of step is 1 by default.
"""
print(random.randrange(1, 2))

# The uniform() method returns a random floating number between the two specified numbers
print(random.uniform(0,4))

"""
To generate a random floating point number using 
Gaussian distribution in Python, use gauss() function of Python random package. 
"""
print(random.gauss(0, 1))

"""
The random.choice() method returns a randomly 
selected element from a non-empty sequence. 
An empty sequence as argument raises an IndexError.
"""
print(random.choice('Ashraf'))

# The random.shuffle() method randomly reorders the elements in a list.
numbers=[12,23,45,67,65,43]
random.shuffle(numbers)
print(numbers)