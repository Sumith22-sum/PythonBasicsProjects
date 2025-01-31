import random
import time

print("Welcome To The Timed Math Challenge!!!")

OPERATORS= ["+", "-", "*"]
MIN_OPERAND= 3
MAX_OPERAND= 10
TIME_LIMIT= 10  

def generate_problem():
    left= random.randint(MIN_OPERAND, MAX_OPERAND)
    right= random.randint(MIN_OPERAND, MAX_OPERAND)
    operator= random.choice(OPERATORS)
    
    expr= str(left) + " " + operator + " " + str(right)
    answer= eval(expr)
    return expr, answer

def timed_challenge():
    correct_count = 0
    total_time = 0
    
    for i in range(5):  
        expr, correct_answer = generate_problem()
        print(f"Question {i + 1}: Solve this: {expr}")
        
        start_time= time.time()
        user_answer= input("Your answer: ")
        time_taken= time.time() - start_time
        
        if time_taken > TIME_LIMIT:
            print(f"Time's up! Correct answer: {correct_answer}.")
        elif int(user_answer)== correct_answer:
            print("Correct!")
            correct_count += 1
        else:
            print(f"Incorrect! Correct answer: {correct_answer}.")
        
        total_time += time_taken
    
    print(f"\nYou answered {correct_count} questions correctly out of 5.")
    print(f"Total time: {total_time:.2f} seconds.")

timed_challenge()
