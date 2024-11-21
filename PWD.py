import random
import string

def password_generator(size):
    if size < 8 or size > 16:
        return "Password must be between 8 to 16 characters"
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [ random.choice(lower), random.choice(upper), random.choice(digits), random.choice(special) ]

    all_characters = lower + upper + digits + special 
    password += random.choices(all_characters, k = size-4)

    random.shuffle(password)

    return ''.join(password)

size = int(input("Enter the length of the password you want which should be between 8 and 16: "))
password = password_generator(size)
print(f"Your password is {password}")