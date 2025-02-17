'''
Name: Amir Khoshour
Student ID: 100993995
Date: Feb 16, 2025
Lab1
'''
import random
import string


def get_user_input():

    while True:
        try:
            length = int(input("Enter total password length (min 8): "))
            if length < 8:
                raise ValueError("Password length must be at least 8 characters.")

            num_letters = int(input("Enter number of letters: "))
            num_digits = int(input("Enter number of digits: "))
            num_specials = int(input("Enter number of special characters: "))

            if num_letters + num_digits + num_specials != length:
                raise ValueError("Sum of letters, digits, and special characters must equal total length.")

            return length, num_letters, num_digits, num_specials
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def generate_password(length, num_letters, num_digits, num_specials):

    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)

    password_list = letters + digits + specials
    random.shuffle(password_list)

    return ''.join(password_list)


def main():

    print("\nSecure Password Generator")
    length, num_letters, num_digits, num_specials = get_user_input()
    password = generate_password(length, num_letters, num_digits, num_specials)
    print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
