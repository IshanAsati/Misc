import string

alphabet = string.ascii_lowercase

def enCRYtper(i):
    """
    get the user input then scramble it via rot13 
    """

    if i == " ":
        return " "
    if i not in alphabet:
        return i
    elif alphabet.index(i) > 12:
        letter = alphabet.index(i)
        letter +=13
        new_letter = letter - 26
        return alphabet[new_letter]
    else:
        letter = alphabet.index(i)
        letter += 13
        new_letter = letter
        return alphabet[new_letter]
        
for i in input("Enter Text: "):
    print(enCRYtper(i), end="")

