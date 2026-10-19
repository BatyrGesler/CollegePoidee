import re

usernames = ["aidana_01", "1abc", "ab", "very_long_username_123", "yerlan-k"]
phones = ["+7 701 123-45-67", "8(701)1234567", "+77011234567",
          "7701123456", "+8 701 123 45 67"]

def is_valid_username(username):
    if re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_]{2,19}", username):
        return True
    return False

def clean_phone(phone):
    return re.sub(r"\D", "", phone)


def is_valid_phone(phone):
    if not (phone.startswith("+7") or phone.startswith("7") or phone.startswith("8")):
        return False
    digits = clean_phone(phone)

    if re.fullmatch(r"[78]7\d{9}", digits):
        return True
    return False


for u in usernames:
    print(u, ":", is_valid_username(u))

print("----------------------------\n")
for p in phones:
    print(p, clean_phone(p), ":", is_valid_phone(p))