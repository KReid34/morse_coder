import sys

morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
              'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
              'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
              'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
              }


def get_input():
    print('Welcome to the Morse Coder')
    user_input = input("Type a word you wish to encode or type 'q' to quit: ").lower()
    if user_input == 'q':
        sys.exit()

    else:
        encode_input(user_input)


def encode_input(user_input):
    print(f"You wish to encode: {user_input}")
    try:
        encoded_word = [morse_code[letter] for letter in user_input]
        print(' '.join(encoded_word))
    except KeyError:
        print("Sorry, I can only encode one word at a time and I don't understand numbers just yet.")
        get_input()
    else:
        get_input()


keep_coding = True
while keep_coding:
    get_input()
