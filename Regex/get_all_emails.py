import re

file = open("data.txt")
text = file.read()

# emails = re.findall(r'\w+@\w+\.\w+', text)
emails = re.findall(r'(?:\w+\.)*\w+@(?:\w+\.)+\w+', text)

for email in emails:
    print(email)

for match in  re.finditer(r'((?:\w+\.)*\w+)@((?:\w+\.)+\w+)', text):
    print("email:{}, name:{}, domain:{}".format(
        match.group(), match.group(1), match.group(2)
    ))

