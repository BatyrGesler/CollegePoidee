text = input("Write text: ")
g = 0
def count_words(text):
    text = text.split(" ")
    return len(text)

def count_vowels(text, g):
    for letter in text:
        if letter in "aeioyuAEYIOU":
            g += 1
        else:
            continue
    return g
def longest(text):
    text = text.split(" ")
    longest = ""
    for word in text:
        if len(word) > len(longest):
            longest = word
    return longest

def print_report(text):
    return f"words - {count_words(text)} vowels - {count_vowels(text, g)} longest word - {longest(text)}"

print(print_report(text))
