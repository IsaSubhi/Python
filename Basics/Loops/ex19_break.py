x = [1221, 3221, 43345, 447, 4544, 5454323, 32235]
# x = [1221, 3221, 43345, 447, 4543, 5454323, 32235]

# print "HAS EVEN" if the list contains an even number
# else print "NO EVEN"

for num in x:
    if num % 2 == 0:
        print("list has an even number")
        break
# else: we didn't break and the loop ended
else:
    print("list doesn't have an even number")


