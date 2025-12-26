import random
import string

def generate_password(min_length, numbers=True, special_chars=True):
    characters = string.ascii_letters # Include both uppercase and lowercase letters

    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if min_length < 4:
        raise ValueError("Password length is incorrect")
    
    password = ''.join(random.choice(characters) for _ in range(min_length))
    return password



length = int(input("Enter the desired password length (minimum 4): "))
password = generate_password(length)


print("Generated Password:", password)