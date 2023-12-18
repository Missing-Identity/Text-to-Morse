# Morse Code Converter

This is a simple command-line program that can convert text to Morse code and Morse code to text. This Project was an idea given my Angela Yu in her Udemy course: 100 Days of Code - The Complete Python Pro Bootcamp for 2021. I have added some additional functionality to the program, such as the ability to convert Morse code to text. This is a simple program that I created to practice using Python dictionaries.

## Usage

To use this program, you need to provide two command-line arguments:

1. The conversion mode: This can be either `text_to_morse` or `morse_to_text`.
2. The input to be converted: This can be any string of text or Morse code.

Here are some examples of how to use this program:

```bash
python3 text_to_morse.py text_to_morse "Hello, World!"
python3 text_to_morse.py morse_to_text ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.."
```

In the Morse code output, each letter is separated by a space and each word is separated by a slash (/).

## Morse Code Dictionary

This program uses the following Morse code dictionary:

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
...
}
