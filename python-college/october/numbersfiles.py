import os

n = int(input("How many nums? "))
with open("numbers.txt", "w", encoding="utf-8") as f:
    for i in range(n):
        line = input("Enter a number: ")
        f.write(line + "\n")

count = 0
total_sum = 0.0
max_val = 0

with open("numbers.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line != "":
            num = float(line)
            count += 1
            total_sum += num
            if count == 1 or num > max_val:
                max_val = num

print(f"Count: {count}, Sum: {total_sum}, Max: {max_val}")

os.remove("numbers.txt")