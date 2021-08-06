import random
import base64

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def banner(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(banner(255, 0, 0, '''
  ______                             _     _____ _   
 |  ____|                           | |   |_   _| |  
 | |__   _ __   ___ _ __ _   _ _ __ | |_    | | | |_ 
 |  __| | '_ \ / __| '__| | | | '_ \| __|   | | | __|
 | |____| | | | (__| |  | |_| | |_) | |_   _| |_| |_ 
 |______|_| |_|\___|_|   \__, | .__/ \__| |_____|\__|
                          __/ | |                    
                         |___/|_|
'''))

print("Open Source: https://github.com/GhostlyPy/encrypt-it\n"
      "Creator: GhostlyPy (https://github.com/GhostlyPy)\n")

while True:
    password_length = int(input("How long should your password be: "))
    password = ""
    for x in range(0, password_length):
        password_chars = random.choice(a)
        password = password + password_chars
    print("Here is your password: " + password)
    break

encrypt_me = input("Would you like to encrypt your password (yes/no): ")

def encrypt_base64():
    data_string = password
    data_bytes = data_string.encode("utf-8")
    encoded_data = base64.b64encode(data_bytes)

    print("Base 64 Encoded: ", encoded_data)

def encrypt_reverse():
    endPoint = password[::-1]
    print("Reversed Cipher: " + endPoint)

def encrypt_base32():
    data_string_32 = password
    data_bytes_32 = data_string_32.encode("utf-8")
    encoded_data_32 = base64.b32encode(data_bytes_32)

    print("Base32 Encoded: ", encoded_data_32)

if encrypt_me == "yes":
    print("[1] => Base64\n"
          "[2] => Reversed Cipher\n"
          "[3] => Base32\n")
    options = input("Please choose which encryption method you would like to use: ")

    if options == "1":
        encrypt_base64()
    elif options == "2":
        encrypt_reverse()
    elif options == "3":
        encrypt_base32()
    else:
        print("We don't currently support that type of encryption!")

elif encrypt_me == "no":
    print("Have a good day!")
    print("Don't forget your password: " + password)
else:
    print("Please choose yes or no")