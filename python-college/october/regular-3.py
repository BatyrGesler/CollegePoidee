import re

text = "  Contact:  anna@mail.kz ,  john.doe@example.com.\nCall +7 701 123 45 67 or 8 (777) 555-12-34.   Deadline: 05.11.2026, report due 20.11.2026.  "

clean = re.sub(r"\s+", " ", text).strip()
clean = re.sub(r"\s+,", ",", clean)

emails = re.findall(r"[\w.]+@[\w.]+\.\w+", clean)

clean = re.sub(r"(\d{2})\.(\d{2})\.(\d{4})", r"\3-\2-\1", clean)

clean = re.sub(r"(?:\+7|8)[\s(]*\d{3}[\s)]*\d{3}[\s-]*\d{2}[\s-]*\d{2}", "***", clean)

print(clean)
print(emails)