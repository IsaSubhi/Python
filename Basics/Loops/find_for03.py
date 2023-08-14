names = ['moshe', 'david', 'shlomo', 'lea']

while True:
    name_to_find = input("enter name to find:")

    for name in names:
        if name_to_find == name:
            print("found")
            break
    else:
        print("not found")




