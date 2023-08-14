# change the list so that each element is divided by 10
nums = [10, 20, 30, 40, 50]

print("before:", nums)

# FIX: iterate over the indexes and use x[i]= to change values
i = 0
while i < len(nums):
    nums[i] = nums[i] // 10
    i += 1

print("after :", nums)