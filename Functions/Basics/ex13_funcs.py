

def print_line(char, length, has_newline):
    print(char * length, end='')

    if has_newline:
        print()

# prints a rectangle of asterisks (*)
# with width w and height h
def print_rectangle(w, h):
    for row in range(h):
        print_line('*', w, True)



# MAIN:

print_line('*', 5, True)
print_line('~', 3, False)
print_line('#', 4, True)

print()

print_rectangle(13, 9)

"""
OUTPUT:
*****
~~~####
"""

