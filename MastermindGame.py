import random

print("Welcome To The Mastermind Game!!!")

COLORS = ["R", "B", "Y", "O"]

def generate_code():
    return [random.choice(COLORS) for _ in range(4)]
    
def feedback(code, guess):
    incorrect_pos = sum(a == b for a, b in zip(code, guess))  
    correct_pos = sum(min(code.count(c), guess.count(c)) for c in set(guess)) - incorrect_pos  
    return incorrect_pos, correct_pos
    
def play_mastermind():
    code = generate_code()
    attempts = 0
    max_attempts = 10  
    
    print("Welcome to this game!! Colors: R(Red), B(Blue), Y(Yellow), O(Orange)")
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: Enter 4 Colors (eg: RBYO): ").upper()
        
        if len(guess) != 4 or any(c not in COLORS for c in guess):
            print("Invalid Input. Use only R, B, Y, O (4 Characters)")
            continue
        
        guess = list(guess)  
        attempts += 1
        incorrect, correct = feedback(code, guess)
        
        print(f"Feedback: {incorrect} correct positions, {correct} correct colors in wrong positions")
        
        if incorrect == 4:
            print(f"Congrats!! You Cracked the code in {attempts} Attempts!!!")
            break
    else:
        print(f"Sorry, you've reached the maximum attempts ({max_attempts}). The correct code was {''.join(code)}.")

play_mastermind()
