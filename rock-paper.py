import random

# Step 1: Define the possible choices
choices = ["rock", "paper", "scissors"]

# Step 2: Determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Step 3: Main game loop
def rock_paper_scissors():
    while True:
        # Get player choice
        player_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        if player_choice not in choices:
            print("Invalid choice! Please choose Rock, Paper, or Scissors.")
