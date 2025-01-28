print("Welcome to the Computer Quiz Game!")
points = 0

playing= input("Do you want to play the game? ")

if playing.upper() != "YES":
    quit()
    
print("Okay! Let's play the game ;) ")

answer= input("What does ALU stands for? ")
if answer.upper() == "ARITHEMATIC LOGIC UNIT":
    print('It is a Correct answer')
    points+=5
else:
    print('It is a wrong answer')
    
answer= input("What's the most famous sport in the world? ")
if answer.upper() == "FOOTBALL":
    print('It is a Correct answer')
    points+=5
else:
    print('It is a wrong answer')
    
answer= input("Who's the most famous rapper in the world? ")
if answer.upper() == "EMINEM":
    print('It is a Correct answer')
    points+=5
else:
    print('It is a wrong answer')
    
if points>=10:
    print("Congrats you have passed")
else:
    print("Try again!!")
    
