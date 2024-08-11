import random
import string

generated_passwords = set()

def generate_password(length, strength):
    global generated_passwords
    
    if strength == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif strength == 'normal':
        characters = string.ascii_lowercase + string.digits
    elif strength == 'weak':
        characters = string.ascii_lowercase
    else:
        raise ValueError("Strength must be either 'strong', 'normal' or 'weak'")
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if password not in generated_passwords:
            generated_passwords.add(password)
            return password

password_length = int(input("Enter the desired length of the password: "))
password_strength = input("Enter the desired strength of the password (strong/normal/weak): ").strip().lower()

new_password = generate_password(password_length, password_strength)
print(f"Generated {password_strength} password: {new_password}")
