#!/usr/bin/env python3
import random
import string
import secrets

def generate_strong_password(length):
    """
    Generate a strong password with the specified length.
    Includes uppercase, lowercase, digits, and special characters.
    """
    if length < 4:
        print("Password length should be at least 4 characters for security.")
        return None
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure password has at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(secrets.choice(all_chars))
    
    # Shuffle the password list to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def check_password_strength(password):
    """
    Check and display password strength indicators.
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password)
    
    strength_score = sum([has_lower, has_upper, has_digit, has_special])
    
    print(f"\nPassword Strength Analysis:")
    print(f"✓ Lowercase letters: {has_lower}")
    print(f"✓ Uppercase letters: {has_upper}")
    print(f"✓ Numbers: {has_digit}")
    print(f"✓ Special characters: {has_special}")
    print(f"Length: {len(password)} characters")
    
    if strength_score == 4 and len(password) >= 12:
        print("Strength: Very Strong 🔒")
    elif strength_score >= 3 and len(password) >= 8:
        print("Strength: Strong 🔐")
    elif strength_score >= 2:
        print("Strength: Medium ⚠️")
    else:
        print("Strength: Weak ❌")

def main():
    print("=== Strong Password Generator ===")
    print("This tool generates cryptographically secure passwords.")
    
    while True:
        try:
            # Get password length from user
            length = int(input("\nEnter desired password length (minimum 4): "))
            
            if length < 4:
                print("Please enter a length of at least 4 characters.")
                continue
            
            # Generate password
            password = generate_strong_password(length)
            
            if password:
                print(f"\nGenerated Password: {password}")
                check_password_strength(password)
                
                # Ask if user wants another password
                again = input("\nGenerate another password? (y/n): ").lower()
                if again not in ['y', 'yes']:
                    break
            
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
    
    print("\nStay secure! 🛡️")

if __name__ == "__main__":
    main()
