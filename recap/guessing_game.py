# this is a guessing game code
# guess a number between 1 and 10

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(f"Guess a number\n you only have 3 guesses: "))
    guess_count += 1
    count = int(guess_count)
    print(f"this is guess number {count}")
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

