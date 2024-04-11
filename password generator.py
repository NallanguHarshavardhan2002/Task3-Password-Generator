import random
import string

def generate_password(pw_length):
    # Generate a password with a mix of letters, digits, and special characters
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for i in range(pw_length):
        # Randomly choose a character type: letter, digit, or special character
        character_type = random.choice([string.ascii_letters, string.digits, string.punctuation])
        # Randomly choose a character from the chosen character type
        password.append(random.choice(character_type))
    # Ensure at least one uppercase letter, one lowercase letter, and one digit
    while (not any(c.isupper() for c in password) or
           not any(c.islower() for c in password) or
           not any(c.isdigit() for c in password)):
        password[random.randrange(len(password))] = random.choice(password_characters)
    return ''.join(password)

def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(num_passwords) + " passwords")
    password_lengths = []
    for i in range(num_passwords):
        length = int(input("Enter the length of Password #" + str(i+1) + " "))
        if length < 3:
            print("Minimum length of password should be 3")
            length = 3
        password_lengths.append(length)
    passwords = [generate_password(length) for length in password_lengths]
    for i in range(num_passwords):
        print("Password #" + str(i+1) + " = " + passwords[i])

main()
