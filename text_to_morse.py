import argparse

parser = argparse.ArgumentParser(description='Convert text to morse code')

parser.add_argument('Mode', metavar='mode', type=str, choices=['text_to_morse', 'morse_to_text'], help='Mode to convert to (text or morse)')
parser.add_argument('Input', metavar='input', type=str, help='Input to convert')

args = parser.parse_args()

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
}

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

def text_to_morse(text):
    input_text = text.upper()
    output_text = ''
    for char in input_text:
        if char in morse_code_dict:
            output_text += morse_code_dict[char] + ' '
        elif char == ' ':
            output_text += '/'
        else:
            output_text += char
    return output_text

def morse_to_text(morse):
    words = morse.split('/')
    output_text = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in reverse_morse_code_dict:
                output_text += reverse_morse_code_dict[letter]
        output_text += ' '  # Add a space at the end of each word
    return output_text.strip()  # Remove trailing space

# Perform the conversion based on the mode
if args.Mode.lower() == 'text_to_morse':
    print(f"Your text: '{args.Input}' converted to morse code is:- \n \n {text_to_morse(args.Input)}")
elif args.Mode.lower() == 'morse_to_text':
    print(f"Your morse code: '{args.Input}' converted to text is:- \n \n {morse_to_text(args.Input)}")
else:
    print(f'Unknown mode: {args.Mode}')

