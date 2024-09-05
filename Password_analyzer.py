import re
import random
import string

def analyze_password(password):
    # Initialize the strength score
    strength_score = 0

    # Length check
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password is too short. It should be at least 8 characters long.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

    # Output the strength
    if strength_score == 5:
        print("Strong password!")
    elif 3 <= strength_score < 5:
        print("Moderate password.")
        suggest_password()
    else:
        print("Weak password.")
        suggest_password()

def suggest_password():
    length = 12  # Default length of the generated password
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(random.choice(characters) for i in range(length))
    print(f"Suggested secure password: {secure_password}")

# Test the function
password = input("Enter your password: ")
analyze_password(password)