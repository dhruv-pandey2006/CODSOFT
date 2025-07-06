#Password Generator
import secrets
import string

def create_secure_password(pwd_len=8, require_strong=True):
    if pwd_len < 4:
        raise ValueError("Password must be at least 4 characters long.")
    
    charset = string.ascii_letters + string.digits + string.punctuation

    def is_strong(pwd):
        return (any(c.islower() for c in pwd) and
                any(c.isupper() for c in pwd) and
                any(c.isdigit() for c in pwd) and
                any(c in string.punctuation for c in pwd))

    password = ''
    attempts = 0
    while attempts < 1000:
        password = ''.join(secrets.choice(charset) for _ in range(pwd_len))
        if require_strong:
            if is_strong(password):
                break
        else:
            break
        attempts += 1

    return password

# Main execution block
if __name__ == "__main__":
    try:
        user_input = input("Choose password length (minimum 4): ")
        desired_length = int(user_input)
        final_password = create_secure_password(pwd_len=desired_length)
        print("\nYour new password:", final_password)
    except ValueError as err:
        print("Invalid input:", err)
