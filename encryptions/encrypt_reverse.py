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

def encrypt_reverse():
    endPoint = ''
    i = len(password) - 1
    
    while i >= 0:
        endPoint = endPoint + password[i]
        i = i - 1
    print("Reversed Cipher: " + endPoint)

encrypt_reverse()