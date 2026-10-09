c = list(map(int, input().split()))

f = list(map(lambda x: x * 9 / 5 + 32, c))

print(f"celsium: {c}, farenheit: {f}")


dop = list(map(lambda cel, far: f"{cel}°C = {far}°F", c, f))

print(dop)
