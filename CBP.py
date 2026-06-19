import random
import string

# Generate password
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Check password strength
def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    return strength

# Give suggestions
def give_suggestions(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Make your password at least 8 characters long.")
    if not any(c.islower() for c in password):
        suggestions.append("Add some lowercase letters (a-z).")
    if not any(c.isupper() for c in password):
        suggestions.append("Add some uppercase letters (A-Z).")
    if not any(c.isdigit() for c in password):
        suggestions.append("Include some numbers (0-9).")
    if not any(c in string.punctuation for c in password):
        suggestions.append("Add special symbols (!, @, #, $, etc.).")

    return suggestions

# Get valid password length
def get_valid_length():
    while True:
        user_input = input("Enter password length (minimum 8, press Enter for default 8): ")

        if user_input == "":
            return 8

        elif user_input.isdigit():
            length = int(user_input)
            if length >= 8:
                return length
            else:
                print("Invalid! Length must be at least 8.")

        else:
            print("Please enter a valid number.")

# Main function
def main():
    print("=== PASSWORD GENERATOR & CHECKER ===")

    user_choice = input("Do you want to generate a new password? (y/n): ").lower()

    if user_choice == 'y':
        length = get_valid_length()
        password = generate_password(length)
        print(f"\nGenerated Password: {password}\n")

    else:
        password = input("Enter your password to check: ")

        strength = check_password_strength(password)
        suggestions = give_suggestions(password)

        print("Password Strength:", end=" ")

        if strength == 5:
            print("Very Strong")
        elif strength == 4:
            print("Strong")
        elif strength == 3:
            print("Moderate")
        elif strength == 2:
            print("Weak")
        else:
            print("Very Weak ")

        print("\nSuggestions:")
        if suggestions:
            for s in suggestions:
                print(" -", s)
        else:
            print(" - Your password looks great!")

# Run program
if __name__ == "__main__":
    main()
