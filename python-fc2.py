#Project 1
 #Problem Statement:
    #You want to create a simple game of Rock-Paper-Scissors in Python that 
    # takes the input as Rock, Paper, or Scissors and allows you to compete against the computer.

 #Question:
    #How can you create a Python program that allows the player to play Rock-Paper-Scissors 
    # against the computer?

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

player = input("Enter rock, paper, or scissors: ")

if player not in choices:
    print("Invalid Choice!")

elif player == computer:
    print("It's a Tie!")

elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You Win!")

else:
    print("Computer Wins!")

print("Your Choice:", player)
print("Computer Choice:", computer)


# Project 2: Binary Search Algorithm

# Problem Statement:
# You want to implement a Binary Search algorithm in Python to efficiently
# search for a target value in a sorted list.

# Question:
# How can I write a Python program that uses the Binary Search algorithm
# to find a target value in a sorted list?

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorted list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# User input
target = int(input("Enter the number to search: "))

# Call the function
result = binary_search(numbers, target)

# Display the result
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found.")


# Project 3: Send Emails Using Python

# Problem Statement:
# You want to write a Python program that can send emails to one or multiple
# recipients using an email account.

# Question:
# How can I write a Python program that can send emails to one or multiple
# recipients using an email account?


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender email credentials
sender_email = "muskaanshaikhwork@gmail.com"
sender_password = "password"

# List of recipients
recipients = [
    "recipient1@gmail.com",
    "recipient2@gmail.com"
]

# Email subject and body
subject = "Test Email"
body = "Hello,\n\nThis is a test email sent using Python.\n\nThank you!"

# Create email message
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)

# Send email to each recipient
for recipient in recipients:
    message["To"] = recipient
    server.sendmail(sender_email, recipient, message.as_string())
    print(f"Email sent to {recipient}")

# Close the connection
server.quit()
print("All emails sent successfully.")

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


# Project 5: Bulk File Renaming

# Problem Statement:
# Often, we have a large number of files in a directory with names that do not
# follow a specific pattern or are not easy to understand. Renaming each file
# manually can be time-consuming and error-prone. To solve this problem, we
# need a program that can rename a large number of files in bulk, based on a
# specified pattern.

# Question:
# Can you develop a Python program that takes a directory path and a pattern
# as input, and renames all the files in the directory that match the pattern
# to a new name that follows the specified pattern?

import os

# Take directory path and pattern as input
directory = input("Enter the directory path: ")
pattern = input("Enter the pattern to search for: ")
new_pattern = input("Enter the new pattern: ")

# Get all files in the directory
files = os.listdir(directory)

count = 1

# Rename matching files
for file in files:
    old_path = os.path.join(directory, file)

    if os.path.isfile(old_path) and pattern in file:
        extension = os.path.splitext(file)[1]
        new_name = new_pattern + str(count) + extension
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)

        print(f"Renamed: {file} -> {new_name}")
        count += 1

print("All matching files have been renamed successfully.")


# Project 6: Web Scraping Using Beautiful Soup

# Problem Statement:
# The task is to scrape the list of largest companies in US by revenue from
# Wikipedia using Beautiful Soup in Python. The data required includes the
# rank, name of company, Industry, Revenue, Revenue growth, Headquarters.

# Question:
# What is the process to extract data from the Wikipedia website using
# Beautiful Soup in Python? Specifically, how can we extract the rank,
# name of the company, Industry, Revenue, Revenue growth, Headquarters
# for the top US companies by Revenue?

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")

data = []

for row in rows[1:]:
    cells = row.find_all(["th", "td"])

    if cells:
        row_data = [cell.get_text(strip=True) for cell in cells]
        data.append(row_data)

df = pd.DataFrame(data)

print(df.head())