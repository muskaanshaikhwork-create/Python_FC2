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
