import random
import base64

#########################################################
# Project: https://github.com/GhostlyPy/encrypt-it      #
# Creator: GhostlyPy                                    #
# Version: 1.0.4                                        #
#########################################################

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
    # Loops through the provided characters to create a random pasword
    for x in range(0, password_length):
        password_chars = random.choice(a)
        password = password + password_chars
    # Prints randomly generated password
    print("Here is your password: " + password)
    break

# Encryption begins
encrypt_me = input("Would you like to encrypt your password (yes/no): ")

# Base64 encryption
def encrypt_base64():
    bs64_string = password
    bs64_bytes = bs64_string.encode("utf-8")
    bs64_encoded_passwd = base64.b64encode(bs64_bytes)
    
    print("Base 64 Encoded: ", bs64_encoded_passwd)

# Reverse cipher
def encrypt_reverse():
    endPoint = password[::-1]
    
    print("Reversed Cipher: " + endPoint)

# Base32 encryption
def encrypt_base32():
    bs32_string = password
    bs32_bytes = bs32_string.encode("utf-8")
    bs32_encoded_passwd = base64.b32encode(bs32_bytes)

    print("Base32 Encoded: ", bs32_encoded_passwd)

# Begin encryption options
if encrypt_me == "yes":
    print("[1] => Base64\n"
          "[2] => Reversed Cipher\n"
          "[3] => Base32\n")
    options = input("Please choose which encryption method you would like to use: ")

    # Choose encryption method
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