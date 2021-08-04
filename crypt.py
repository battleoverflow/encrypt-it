import random
import base64

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

while 1:
    password_length = int(input("How long should your password be: "))
    password = ""
    for x in range(0, password_length):
        password_chars = random.choice(characters)
        password = password + password_chars
    print("Here is your password: " + password)
    break

encrypt_me = input("Would you like to encrypt your password (yes/no): ")

if encrypt_me == "yes":
    print("Available Options: base64, caesar")
    options = input("Please choose which encryption method you would like to use: ")

    if options == "base64":
        data_string = password
        data_bytes = data_string.encode("utf-8")
        encoded_data = base64.b64encode(data_bytes)

        print("Encoded: ", encoded_data)
    elif options == "caesar":
        print("Coming soon!")
    else:
        print("We don't currently support that type of encryption!")

elif encrypt_me == "no":
    print("Have a good day!")
    print("Don't forget your password: " + password)

else:
    print("Please choose yes or no")
