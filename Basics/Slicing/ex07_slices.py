x = "Hello, World!"

print('0123456789')
print(x)

# indexing
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

# slicing
# [ START  : END ]    <- END is always not included
# x[ 0 : 5 ]  <-  from character in x[0] upto character in x[4]
print(x[0:5])
print(x[7:12])

print("----")
# [:END]  <- (starts from the "beginning") end not included
print(x[:5])
# [START:] <- until the "end" (including!)
print(x[5:])

# [START:END:SKIP/DIRECTION]
print(x[1:10])
print(x[1:10:2])

y = '0123456789'
print(y[3:8:2])

#    0123456789
z = 'ABCDEFGHIJK'
print(z[3:8:2])












