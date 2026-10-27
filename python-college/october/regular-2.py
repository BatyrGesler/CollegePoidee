import re

log = [
    "2026-10-14 09:15:02 INFO User aidana logged in from 192.168.1.10",
    "2026-10-14 09:17:45 ERROR Database timeout after 30s",
    "2026-10-14 09:20:11 WARNING Disk usage 91%",
    "2026-10-14 09:25:33 ERROR Failed login for user yerlan from 10.0.0.5",
    "2026-10-14 09:30:00 INFO User dana logged out",
]

pattern = r"(?P<date>\S+) (?P<time>\S+) (?P<level>[A-Z]+) (?P<message>.+)"
ip_pattern = r"\d+\.\d+\.\d+\.\d+"

levels = {}
errors = []
ips = []

for line in log:
    m = re.match(pattern, line)
    level = m.group("level")
    message = m.group("message")

    levels[level] = levels.get(level, 0) + 1

    if level == "ERROR":
        errors.append(message)
    ips += re.findall(ip_pattern, message)



print(f"lvls - {levels}")
print("--------------------------")
print(f"ERRORS - {errors}")
print("------------------------------")
print(f"IPS - {ips}")
