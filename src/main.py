import hashlib
import random

braille_map = {
    '0': '010110', '1': '100001', '2': '110000', '3': '101000', 
    '4': '101100', '5': '100100', '6': '111000', '7': '111100', 
    '8': '110100', '9': '011000', 'a': '100000', 'b': '120000', 
    'c': '100400', 'd': '100450', 'e': '100050', 'f': '120400', 
    'g': '120450', 'h': '120050', 'i': '020400', 'j': '020450', 
    'k': '103000', 'l': '113000', 'm': '103400', 'n': '103450', 
    'o': '103050', 'p': '123400', 'q': '123450', 'r': '123050', 
    's': '023400', 't': '023450', 'u': '103006', 'v': '123006', 
    'w': '020456', 'x': '103406', 'y': '103456', 'z': '103056'
}

def generate_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def transform_to_braille(hash_string):
    braille_string = ''.join(braille_map[char] for char in hash_string)
    return braille_string

def replace_zeros(braille_string):
    return ''.join(char if char != '0' else str(random.choice([7, 8, 9])) for char in braille_string)

def transform_password(password):
    hash_string = generate_hash(password)
    braille_string = transform_to_braille(hash_string)
    secure_string = replace_zeros(braille_string)
    return secure_string
