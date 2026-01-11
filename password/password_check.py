import re

def check_password_strength(password):
    if len(password) < 8:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%]", password):
        return False

    return True


if __name__ == "__main__":
    pwd = input("Enter your password: ")

    if check_password_strength(pwd):
        print("Strong password")
    else:
        print("Weak password")
        print("Password must have:")
        print("- At least 8 characters")
        print("- Uppercase and lowercase")
        print("- One number")
        print("- One special character (!@#$%)")

