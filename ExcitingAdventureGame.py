name= input("Type your Name: ")
print("Welcome", name, "to this Exciting Adventure Game!!")

answer= input("You are in a Jungle, and there are two ways you can go left or right. Which way you would go? ")

if answer == "left":
    answer= input("You have come to a river, you can walk or swim accross? Type walk to walk and swim to swim accross: ")
    
    if answer == "swim":
        print("You swimmed accross the river but unfortunately got eaten by Alligator!!")
        
    elif answer == "walk":
        print("Well You walked for milles on this Jungle but unluckily you reached dead end, so You Lost!!")
        
    else:
         print("Not a Valid Option. You Loose!!")
    
elif answer == "right":
    answer= input("Well, You now came accross a wobbly highway, do you want to cross it or go back(cross/back)? ")
    
    if answer == "back":
        print("Well you are back to square one, You Lost!!")
        
    elif answer == "cross":
        answer= input("Well nice choice! You crossed and now met a stranger where they gave u gold!!Would you like to return the gold to the needy people in your society(yes/no)? ")
        
        if answer == "yes":
            print("Congrats!! Now you became a hero to this society, YOU WON THIS ADVENTURE GAME!! ")
            
        elif answer == "no":
            print("Well so sorry you didn't give needy people gold so they're dead because of you, You Lost the Game!! BETTER LUCK NEXT TIME!!")
        
    else:
         print("Not a Valid Option. You Loose!!")
    
else:
    print("Not a Valid Option. You Loose!!")
    
print("Thanks for playing this Exciting Adventure Game!!!", name)
