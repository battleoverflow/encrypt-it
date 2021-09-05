import random
import base64
from cryptography.fernet import Fernet
import rsa
from __version__ import v3rsion

#########################################################
# Project: https://github.com/Hifumi-Sec/encrypt-it     #
# Creator: Hifumi Sec                                   #
# Version: 1.1.0                                        #
#########################################################

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

print("🔐 Simple password generator offering various encryption methods.\n")

print("Open Source: https://github.com/Hifumi-Sec/encrypt-it\n"
      "Creator: Hifumi Sec (https://github.com/Hifumi-Sec)")
print("Version: " + v3rsion + "\n")

# Characters used for the randomized password
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

while True:
    password_length = int(input("How many characters will your password be: "))
    password = ""
    # Loops through the provided characters to create a random pasword
    for x in range(0, password_length):
        password_chars = random.choice(a)
        password = password + password_chars
    # Prints randomly generated password
    print(f"\nHere is your password: {password}")
    break

# Encryption begins
encrypt_me = input("\nWould you like to encrypt your password (yes/no): ")

# Asks user if they would like to save password & encryption in a file (.txt)
file_push = input("\nWould you like your password saved in a file (yes/no): ")

# Base64 encryption
def encrypt_base64():
    bs64_string = password
    bs64_bytes = bs64_string.encode("utf-8")
    bs64_encoded_passwd = base64.b64encode(bs64_bytes)
    
    print("\nBase 64 Encoded: ", bs64_encoded_passwd)

    if file_push == "yes":
        f = open("base64.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encoded Password: " + str(bs64_encoded_passwd))
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# Reverse cipher
def encrypt_reverse():
    endPoint = password[::-1]
    
    print(f"\nReversed Cipher: {endPoint}")

    if file_push == "yes":
        f = open("reverse.txt", "w")
        f.write(f"Password: {password}\n")
        f.write(f"Reversed Password: {endPoint}")
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# Base32 encryption
def encrypt_base32():
    bs32_string = password
    bs32_bytes = bs32_string.encode("utf-8")
    bs32_encoded_passwd = base64.b32encode(bs32_bytes)

    print("\nBase32 Encoded: ", bs32_encoded_passwd)

    if file_push == "yes":
        f = open("base32.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encoded Password: " + str(bs32_encoded_passwd))
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# Fernet encryption
def encrypt_fernet():
    # Encrypt the password
    fernet_pass = password

    # Generates key
    fernetKey = Fernet.generate_key()
    fernet = Fernet(fernetKey)
    encryptedFernetPass = fernet.encrypt(fernet_pass.encode())

    print("\nEncrypted Password: ", encryptedFernetPass)
    print(banner(255, 0, 0, '\nDO NOT SHARE THIS!'))
    print("Encryption Key: ", fernetKey)

    if file_push == "yes":
        f = open("fernet.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encrypted Password: " + str(encryptedFernetPass) + "\n")
        f.write("Encryption Key: " + str(fernetKey) + "\n")
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# RSA encryption
def encrypt_rsa():
    # key_size = int(input("Please choose a key size for your RSA encryption: "))
    publicRSAKey, privateRSAKey = rsa.newkeys(1024)
    rsa_pass = password
    rsaEncryptedPass = rsa.encrypt(rsa_pass.encode(), publicRSAKey)
    
    print("Encrypted Password (Public Key | 1024): ", rsaEncryptedPass)
    print("Encryption Key (Private Key | 1024): ", privateRSAKey)

    # Used for testing RSA decryption
    # rsaDecryptedPass = rsa.decrypt(rsaEncryptedPass, privateRSAKey).decode()
    # print("Decrypted Password: ", rsaDecryptedPass)
    
    if file_push == "yes":
        f = open("rsa_keys.txt", "w")
        f.write(f"Password: {password}\n")
        f.write("Encrypted Password (Public Key | 1024): " + str(rsaEncryptedPass) + "\n")
        f.write("Encryption Key (Private Key | 1024): " + str(privateRSAKey) + "\n")
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# Caesar Cipher (this should not have been so difficult)
# Please ignore the terrible var names, my world ended the second I started this function
def encrypt_caesar():
    shift = int(input("Please enter your shift number: "))
    iteratePass = password
    caesar_cipher = ""
    for caesar_end in iteratePass:
        if caesar_end.isupper():
            begin_shift = ord(caesar_end) - ord('A')
            caesar_shift = (begin_shift + shift) % 26 + ord('A')
            new_caesar = chr(caesar_shift)
            caesar_cipher += new_caesar
        elif caesar_end.islower():
            begin_shift = ord(caesar_end) - ord('a') 
            caesar_shift = (begin_shift + shift) % 26 + ord('a')
            new_caesar = chr(caesar_shift)
            caesar_cipher += new_caesar
        else:
            caesar_cipher += caesar_end

    print(f"Cipher: {caesar_cipher}")
    print(f"Shift Used: {shift}")

    if file_push == "yes":
        f = open("caesar.txt", "w")
        f.write(f"Password: {password}\n")
        f.write(f"Caesar Cipher: {caesar_cipher}\n")
        f.write(f"Shift: {shift}")
        f.close()
        print("\nYour password was successfully saved!")
    elif file_push == "no":
        print("\nYour password was not saved.")

# Begin encryption options
if encrypt_me == "yes":
    print("[1] => Base64 Encoding\n"
          "[2] => Reversed Cipher\n"
          "[3] => Base32 Encoding\n"
          "[4] => Fernet Encryption\n"
          "[5] => RSA Encryption\n"
          "[6] => Caesar Cipher\n")
    options = input("Please choose which encryption method you would like to use: ")

    # Choose encryption method
    if options == "1":
        encrypt_base64()
    elif options == "2":
        encrypt_reverse()
    elif options == "3":
        encrypt_base32()
    elif options == "4":
        encrypt_fernet()
    elif options == "5":
        encrypt_rsa()
    elif options == "6":
        encrypt_caesar()
    else:
        print("We don't currently support that type of encryption!\n")

elif encrypt_me == "no":
    if file_push == "yes":
        f = open("password.txt", "w")
        f.write(f"Password: {password}")
        f.close()
        print("Your password was successfully saved!")
    elif file_push == "no":
        print("Your password was not saved.")
    print("Have a good day!\n")
    print(f"Don't forget your password: {password}")
else:
    print("Please choose yes or no")