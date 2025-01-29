passwords = {}

print("Welcome To The Password Manager!")
print("1. Add Password\n2. View Passwords\n3. Retrieve Passwords\n4. Exit")

while True:
    choices = input("\nEnter The Choices (1-4): ")
    
    if choices == "1":
        website = input("Enter The Website/App Name: ")
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        passwords[website] = {"username": username, "password": password}
        print("Password Saved!!")
        
    elif choices == "2":
        if passwords:
            for site in passwords:
                print(f"\nWebsite: {site}")
                print(f"Username: {passwords[site]['username']}")
                print(f"Password: {passwords[site]['password']}")
        else:
            print("No Passwords Saved!!")
            
    elif choices == "3":
        website = input("Enter Website/App Name to retrieve password: ")
        if website in passwords:
            print(f"\nWebsite: {website}")
            print(f"Username: {passwords[website]['username']}")
            print(f"Password: {passwords[website]['password']}")
        else:
            print("No password found for this website.")
            
    elif choices == "4":
        print("Exiting The Password Manager. GOODBYE!!")
        break
    
    else:
        print("Invalid Choice!! Please Enter Choices from (1-4) Only.")
