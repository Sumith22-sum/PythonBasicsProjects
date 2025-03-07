import random

print("Welcome To The Code Guessing Game!!!")

def generate_code():
    "Generate a 4 - Digit Number as Secret Code"
    return random.randint(1000, 3000)
    
def code_game():
    print("Welcome To This Game!!!")
    print("You have only 10 Tries to guess The Correct Code")
    
    secret_code= generate_code()
    attempts= 0
    max_attempts= 10
    
    while attempts < max_attempts:
        try:
            guess= int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess your 4- Digit Code: "))
            if guess < 1000 or guess > 3000:
                print("Invalid Input! Enter correct 4 - Digit Code: ")
                continue
        except ValueError:
            print("Invalid Input!! Please Enter Numbers Only")
            continue
        
        attempts += 1
        
        if guess == secret_code:
            print(f"YOOOOHOOOO!!! Congrats!! You Guessed the code {secret_code} in {attempts} Attempts!")
            break
        elif guess > secret_code:
            print("Tooo High!! Try Again!!")
        else:
            print("Too Low!! Try Again!!")
            
    if attempts == max_attempts:
        print(f"Game Over!!! You've Used All {max_attempts} Attempts. The Correct Code Was {secret_code}")
        
if __name__ == "__main__":
    code_game()
