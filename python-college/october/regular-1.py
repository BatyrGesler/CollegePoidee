import re

usernames = ["aidana_01", "1abc", "ab", "very_long_username_123", "yerlan-k"]
phones = ["+7 701 123-45-67", "8(701)1234567", "+77011234567",
          "7701123456", "+8 701 123 45 67"]


def only_numbers(phone_number):
    result = []
    for phone in phone_number:
        result.append(re.sub(r"\D", "", phone))
    return result


check_log = []
for name in usernames:
    if re.fullmatch(r"\w{6,23}", name):
        check_log.append(name)



correct_phones = []
for phone in phones:
    correct_phones.append(re.sub(r"[ ()-]", "", phone))

kz_phones = []
for i in correct_phones:
    if re.findall(r"\+77\d{9}", i) or re.findall(r"^8\d{9}", i):
        kz_phones.append(i)

print(check_log)
print(kz_phones)
print(only_numbers(phones))