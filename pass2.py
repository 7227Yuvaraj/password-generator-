import random
import string
import json

class PasswordGenerator:
    def __init__(self):
        self.length = 0
        self.min_chars = 0
        self.min_digits = 0
        self.min_symbols = 0

    def get_user_input(self):
        while True:
            try:
                self.length = int(input("Enter the length of the password: "))
                self.min_chars = int(input("Enter the minimum number of characters: "))
                self.min_digits = int(input("Enter the minimum number of digits: "))
                self.min_symbols = int(input("Enter the minimum number of symbols: "))
                if self.min_chars + self.min_digits + self.min_symbols > self.length:
                    print("Error: Sum of minimum character counts exceeds password length.")
                else:
                    break
            except ValueError:
                print("Error: Invalid input. Please enter a valid integer.")

    def generate_password(self):
        characters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        all_chars = characters + digits + symbols

        password = []
        password.extend(random.choice(characters) for _ in range(self.min_chars))
        password.extend(random.choice(digits) for _ in range(self.min_digits))
        password.extend(random.choice(symbols) for _ in range(self.min_symbols))

        for _ in range(self.length - self.min_chars - self.min_digits - self.min_symbols):
            password.append(random.choice(all_chars))

        random.shuffle(password)
        return ''.join(password)

    def save_password(self, password, filename="passwords.json"):
        try:
            with open(filename, 'r') as f:
                passwords = json.load(f)
        except FileNotFoundError:
            passwords = []

        passwords.append(password)

        with open(filename, 'w') as f:
            json.dump(passwords, f, indent=4)

def main():
    generator = PasswordGenerator()
    generator.get_user_input()
    password = generator.generate_password()
    print("Generated Password:", password)
    generator.save_password(password)

if __name__ == "__main__":
    main()