# Cryptography with Polyalphabetic Ciphers - 4179

**Language**: `Python`

**Lines of code**: `37`

## Description

This program is written in Python and implements a polyalphabetic cipher to encrypt and decrypt messages. A polyalphabetic cipher uses multiple substitution alphabets to encrypt the plaintext, making it harder for an attacker to crack the encryption. The program prompts the user for a message to encrypt, a keyword to use as the encryption key, and a mode (either "encrypt" or "decrypt"). The program then uses the Vigenere cipher to perform the encryption or decryption and returns the result.

The program uses a function called vigenere_cipher to implement the Vigenere cipher algorithm. The function takes in three arguments: the message to encrypt or decrypt, the keyword to use as the encryption key, and the mode (either "encrypt" or "decrypt"). The function then iterates through each character in the message and encrypts or decrypts it based on the corresponding character in the key. The resulting ciphertext or plaintext is then returned.

The main function prompts the user for a message, keyword, and mode, and then calls the vigenere_cipher function to perform the encryption or decryption. The result is printed to the console.

## Code

``` Python
# Vigenere Cipher Implementation
def vigenere_cipher(message, key, mode):
    """Encrypts or decrypts a message using the Vigenere cipher."""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    message = message.upper()
    key_index = 0
    cipher_text = ""
    for char in message:
        if char in alpha:
            key_char = key[key_index % len(key)]
            if mode == "encrypt":
                cipher_text += alpha[(alpha.index(char) + alpha.index(key_char)) % 26]
            elif mode == "decrypt":
                cipher_text += alpha[(alpha.index(char) - alpha.index(key_char)) % 26]
            key_index += 1
        else:
            cipher_text += char
    return cipher_text

# User Interface
def main():
    """Prompts the user for a message, keyword, and mode (encrypt or decrypt)."""
    message = input("Enter message: ")
    keyword = input("Enter keyword: ")
    mode = input("Encrypt or decrypt? ")
    if mode.lower() == "encrypt":
        cipher_text = vigenere_cipher(message, keyword, "encrypt")
        print("Encrypted message: ", cipher_text)
    elif mode.lower() == "decrypt":
        plain_text = vigenere_cipher(message, keyword, "decrypt")
        print("Decrypted message: ", plain_text)
    else:
        print("Invalid mode entered. Please enter either 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()

```

## Prompt

```

Make me a program in any language that is more than 20 lines of code long and is complex and interesting.

When you create the program make a title for it and a short description of what it does.

Also tell me what language it is

```