import random

print("Welcome To The PIG Game!!!")

def roll_die():
    return random.randint(1, 6)

def pig_game():
    scores = [0, 0]  
    player = 0  
    
    while max(scores) < 30:  
        turn_total = 0
        print(f"Player {player + 1}'s Turn: ")
        
        while True:
            roll = roll_die()
            print(f"Rolled: {roll}")
            
            if roll == 1:  
                print("Oops!! You rolled a 1. No points at all this round")
                turn_total = 0  
                break
            else:
                turn_total += roll  
                print(f"Turn total: {turn_total}")
                
                if input("Roll Again (y) or Hold (n)? ").strip().lower() == 'n':
                    break

        scores[player] += turn_total  
        print(f"Player {player + 1}'s total score: {scores[player]}")

        if scores[player] >= 30:
            print(f"\nYuuhuuu, Congrats!!! Player {player + 1} Wins with {scores[player]} Points!!!")
            break
        
        player = 1 if player == 0 else 0  

pig_game()
