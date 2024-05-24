#Ananya Pandey
#Byte Uprise
''' Implentation of password complexity checker using python programming,
I have used RE of Regular Expression Library which enables search operation in Words or Sentences.
'''
import re

def check_password_strength(password):
    # Define criteria 
    # Length of password should be more than 8 characters
    # Must include digits, uppercase characters, lowercase characters, and special characters
    
    is_length_error = len(password) < 8
    is_digit_error = re.search(r"\d", password) is None
    is_uppercase_error = re.search(r"[A-Z]", password) is None
    is_lowercase_error = re.search(r"[a-z]", password) is None
    is_special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    # Evaluate criteria
    strength = 0
    errors = []
    if is_length_error:
        errors.append("Password should be at least 8 characters long.")
    else:
        strength += 1
    
    if is_digit_error:
        errors.append("Password should contain at least one digit.")
    else:
        strength += 1
    
    if is_uppercase_error:
        errors.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1
    
    if is_lowercase_error:
        errors.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1
    
    if is_special_char_error:
        errors.append("Password should contain at least one special character.")
    else:
        strength += 1
    
    return strength, errors

def main():
    password = input("Enter your password: ")
    strength, errors = check_password_strength(password)
    if strength == 5:
        print("Password is strong!")
    else:
        print("Password is weak:")
        for error in errors:
            print("- ", error)

if __name__ == "__main__":
    main()
