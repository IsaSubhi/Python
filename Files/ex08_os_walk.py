import os

DIR = 'sample'

for d, dirs, files in os.walk(DIR):
    print(*files)


s = 0
for d, dirs, files in os.walk(DIR):
    s += len(files)

print(f"there are {s} non-directory files")
