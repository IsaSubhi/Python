
def print_line(char, length, has_newline):
    print(char * length, end='')

    if has_newline:
        print()


# MAIN:

print_line('*', 5, True)
print_line('~', 3, False)
print_line('#', 4, True)

"""
OUTPUT:
*****
~~~####
"""

