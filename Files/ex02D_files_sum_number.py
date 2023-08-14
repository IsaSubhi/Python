"""
create a program that reads the local file
"numbers.txt" assume it contains a number in each line
and nothing else.
print the sum of those lines
"""

NUMBER_FILE = 'numbers.txt'

f = open(NUMBER_FILE)
s = 0
for line in f:
    s += float(line)

print(s)
f.close()
f.readlines()
