import time

print("Hello!! This Is A WPM Typing Test!!")

sample_text = "The quick brown fox jumps over the lazy dog."

def typing_test():
    print("Type the following sentence:")
    print(sample_text)
    print("\nPress Enter to start.")
    
    input()
    
    print("\n Get ready...")
    time.sleep(1)
    print("3!!!")
    time.sleep(1)
    print("2!!!")
    time.sleep(1)
    print("1!!!")
    time.sleep(1)
    print("\nStart typing now!\n")
    
    start_time= time.time()
    typed_text= input()  
    end_time= time.time()
    time_taken= end_time - start_time
    words= len(typed_text.split())
    wpm= (words / time_taken) * 60
    correct_chars= sum(1 for a, b in zip(typed_text, sample_text) if a == b)
    accuracy= (correct_chars / len(sample_text)) * 100

    print(f"\nYou typed {words} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is {wpm:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")

    retry = input("\nDo you want to retry? (y/n): ").strip().lower()
    if retry == 'y':
        typing_test()
    else:
        print("Thank you for taking the typing test!")

typing_test()
