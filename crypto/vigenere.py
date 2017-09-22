import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    encrypted = ''
    key_count = 0
    for letter in text:
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        if letter in lower:
            y = key_count % len(key)
            z = key[y]
            r = alphabet_position(z)
            let = rotate_character(letter, r)
            key_count += 1
            encrypted += let
        elif letter in upper:
            y = key_count % len(key)
            z = key[y]
            r = alphabet_position(z)
            let = rotate_character(letter, r)
            key_count += 1
            encrypted += let
        else:
            let = letter
            encrypted += let
    return encrypted


def main():
    text = input("What message would you like encrypted? ")
    key = input("What is your key word? ")
    print(encrypt(text, key))
    
if __name__ == "__main__":
    main()
