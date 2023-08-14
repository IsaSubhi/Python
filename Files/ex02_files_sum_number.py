"""
create a program that reads the local file
"numbers.txt" assume it contains a number in each line
and nothing else.
print the sum of those lines
"""

NUMBER_FILE = 'numbers.txt'

f = open(NUMBER_FILE)

# readlines returns a list of strings (they include the newline)
lines = f.readlines()

s = 0
for line in lines:
    num = float(line)
    s += num

print(s)
f.close()
