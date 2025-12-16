import random

# characters list (manually written)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&"

# user input
length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated Password:", password)
