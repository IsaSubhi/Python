nums = [10, 20, 30, 40, 50]


print("before:", nums)

# BAD: doesn't actually changes the cells of nums
# change the list so that each element is divided by 10
for n in nums:
    n = n // 10  # shortcut: n //= 10

print("after :", nums)