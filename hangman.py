import random

# Step 1: List of words for the game
word_list = ["python", "java", "hangman", "programming", "computer", "openai", "github", "terminal"]

# Step 2: Choose a random word from the list
def choose_word():
    return random.choice(word_list).lower()

# Step 3: Display the current state of the word (with blanks)
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Step 4: Main Game Loop
def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed
    incorrect_guesses = set()
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        # Check if input is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter!")
            continue
        
        if guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses.add(guess)
            attempts -= 1
            print(f"Wrong guess! {guess} is not in the word.")
        
        # Check if player has guessed the word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nSorry, you ran out of attempts. The word was: {word}")

# Step 5: Run the game
hangman()
