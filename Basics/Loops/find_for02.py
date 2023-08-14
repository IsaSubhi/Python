names = ['moshe', 'david', 'shlomo', 'lea']

while True:
    name_to_find = input("enter name to find:")

    is_name_found = False
    for name in names:
        if name_to_find == name:
            is_name_found = True
            break

    if is_name_found:
        print("found")
    else:
        print("not found")




