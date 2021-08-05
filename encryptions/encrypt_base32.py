import base64
import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while 1:
    password_length = int(input("How long should your password be: "))
    password = ""
    for x in range(0, password_length):
        password_chars = random.choice(characters)
        password = password + password_chars
    print("Here is your password: " + password)
    break

def encrypt_base32():
    data_string_32 = password
    data_bytes_32 = data_string_32.encode("utf-8")
    encoded_data_32 = base64.b32encode(data_bytes_32)

    print("Base32 Encoded: ", encoded_data_32)

encrypt_base32()