from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_message(message, key):
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return iv, encrypted_message

def decrypt_message(encrypted_message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), AES.block_size).decode()
    return decrypted_message

def main():
    print("*" * 70)
    print("Welcome to Encryptor and Decryptor")
    print("*" * 70)

    print("1. Encryption")
    print("2. Decryption")
    print("")

    op = int(input("Enter your choice (1 or 2): "))

    if op == 1:
        message = input("Enter the message to encrypt: ")
        key = os.urandom(32)
        iv, encrypted_message = encrypt_message(message, key)
        print("\nEncrypted Message (hex):", encrypted_message.hex())
        print("Key (hex):", key.hex())
        print("IV (hex):", iv.hex())
    elif op == 2:
        encrypted_message = bytes.fromhex(input("Enter the encrypted message (hex): "))
        key = bytes.fromhex(input("Enter the key (hex): "))
        iv = bytes.fromhex(input("Enter the IV (hex): "))
        try:
            decrypted_message = decrypt_message(encrypted_message, key, iv)
            print("\nDecrypted Message:", decrypted_message)
        except Exception as e:
            print("Decryption failed:", e)
    else:
        print("!!! Invalid option")

main()
