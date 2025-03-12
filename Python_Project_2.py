# Python Project 2 :- 

# Dictionary mapping characters to keypress sequences
keypad = {
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    ' ': '0'
}

# Function to convert text to keypress sequence
def text_to_keypress(text):
    text = text.upper()  # Convert to uppercase for uniform mapping
    keypress_sequence = ""

    for char in text:
        if char in keypad:
            keypress_sequence += keypad[char]

    return keypress_sequence

# Example usage
user_input = input("Enter a message: ")
output = text_to_keypress(user_input)
print("Keypress sequence:", output)