x = [1221, 3221, 43345, 447, 4544, 5454323, 32235]
# x = [1221, 3221, 43345, 447, 4543, 5454323, 32235]

# print "HAS EVEN" if the list contains an even number
# else print "NO EVEN"

has_even = False

for num in x:
    if num % 2 == 0:
        has_even = True
        break

if has_even:
    print("HAS EVEN")
else:
    print("NO EVEN")

