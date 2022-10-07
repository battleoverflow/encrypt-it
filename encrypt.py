import random, base64, rsa
from cryptography.fernet import Fernet
import jwt as j

###############################################################
#   ______                             _     _____ _          # 
#  |  ____|                           | |   |_   _| |         #
#  | |__   _ __   ___ _ __ _   _ _ __ | |_    | | | |_        # 
#  |  __| | '_ \ / __| '__| | | | '_ \| __|   | | | __|       #
#  | |____| | | | (__| |  | |_| | |_) | |_   _| |_| |_        #
#  |______|_| |_|\___|_|   \__, | .__/ \__| |_____|\__|       #
#                           __/ | |                           #
#                          |___/|_|                           #
###############################################################

VERSION = "1.1.9"

print(f'''
  ______                             _     _____ _   
 |  ____|                           | |   |_   _| |  
 | |__   _ __   ___ _ __ _   _ _ __ | |_    | | | |_ 
 |  __| | '_ \ / __| '__| | | | '_ \| __|   | | | __|
 | |____| | | | (__| |  | |_| | |_) | |_   _| |_| |_ 
 |______|_| |_|\___|_|   \__, | .__/ \__| |_____|\__|
                          __/ | |                    
                         |___/|_|
                        
                        {VERSION}
''')

print("Open Source: https://github.com/Hifumi1337/encrypt-it\n"
      "Creator: Hifumi1337 (https://github.com/Hifumi1337)\n")

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
encrypt_me = input("\nWould you like to encrypt/encode your password (y/n): ")

# Asks user if they would like to save password & encryption in a file (.txt)
file_push = input("\nWould you like your password saved in a file (y/n): ")

class Encrypt:

    def __init__(self):
        self.password = password

    # Base64 encode
    def encode_base64(self):
        base64_string = password
        base64_bytes = base64_string.encode("utf-8")
        base64_encoded_pass = base64.b64encode(base64_bytes)
        
        print("\nBase 64 Encoded: ", base64_encoded_pass)

        if file_push == "y":
            with open("base64.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write("Encoded Password: " + str(base64_encoded_pass))

            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    # Reverse cipher
    def reverse_cipher(self):
        reverse_me = self.password[::-1]
        
        print(f"\nReversed Cipher: {reverse_me}")

        if file_push == "y":
            with open("reverse.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write(f"Reversed Password: {reverse_me}")

            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    # Base32 encryption
    def encode_base32(self):
        base32_string = self.password
        base32_bytes = base32_string.encode("utf-8")
        base32_encoded_pass = base64.b32encode(base32_bytes)

        print("\nBase32 Encoded: ", base32_encoded_pass)

        if file_push == "y":
            with open("base32.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write("Encoded Password: {0}".format(str(base32_encoded_pass)))

            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    # Fernet encryption
    def encrypt_fernet(self):
        # Encrypt the password
        fernet_pass = self.password

        # Generates key
        fernet_key = Fernet.generate_key()
        fernet = Fernet(fernet_key)
        encrypted_fernet_pass = fernet.encrypt(fernet_pass.encode())

        print("\nEncrypted Password: ", encrypted_fernet_pass)
        print("\nDO NOT SHARE THIS!")
        print("Encryption Key: ", fernet_key)

        if file_push == "y":
            with open("fernet.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write("Encrypted Password: " + str(encrypted_fernet_pass) + "\n")
                f.write("Encryption Key: " + str(fernet_key) + "\n")
           
            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    # RSA encryption
    def encrypt_rsa(self):
        # key_size = int(input("Please choose a key size for your RSA encryption: "))
        public_rsa_key, private_rsa_key = rsa.newkeys(1024)
        rsa_pass = self.password
        encrypted_rsa_pass = rsa.encrypt(rsa_pass.encode(), public_rsa_key)
        
        print("Encrypted Password (Public Key | 1024): ", encrypted_rsa_pass)
        print("Encryption Key (Private Key | 1024): ", private_rsa_key)

        # Used for testing RSA decryption
        # decrypted_rsa_pass = rsa.decrypt(encrypted_rsa_pass, private_rsa_key).decode()
        # print("Decrypted Password: ", decrypted_rsa_pass)
        
        if file_push == "y":
            with open("rsa_keys.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write("Encrypted Password (Public Key | 1024): {0}".format(str(encrypted_rsa_pass) + "\n"))
                f.write("Encryption Key (Private Key | 1024): {0}".format(str(private_rsa_key) + "\n"))
                
            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    # Caesar cipher
    def caesar_cipher(self):
        shift = int(input("Please enter your shift number: "))
        iterate_pass = self.password
        caesar_cipher = ""
        
        for cipher in iterate_pass:
            if cipher.isupper():
                begin_shift = ord(cipher) - ord('A')
                caesar_shift = (begin_shift + shift) % 26 + ord('A')
                new_caesar = chr(caesar_shift)
                caesar_cipher += new_caesar
            
            elif cipher.islower():
                begin_shift = ord(cipher) - ord('a') 
                caesar_shift = (begin_shift + shift) % 26 + ord('a')
                new_caesar = chr(caesar_shift)
                caesar_cipher += new_caesar
            
            else:
                caesar_cipher += cipher

        print(f"Cipher: {caesar_cipher}")
        print(f"Shift Used: {shift}")

        if file_push == "y":
            with open("caesar.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write(f"Caesar Cipher: {caesar_cipher}\n")
                f.write(f"Shift: {shift}")
 
            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")

    def jwt_token_encode(self):
        set_secret = input("Set JWT secret: ")

        encoded_msg = j.encode({
            'payload': password
        }, str(set_secret), algorithm='HS256')

        print(f"\nEncoded JWT Token: {encoded_msg}")

        if file_push == "y":
            with open("jwt.txt", "w") as f:
                f.write(f"Password: {self.password}\n")
                f.write("Encoded JWT Token: {0}".format(str(encoded_msg)))

            print("\nYour password was successfully saved!")
        elif file_push == "n":
            print("\nYour password was not saved.")


# Begin encryption options
if encrypt_me == "y":
    print("[1] => Base64 Encoding\n"
        "[2] => Reverse Cipher\n"
        "[3] => Base32 Encoding\n"
        "[4] => Fernet Encryption\n"
        "[5] => RSA Encryption\n"
        "[6] => Caesar Cipher\n"
        "[7] => JWT Token\n")

    E = Encrypt()
    
    options = input("Please choose which encryption method you would like to use: ")

    # Choose encryption method
    if options == "1":
        E.encode_base64()
    elif options == "2":
        E.reverse_cipher()
    elif options == "3":
        E.encode_base32()
    elif options == "4":
        E.encrypt_fernet()
    elif options == "5":
        E.encrypt_rsa()
    elif options == "6":
        E.caesar_cipher()
    elif options == "7":
        E.jwt_token_encode()
    else:
        print("We don't currently support that type of encryption!\n")

elif encrypt_me == "n":
    if file_push == "y":
        with open("password.txt", "w") as f:
            f.write(f"Password: {password}")

        print("Your password was successfully saved!")
    elif file_push == "n":
        print("Your password was not saved.")
    
    print("Have a good day!\n")
    print(f"Don't forget your password: {password}")
else:
    print("Please choose y or n")