str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = '012123234345456567678789'
str3 = '010203040506070809'

'''
create a string vairable str4 that will be filled
as follows:
  * All the letters from str1 starting from the second letter,
    ending in one before last.
    
  * Add to str4 the slice from str2 for every third letter
    starting the second letter.
    
  * Add to str4 the slice from str3 for every second letter in
    reverse.
'''
str4 = str1[1:-1]
str4 += str2[1::3]
str4 += str3[::-2]

print(str4)


"""
Add to str4 the slice from str2 for every third letter (skip: 3)
    starting the second letter (start index: 1).
"""