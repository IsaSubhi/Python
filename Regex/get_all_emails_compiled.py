import re

file = open("data.txt")
text = file.read()

all_emails_pattern = re.compile(r'(?:\w+\.)*\w+@(?:\w+\.)+\w+')

emails = all_emails_pattern.findall(text)

for email in emails:
    print(email)


