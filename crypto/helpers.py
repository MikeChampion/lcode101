import string

def alphabet_position(letter):
    """Takes in a 1 character string and returns it's 0 based index point"""
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    if letter in lower: 
        char_ind = lower.index(letter)
    elif letter in upper:
        char_ind = upper.index(letter)
    return char_ind
    """test"""

def rotate_character(char, rot):
    """Takes a 1 character string and an integer for rotation returns a 1 character string of the new character position"""
    for l in char:
        lower = list(string.ascii_lowercase)
        upper = list(string.ascii_uppercase)
        if l in lower: 
            l = alphabet_position(l) 
            l = l + rot
            new_l = lower[(l % 26)]
        elif l in upper:
            l = alphabet_position(l)
            l = l + rot
            new_l = upper[(l % 26)]
        else:
            new_l = (l)
    return new_l