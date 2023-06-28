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
