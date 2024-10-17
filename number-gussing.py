import random

# Step 1: Generate a random number
def generate_number():
    return random.randint(1, 100)

# Step 2: Main game loop
def number_guessing_game():
    secret_number = generate_number()
    attempts = 10  # The player gets 10 attempts to guess the number
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Make a guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the correct number: {secret_number}")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    else:
        print(f"Sorry, you're out of attempts. The correct number was: {secret_number}")

# Step 3: Run the game
number_guessing_game()
