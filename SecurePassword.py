import random

symbols = "!@#$%^&*()"
numbers = "1234567890"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()

password_generator =  symbols + numbers + uppercase_letters + lowercase_letters

while True:
    user_length = int(input("Enter desired length for password: "))
    if user_length > len(password_generator):
        print("Length exceeds available characters. Please enter a smaller length.")
    elif user_length < 10:
        print("For a secure password the recommended length should be more than 9 characters.") 
    else:
        userPassword = "".join(random.sample(password_generator, user_length))
        break

print(userPassword)