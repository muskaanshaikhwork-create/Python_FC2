# Project 4: Zodiac Sign Finder Using Pandas

# Problem Statement:
# Given the birthdate and name of the person, you want to create a Python
# program to determine the corresponding Zodiac sign based on the date.

# Question:
# How can you write a Python program that takes name and birthdate as input
# and outputs the corresponding Zodiac sign and store it in a file using Pandas?

import pandas as pd

# Get user input
name = input("Enter your name: ")
day = int(input("Enter birth day (1-31): "))
month = int(input("Enter birth month (1-12): "))

# Function to determine Zodiac sign
def zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"

# Find Zodiac sign
sign = zodiac_sign(day, month)

# Create DataFrame
data = {
    "Name": [name],
    "Birth Day": [day],
    "Birth Month": [month],
    "Zodiac Sign": [sign]
}

df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("zodiac_sign.csv", index=False)

# Display result
print("\nName:", name)
print("Zodiac Sign:", sign)
print("Data saved successfully in 'zodiac_sign.csv'")