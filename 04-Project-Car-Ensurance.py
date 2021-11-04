
"""
This is a fictional car insurance company called Car Crash
They calculate the yearly ensurance price based on the current market price of the car
Given the market price: market_price
Then the yearly ensurance price is 9% of the market_price if it is a male above 26 years old.
As we see in the decision tree, we have 4 possible price calculations.
Create a program, which takes input and based on that calculated the correct price for all 4 cases
"""

gender = input("What is your gender (m/f) ")
gender = gender.upper()

if gender == "M":
    print("Male")
    age = int(input("What is your age "))
    if(age <= 26):
        print("Less/Equal to 26")
        percentage = 26
    else:  
        print("More than 26")
        percentage = 9
elif gender == "F":
    print("Fmale")
    car_type = ("What is your car type (sports / non sports)")
    sports = car_type.upper()
    if(car_type == "SPORTS"):
        print("Sports car")
        percentage = 21
    else:
        print("Non Sport car")
        percentage = 10
else:
    print("Worng input")
    percentage = None

market_price = input("what is you market price of you car: ")
market_price = int(market_price)
ensurance = market_price * percentage / 100

print(f"Insurance Offer: {ensurance}")