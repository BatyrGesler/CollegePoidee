try:
    user_note = input("Note: ")
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(user_note + "\n")

    with open("notes.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        print("Lines in file:", len(lines))
except Exception:
    print("Error.")