import re

text = open("some.xml").read()

# tags = re.findall("<.*?>", text)
tags = re.findall("<[^>]*>", text)

for tag in tags:
    print(tag)

