def encrypt(text, rot):
    new_text = ''
    for i in text:
        new_text += rotate_character(i,rot)
    return new_text

def rotate_character(char, rot):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_char = ''
    cypher = rot
    if char not in lower and char not in upper:
        return char

    elif char in lower:
        new_char += lower[(lower.index(char) + cypher) % (len(lower))]
    elif char in upper:
        new_char += upper[(upper.index(char) + cypher) % (len(upper))]
    return new_char

def alphabet_position(letter):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter in lower:
        position = lower.index(letter)
    elif letter in upper:
        position = upper.index(letter)
    elif letter not in lower and letter not in upper:
        return letter
    return position
