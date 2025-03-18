import random

print("Welcome To The Slot Machine Game!!")
print("Spin The Slot Machine And Win Your Prizes!!")

def spin():
    return [random.choice("ABCDE") for _ in range(3)]
    
balance = 150

while balance > 0:
    print(f"\n Balance: Rs. {balance}")
    bet= int(input("Enter to bet(0 to Quit): "))
    
    if bet == 0:
        print("Thanks For Playing This Game")
        break
    if bet > balance:
        print("Come On!! It's not Enough For U to Play")
        continue
        
    reels= spin()
    print(" | ".join(reels))
        
    if reels[0] == reels[1] == reels[2]:
        winnings = bet * 5
        print("EUUUUU JACKPOT BROOOO!! U WON Rs.", winnings)
    elif reels[0] == reels[1] or reels[1] == reels[2] or reels[0] == reels[2]:
        winnings= bet * 2
        print("OH Nice!! U Won Rs.", winnings)
    else:
        winnings = -bet
        print("OH Dang Bro!! U Lost Rs.", bet)
                
    balance += winnings
                
print("GAME OVER!!!")                
