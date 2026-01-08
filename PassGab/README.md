# PassGab
Password Strength Checker

A simple Python-based password strength checker that evaluates passwords using common security criteria such as length and character variety. This project is an early-stage implementation and is intended for learning and experimentation.

Features

The password checker assigns a score out of 100 based on the following rules:

Contains at least one symbol (+20)

Contains at least one uppercase letter (+20)

Contains at least one lowercase letter (+20)

Contains at least one digit (+20)

Password length greater than 12 characters (+20)

The final score is printed to the console.

How It Works

The program:

Takes a password as input from the user.

Iterates through the password to check for required character types.

Adds points when each condition is satisfied.

Outputs the total score.

Code
import string

symbols = string.punctuation
capitals = string.ascii_uppercase
smalls = string.ascii_lowercase
numerals = string.digits

def passGab(password):
    global score
    score = 0
    password = list(password)

    for symbol in password:
        if symbol in symbols:
            score += 20
            break

    if len(password) > 12:
        score += 20

    for capital in password:
        if capital in capitals:
            score += 20
            break

    for small in password:
        if small in smalls:
            score += 20
            break

    for numeral in password:
        if numeral in numerals:
            score += 20
            break

    print(f"Your Password is {score}/100 lil vro")

if __name__ == '__main__':
    passGab(input("Enter your password: "))

Requirements

Python 3.x

No external libraries required (uses Python’s built-in string module)

Usage

Run the script from the terminal:

python password_checker.py


Then enter a password when prompted.

Limitations

Uses a checklist-based scoring system, which can be easily gamed

Does not check for:

Dictionary words

Repeated characters

Common patterns (e.g. 1234, aaaa)

Does not estimate entropy

Passwords are not hashed (not intended for real authentication systems)

Planned Improvements

Dictionary-based password detection

Penalties for repeated characters and patterns

Entropy-based scoring

More detailed feedback instead of a single score

Optional password hashing for realistic use cases

Disclaimer

This project is not intended for production use. It is a learning project designed to explore password strength concepts and basic Python programming.