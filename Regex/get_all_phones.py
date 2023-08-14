import re

file = open("data.txt")
text = file.read()

phones = re.findall(r'[0-9]{2,3}-?[0-9]{7}', text)

for number in phones:
    print(number)


