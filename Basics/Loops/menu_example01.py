print("""
Title:
------
1) Action One
2) Action Two
3) Action Three
0) Quit
""")

option = input("enter option:")

if option == '1':
    print("PERFORMING ACTION ONE...")
elif option == '2':
    print("PERFORMING ACTION TWO...")
elif option == '3':
    print("PERFORMING ACTION THREE...")
elif option == '0':
    print("Goodbye")
else:
    print("error. invalid option.")

print("end of menu")
