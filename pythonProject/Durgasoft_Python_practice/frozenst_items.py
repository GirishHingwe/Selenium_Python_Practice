s = {10,20,30,40,50}
fs = frozenset(s)
print(type(fs))

for i in fs:
    print(i)

fs.add(60)
print(fs)