from cipher_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

convert = 0
check = "encode"
permission = "no"
print(logo)
permission = input("Do you want to start type yes or type no").lower()

def encrypt(writing, convert):
    encrypted_word = ""
    for n in range(len(writing)):
        if writing[n] in alphabet:
            position = alphabet.index(writing[n])
            new_position = position + convert
            new_letter = alphabet[new_position]
            encrypted_word += new_letter
        else:
            encrypted_word  += writing[n]


    print(f"The encoded text is {encrypted_word}")

def decrypt(writing, convert):
    encrypted_word = ""
    for n in range(len(writing)):
        if writing[n] in alphabet:
            position = alphabet.index(writing[n])
            new_position = position - convert
            new_letter = alphabet[new_position]
            encrypted_word += new_letter
        else:
            encrypted_word += writing[n]

    print(f"The encoded text is {encrypted_word}")

while(permission == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    permission = input("Do you want to start type yes or type no").lower()



