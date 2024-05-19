import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4")
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    all_chars = lowercase + uppercase + digits + special_chars
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    password += random.choices(all_chars, k=length - 4)
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))
    
    try:
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
