import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize a variable to count the number of attempts
attempts = 0

# Ask the user to guess the number
print("Welcome to the Guessing Game!")
print("I have selected a secret number between 1 and 100. Can you guess it?")

while True:
    try:
        # Read user input as an integer
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check if the guess is correct, too high, or too low
        if guess < secret_number:
            print("Too low ! Try again.")
        elif guess > secret_number:
            print("Too high ! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break  # Exit the loop if the guess is correct
    except ValueError:
        print("Invalid input. Please enter a valid number.")
