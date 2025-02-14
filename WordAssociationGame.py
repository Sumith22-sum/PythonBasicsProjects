import random
import time

print("Welcome To The Word Association Game!!!")
print("I'll say a word and you need to type what comes on your mind")
print("Don't repeat any words")

def word_association_game():
    words= ["apple", "sun", "car", "music", "book", "dog", "moon", "fire"]
    used_words= set()
    score= 0
    
    while True:
        word= random.choice(words).capitalize()
        print(f"\n My Word: {word}")
        response= input("Your Word: ").strip().capitalize()
        
        if response in used_words:
            print("OOPS!! You already used that word. Game Over!!!")
            break
        
        if len(response) == 0 or response == word:
            print("HMMMM....... That doesn't seems like a related word. Game Over!!!")
            break
        
        used_words.add(response)
        score += 1
        print("Nice!!! Keep Going.......")
        
        time.sleep(1)
        
    print(f"\n Your Score: {score}")
    print("Thanks For Playing!!! GOODBYE!!!")
        
word_association_game()    
