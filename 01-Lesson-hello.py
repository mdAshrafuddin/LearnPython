# Goal 
"""
    Get start python code hello world
    Understand print methot input and output
    Learing string method: lowar upper capitalize, replace 
"""

# Hello print 
print('Assalamu Alaikum')

# in print number srting anything all
print('Ashraf Uddin', 22, 33.4)

# Input value from user
x = input("Enter Number Please x : ")
y = input("Enter Number Please y : ")

if x == y:
    print("Number is Equal",)
else:
    print("Not Equal")

# Upper case
upperL = "Ashraf"
print(upperL.upper())

# small case
smallL = "Ashraf"
print(smallL.lower())

# capitlize case
capitalizeL = "ashraf"

print(capitalizeL.capitalize())

# Chheck isdecimal
print("2334".isdecimal()) #True

print("Ashraf".isdecimal()) #False