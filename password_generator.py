import random
import string

while True:
    print("\n----- PASSWORD GENERATOR -----")

    # Get password length safely
    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Password length must be greater than 0. Try again!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lower + upper + numbers + symbols

    # Generate password
    password = "".join(random.choice(all_chars) for _ in range(length))

    print("Your generated password is:", password)

    # Ask user to run again
    again = input("\nDo you want to generate another password? (yes/no): ").strip().lower()
    
    if again not in ("yes", "y"):
        print("Exiting program. Goodbye!")
        break