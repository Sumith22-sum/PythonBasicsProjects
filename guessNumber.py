import random

def number_guess_game():
    print("Welcome to the Number Guess Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    number_to_guess= random.randint(1, 100)
    attempts= 0
    
    while True:
        try:
            guess= int(input("Enter your Guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("The guess is Low! Come on, Try Again")
            elif guess > number_to_guess:
                print("The guess is High! Come on, Try Again")
            else:
                print(f"Congrats! You guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please Enter a Number: ")
            
number_guess_game()
