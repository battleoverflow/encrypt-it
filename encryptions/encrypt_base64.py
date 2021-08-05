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

def encrypt_base64():
    data_string = password
    data_bytes = data_string.encode("utf-8")
    encoded_data = base64.b64encode(data_bytes)

    print("Here is your encoded password: ", encoded_data)

encrypt_base64()