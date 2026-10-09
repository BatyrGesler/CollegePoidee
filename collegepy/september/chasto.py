text = input("Введите текст: ").lower()
max_char = ""
max_count = 0
chek = ''
for i in range(len(text)):
    char = text[i]
    if char in " !@#$%^&*_-+=/" or char in chek:
        continue
    count = 0
    for c in text:
        if c == char:
            count += 1
    if count > max_count:
        max_count = count
        max_char = char

print(f'Самая частая буква: "{max_char}", встречается {max_count} раза')