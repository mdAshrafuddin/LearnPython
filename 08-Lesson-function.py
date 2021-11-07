"""
A function is a block of code that performs a task. It can be called and reused 
multiple times. You can pass information to a function and it can send information back
"""

def my_func(): #
    print('Hello Function')

my_func()

# pass parameter and argument
def print_name(name):
    print(f"Your name {name}")

print_name("Ashraf Uddin")

def print_age(name, age):
    print(f"Your name {name} and age {age}")

print_age("Tanjil", 23)

# calculate age
def calculate_age(birth_year):
    return 2021 - birth_year

print(calculate_age(1994))


print(ord('A'))
print(ord('B'))
print(chr(65))

for c in range(65, 65 + 26):
    print(f"{c} is {chr(c)}")

hours = 50
print((hours * 3) % 24)

# even  and odd
def is_even(n):
    if n % 2 == 0:
        print('even')
    else:
        print('Odd')

is_even(2)

for i in range(10):
    print(i, end=' ')
    is_even(i)
