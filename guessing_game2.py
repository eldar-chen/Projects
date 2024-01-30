import random
# Generate a random number between 1 and 20


# Initialize variables
attempts = 0
points = 0
# Welcome message
print("Welcome to the Guess the Number Game!")

# Repeat function (do you want to play?)
repeat = input("Do you want to play again? (yes/no) ")
while repeat.lower() == "yes":
    target_number = random.randint(1, 21)

    while True:
        # exception for string value entered
        try:
        # Get user input for their guess
            user_guess = input("Enter your guess (between 1 and 20): ")
            # Quitting mid game
            if user_guess.lower() == "quit":
                quit()
            # convert input from string to int
            user_guess = int(user_guess)

            if user_guess < 1 or user_guess > 20:
                print("Out of range! please input a number 1 to 20")

            # Increment the attempts
            attempts += 1

            # Check if the guess is correct
            if user_guess == target_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                points += 10
                break
            elif user_guess < target_number:
                print("Too low. Try again.")
                points -= 1
            else:
                print("Too high. Try again.")
                points -= 1

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"your current score is {points} points")

    repeat = input("Do you want to play again? (yes/no) ")
    if repeat.lower() == "no":
        print("Thank you for playing")
        quit()