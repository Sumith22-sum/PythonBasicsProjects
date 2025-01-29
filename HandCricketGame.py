import random

user_score= 0
computer_score= 0

while True:
    user_input=int(input("Your Turn(1-6): "))
    if user_input < 1 or user_input > 6:
        print("Invalid number! Please enter the valid number(1-6): ")
        continue
    
    computer_input= random.randint(1,6)
    print(f"Computer chooses: {computer_input}")
    
    if user_input == computer_input:
        print(f"OUT!!! Your Final score: {user_score}")
        break
    else:
        user_score += user_input
        print(f"Your score is: {user_score}")
        
print("Your Turn's Over!!!")

while True:
    user_input=int(input("Your Turn(1-6): "))
    if user_input < 1 or user_input > 6:
        print("Invalid number! Please enter the valid number(1-6): ")
    
    print("Computer's Turn: ")
    computer_input= random.randint(1,6)
    print(f"Computer chooses: {computer_input}")
    
    if computer_input == user_input:
        print(f"OUT!!! Computer's Final score:{computer_score}")
        break
    else:
        computer_score += computer_input
        print(f"Computer's score is: {computer_score}")
        
print("Computer Turn's Over!!!")

if user_score > computer_score:
    print(f"Congratulations! You win with {user_score} points!")
elif computer_score > user_score:
    print(f"Computer wins with {computer_score} points!")
else:
    print(f"It's a tie! Both you and the computer have {user_score} points.")

    
print("MATCH OVER!!!")
