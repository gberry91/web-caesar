def alphabet_position(letter):
    char_val = (ord(letter))
    if char_val > 64 and char_val < 97:
        new_char_val = char_val % 65
    elif char_val > 96:
        new_char_val = char_val % 97
    return (new_char_val)


def rotate_character(char, rot):
        if char.isupper():
            pos = alphabet_position(char) + rot
            if pos > 25:
                pos = pos % 26
            pos = pos + 65
            return chr(pos)
        elif char.islower():
            pos = alphabet_position(char) + rot
            if pos > 25:
                pos = pos % 26
            pos = pos + 97
            return chr(pos)

def encrypt(text, rot):
    accu = ""
    for i in text:
        if i.isalpha():
            new_val = rotate_character(i, rot)
            accu += new_val
        else:
            accu += i
    return (accu)
