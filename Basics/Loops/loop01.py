
BEGIN = 1
END = 10

i = BEGIN
while i < END:
    print(i, end=' ')
    i += 1

print()

i = BEGIN
while i < END:
    print(i, end=' ')
    i += 2
print()

i = BEGIN
while i < END:
    print(i, end=' ')
    i *= 2
print()

i = END
while i >= BEGIN:
    print(i, end=' ')
    i -= 1
print()


