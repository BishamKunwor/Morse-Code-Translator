# Coding Challenge 2
# Name:
# Student No:

# A Morse code encoder/decoder

MORSE_CODE = (
    (".-", "A"), ("-...", "B"), ("-.-.", "C"), ("-..",
                                                "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-",
                                                "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.",
                                                 "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--",
                                                 "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---",
                                     "2"), ("...--", "3"), ("....-", "4"), (".....", "5"),
    ("-....", "6"), ("--...", "7"), ("---..",
                                     "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.",
                                      ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-",
                                       "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

letters_relative_position = tuple(char[1] for char in MORSE_CODE)
code_relative_position = tuple(char[0] for char in MORSE_CODE)
file = None



def print_intro():
    print("Welcome to Wolmorse\nThis program encodes and decodes Morse code.")




def get_input():
    while True:
        choice = input("Would you like to encode (e) or decode (d): ")

        if choice:
            choice = choice[0].lower()
            if choice in ("e", "d"):
                return choice

            else:
                print("Invalid Mode")
                continue





def encode(message):
    words = message.split()
    encoded_message = []

    for word in words:
        for letter in word:
            index = letters_relative_position.index(letter.upper())
            encoded_message.append(MORSE_CODE[index][0])
            encoded_message.append('')
        encoded_message.append("   ")

    return " ".join(encoded_message)





def decode(message):

    words = message.split('   ')

    words = [word for word in words if word]
    decoded_message = []

    for word in words:
        character = word.split()
        letters_list = []

        for letter in character:
            index = code_relative_position.index(letter)
            letters_list.append(MORSE_CODE[index][1])

        decoded_message.append("".join(letters_list))

    return " ".join(decoded_message)




def process_lines(filename, mode):
    mode = mode[0].lower()

    if check_file_exists(filename) and (mode in ("e","d")):
        encoded_decoded_data = []
        data = file.read().split("\n")
        file.close()

        for sentences in data:
            if mode == 'e':
                encoded_decoded_data.append(encode(sentences))
            else: 
                encoded_decoded_data.append(decode(sentences))

        return encoded_decoded_data



def write_lines(lines):
    with open('results.txt','a') as result:
        for sentences in lines:
            result.write(f"{str(sentences)}\n")



def check_file_exists(filename):
    try:
        global file
        file = open(filename)
        return True
       
    except (FileNotFoundError):
        return False



def get_filename_input():
    choice = get_input()
    file_console_choice = input('Would you like to read from a file (f) or the console(c)? ')

    while True:
        if file_console_choice:
     
            if file_console_choice[0].lower() == 'f':
                file_name = input("Enter a filename: ")
                if check_file_exists(file_name):
                    return (choice, None, file_name)
                else:
                    print("Invalid Filename")
                    continue
            else:
                if choice == "e":
                    encode_decode_sentence = input("What message would you like to encode: \n")
                else:
                    encode_decode_sentence = input("What message would you like to decode: \n")
                return (choice, encode_decode_sentence, None)
        else:
            if choice == "e":
                encode_decode_sentence = input("What message would you like to encode: \n")
            else:
                encode_decode_sentence = input("What message would you like to decode: \n")
            return (choice, encode_decode_sentence, None)



def main():
    print_intro()
    
    while True:
        data = get_filename_input()
        if data[0] == 'e':
            if data[1]:
                print(encode(data[1]))
            else:
                write_lines(process_lines(data[2], data[0]))
                print('Output written to results.txt')
        else:
            if data[1]:
                print(decode(data[1]))
            else:
                write_lines(process_lines(data[2], data[0]))
                print('Output written to results.txt')
        repeat_loop = input('Would you like to encode/decode another message? (y/n): ')
        if repeat_loop:
            if repeat_loop[0].lower() == "y":
                continue
            break



if __name__ == '__main__':
    main()
