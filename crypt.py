import random
import base64

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while 1:
    password_length = int(input("How long should your password be: "))
    password = ""
    for x in range(0, password_length):
        password_chars = random.choice(characters)
        password = password + password_chars
    print("Here is your password: " + password)
    break

encrypt_me = input("Would you like to encrypt your password (yes/no): ")

def encrypt_base64():
    data_string = password
    data_bytes = data_string.encode("utf-8")
    encoded_data = base64.b64encode(data_bytes)

    print("Encoded: ", encoded_data)

def encrypt_reverse():
    endPoint = ''
    i = len(password) - 1
    
    while i >= 0:
        endPoint = endPoint + password[i]
        i = i - 1
    print("Reversed Cipher: " + endPoint)

if encrypt_me == "yes":
    print("[1] => Base64\n"
          "[2] => Caesar Cipher (In Development)\n"
          "[3] => ROT13 (In Development)\n"
          "[4] => Reversed Cipher\n")
    options = input("Please choose which encryption method you would like to use: ")

    if options == "1":
        encrypt_base64()
    elif options == "2":
        print("Coming soon!")
        # encrypt_caesar()
    elif options == "3":
        print("Coming soon!")
        # encrypt_rot13()
    elif options == "4":
        encrypt_reverse()
    else:
        print("We don't currently support that type of encryption!")

elif encrypt_me == "no":
    print("Have a good day!")
    print("Don't forget your password: " + password)
else:
    print("Please choose yes or no")