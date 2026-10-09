password = input()
def hs_upper(password):
    if password != password.lower():
        return True
    else:
        return False

def has_digit(password):
    for char in password:
        if char in "1234567890":
            return True
    return False

def has_special(password):
    for char in password:
        if char in "!@#$%^&*()_":
            return True
    return False

def check_password(password):
    if has_digit(password) and has_special(password) and hs_upper(password):
        return "Molodec"
    else:
        return "Nope"

print(check_password(password))