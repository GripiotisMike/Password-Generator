import random

# Character pools for the password
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

def generate_password(nr_letters, nr_symbols, nr_numbers):
    """Generate a randomized password based on user input."""
    password_chars = []

    # Add the specified number of letters, numbers, and symbols to the password
    password_chars += random.choices(letters, k=nr_letters)
    password_chars += random.choices(numbers, k=nr_numbers)
    password_chars += random.choices(symbols, k=nr_symbols)

    # Shuffle the characters for randomness
    random.shuffle(password_chars)

    # Convert the list of characters to a single string
    return ''.join(password_chars)

def main():
    print("Welcome to the PyPassword Generator!")
    
    # Get user input for password composition
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        return
    
    # Generate the password
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"Your generated password is:\n{password}")

if __name__ == "__main__":
    main()
