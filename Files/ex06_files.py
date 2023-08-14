name_file = open("name.txt")
value_file = open("value.txt")

name = name_file.read()
value = int(value_file.read())

print(f"the name is {name} and the value / 10 is {value/10}")

name_file.close()
value_file.close()


