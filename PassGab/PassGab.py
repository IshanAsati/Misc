
import string

symbols = string.punctuation
capitals = string.ascii_uppercase
smalls = string.ascii_lowercase
numerals = string.digits
def passGab(password):

    global score
    score = 0
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