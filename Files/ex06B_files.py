
f = open("name.txt")
name = f.read()
f.close()

f = open("value.txt")
value = int(f.read())
f.close()

print(f"the name is {name} and the value / 10 is {value/10}")



