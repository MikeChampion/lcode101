import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ''
    for letter in text:
        let = rotate_character(letter, rot)
        encrypted += let
    return encrypted

def main():
    text = input("What message would you like encrypted? ")
    rot = input("How many spaces would you like to shift for encryption? ")
    rot = int(rot)
    print(encrypt(text, rot))
    #print(rotate_character('a', 13))
    #print(alphabet_position('t'))

if __name__ == "__main__":
    main()
