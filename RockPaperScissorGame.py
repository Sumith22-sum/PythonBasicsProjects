import random

def rock_paper_scissor():
    print("Welcome to the Rock Paper Scissor Game!")
    print("Type 'Rock','Paper', or 'Scissor' to play")
    print("Type 'exit' to Quit the game")
    
selection = ["Rock", "Paper", "Scissor"]
computer_points=0
user_points=0

while True:
    user_choice = input("Enter your choice(Rock, Paper, Scissor): ").capitalize()
    
    if user_choice == 'Exit':
        if(user_points > computer_points):
            print("user wins!!")
        elif(user_points == computer_points):
            print("Its a tie!!")
        else:
            print("You Lose!!")
        print("Thanks for playing!")
        break
   
    if user_choice not in selection:
        print("Invalid choice! Please choose from 'Rock', 'Paper', or 'Scissor'.")
        continue

    computer_choice = random.choice(selection)
    print(f"Computer chose: ",{computer_choice}) 
    
    if user_choice == computer_choice:
        print("It's a Tie!! Try Again.")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
             print("You WIN!!")
             user_points+=1
    else:
        print("You LOOSE!!")
        computer_points+=1
    
    print(f"Score: You - {user_points} , Computer - {computer_points}")
rock_paper_scissor()
