import os


with open("names.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        name = input("Enter name: ")
        f.write(name + "\n")

with open("names.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip().upper())


os.remove("names.txt")