"""
Input a value from the user and keep it in variable a.
Input another value from the user and keep it in variable b.
Print the product of the two values (a*b).
"""
a = int(input("Enter the number "))
b = int(input("Enter the number "))

print((a*b))

"""
Input how many years the user it.
Convert the years to an integer.
Calculate how many days, hours, minutes, and seconds since the user is born.
"""
age = int(input("How many years "))
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"You are  {days} days old") 
print(f"You are  {hours} hours old") 
print(f"You are  {minutes} minutes old") 
print(f"You are  {seconds} seconds old") 

"""
Here we will make a tip calculator.
Input the price.
Convert the price to an integer.
Input the percentage the user wants to tip.
Convert the percentage to an integer.
Calculate the tip by the following formula: tip = price *  percentage_tip / 100.
Round the tip to two digits.
Print the the tip.
BONUS: Adjust the code to take float input of percentage tip
"""
price = int(input("Enter the Number "))
percentage = int(input("Enter the number "))

tip = price * percentage / 100

print(round(tip, 2))
