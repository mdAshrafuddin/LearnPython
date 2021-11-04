"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
"""

a = 344
b = 56

if (a > b):
    print("a is greater than b")
elif (a == b):
    print("A equla b")
else:
    print('b is greater than a')

# Short hand if is used only one statement
if a > b: print("A is greater than b")

# short hand if....else
n = 30
m = 45

print('N') if (n > b) else print("M")

a1 = 34
b1 = 343
c1 = 45

print("A1") if (a1 > b1) else print("=") if(a1 == b1) else print("B1")

# and keyword both are true
if(a1 > b1 and c1 > a1):
    print("Both condition are true")

# or 
a = 200
b = 33
c = 500

# or 
if(a > b or c > a):
    print('At least one of the condition true')

# Nested If
result = 44

if(result > 10):
    print("Result above 10")
    if(result > 20):
        print("and also above 20!")
    else:
        print("but not above 20!")

# pass
aP = 23
bP = 45

if (aP > bP):
    pass