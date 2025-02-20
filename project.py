import random

def generate_random_password(length=12):
    
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    
    all_characters = lowercase + uppercase + digits
    password = random.choices(all_characters, k=length)
    random.shuffle(password)
    final_password = ''.join(password)  
    return final_password


password_length = 8
password = generate_random_password(password_length)
print("Generated Password:", password)

