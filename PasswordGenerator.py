import random
import string

print("This is a Password Generator!!")

def generate_password(length):
    "Generating a secure password of given length"
    if length < 4:
        print("Sorry the password length should be atleast length of 4")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password= [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice(string.punctuation)]
    password += random.choices(characters, k= length - 4)
    random.shuffle(password)
    return "".join(password)
    
def main():
    "Main function to handle user interaction"
    while True:
        try:
            length= int(input("Enter desired password len(min 4): "))
            if length < 4:
                print("Error: Length must be atleast 4. Try Again!!")
                continue
        except ValueError:
            print("Invalid Input!! Please enter a Number: ")
            continue
        password= generate_password(length)
        if password:
            print("\n Generated Password: ",password)
        choice= input("\n Do you want to generate another password?(yes/no): ").strip().lower()
        if choice != 'yes':
            print("GoodBye!!")
            break
                    
if __name__  == "__main__":
    main()
