

import random
import string

chars=string.whitespace + string.punctuation + string.digits + string.ascii_letters

chars=list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars : {chars}")
print(f"key : {key}")

#encryption function
def encrypt(message):
    encrypted_message = ""
    for char in message:
        index = chars.index(char)
        encrypted_message += key[index]
    return encrypted_message

#decryption function
def decrypt(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        index = key.index(char)
        decrypted_message += chars[index]
    return decrypted_message

#test the functions
message = input("Enter a message to encrypt: ")
print(f"Original message: {message}")
print(f"Encrypted message: {encrypt(message)}")

encrypted_message=input("Enter a message to decrypt: ")
print(f"Decrypted message: {decrypt(encrypted_message)}")

