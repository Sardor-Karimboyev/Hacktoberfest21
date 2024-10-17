import random
import time

# Step 1: Generate a random math problem
def generate_problem():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])

    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    else:  # For division, avoid decimals and ensure num1 is divisible by num2
        while num1 % num2 != 0:
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
        answer = num1 // num2

    return f"{num1} {operation} {num2}", answer

# Step 2: Main game loop
def math_quiz():
    score = 0
    incorrect = 0
    time_limit = 30  # Set a time limit of 30 seconds
    start_time = time.time()

    print("Welcome to the Math Quiz! You have 30 seconds to answer as many questions as possible.")
    print("Let's go!\n")

    while time.time() - start_time < time_limit:
        problem, correct_answer = generate_problem()
        print(f"Solve: {problem}")

        try:
            player_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if player_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.\n")
            incorrect += 1

    print("\nTime's up!")
    print(f"Your final score: {score} correct, {incorrect} incorrect.")

# Step 3: Run the game
math_quiz()
