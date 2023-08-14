# change the list so that each element is divided by 10
nums = [10, 20, 30, 40, 50, 60]

print("before:", nums)

# FIX: iterate over the indexes and use x[i]= to change values

# 0 1 2 3 4  --> range(5)

#                 5
for i in range(len(nums)):
    nums[i] = nums[i] // 10

print("after :", nums)