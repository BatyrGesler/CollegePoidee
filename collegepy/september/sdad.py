# Cpiski
print("------------------------------------------Spiski")
a = []

# append
a.append('a')
print(a, "  - .append('a')")

# extend
a.extend(['b'])
print(a, "  - .extend(['b'])")

# insert
a.insert(0, 'c')
print(a, "  - .insert(0, 'c')")

# remove
a.remove('c')
print(a, "  - .remove('c')")

# pop
pop_val = a.pop(1)
print(f"{a}  - popped = {pop_val}")

# append
a.append('d')
print(a, "  - .append('d')")

# index
idx = a.index('d')
print(f"{a.index('d')}  - index('d') = {idx}")

# count
cnt = a.count('d')
print(f"{a.count('d')}  - count('d') = {cnt}")

# reverse
a.reverse()
print(a, "  - reversed(a)")

# copy
a_copy = a.copy()
print(a.copy(), f"  - copy() = {a_copy}")


# Kartezh
print("--------------------------------------------------------Kartezhi")

b = ('b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# count
print(b.count('f'), "  - count('f')")

# index
print(b.index('h'), "  - index('h')")

# concatenation
b += ('5', '2')
print(b, "  - extended tuple (+=)")


# Slovar
print("---------------------------------------------------------Slovari")
c = {}

# update
c.update({'a': 1, 'b': 2})
c['c'] = 3
print(c, "  - update()")

# get
print(c.get('a'), "  - get('a')")

# keys, values, items
print(c.keys(), "  - keys()")
print(c.values(), "  - values()")
print(c.items(), "  - items()")

# update
c.update({'a': a, 'b': 'b'})
print(c, "  - update()")

# pop
popped_b = c.pop('b', ['b'])
print(f"{c}  - popped 'b' = {popped_b}")

# popitem
popped_item = c.popitem()
print(f"{c}  - popped item = {popped_item}")

# copy
print(c.copy(), "  - copy()")

# clear
c.clear()
print(c, "  - clear()")



# mnozhestva
print("----------------------------------------------------mnozhestva")
s = {1, 2, 3, 4, 5}
print(s)

# add
s.add(6)
print(s, "  - .add(6)")

# remove
s.remove(6)
print(s, "  - .remove(6)")

# discard
s.discard(10)
print(s, "  - .discard(10)")

# pop
popped_elem = s.pop()
print(f"{s}  - popped = {popped_elem}")

# clear
s_copy_clear = s.copy()
s_copy_clear.clear()
print(s_copy_clear, "  - clear()")

# copy
s_copy = s.copy()
print(s_copy, "  - copy()")