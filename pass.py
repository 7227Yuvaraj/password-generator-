import random
import string
import json 

def generate_password(length, min_chars, min_digits, min_symbols):
    """
    Generates a random password with specified length and character composition.

    Args:
        length: Total length of the password.
        min_chars: Minimum number of characters.
        min_digits: Minimum number of digits.
        min_symbols: Minimum number of symbols.

    Returns:
        The generated password as a string.
    """

    if min_chars + min_digits + min_symbols > length:
        raise ValueError("Sum of minimum character counts exceeds password length.")

    characters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = characters + digits + symbols

    password = []
    password.extend(random.choice(characters) for _ in range(min_chars))
    password.extend(random.choice(digits) for _ in range(min_digits))
    password.extend(random.choice(symbols) for _ in range(min_symbols))

    # Fill the remaining password with random characters
    for _ in range(length - min_chars - min_digits - min_symbols):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

# Get user input
length = int(input("Enter the length of the password: "))
min_chars = int(input("Enter the minimum number of characters: "))
min_digits = int(input("Enter the minimum number of digits: "))
min_symbols = int(input("Enter the minimum number of symbols: "))




def save_password(password, filename="passwords.json"):
    """Saves the generated password to a JSON file."""
    try:
        with open(filename, 'r') as f:
            passwords = json.load(f)
    except FileNotFoundError:
        passwords = []

    passwords.append(password)

    with open(filename, 'w') as f:
        json.dump(passwords, f, indent=4)


# Generate and print the password
password = generate_password(length, min_chars, min_digits, min_symbols)
print("Generated Password:", password)
save_password(password)