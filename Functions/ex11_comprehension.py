nums1 = [10, 20, 31, 40, 51, 60, 70]

# nums2 will contain the values in nums1
# transformed (integer divided by 10)
nums2 = [x//10 for x in nums1]

# nums3 will contain the values in nums1
# that are filtered (only even numbers)
nums3 = [x for x in nums1 if x % 2 == 0]


# find the largest uneven number
print(max([x for x in nums1 if x % 2 != 0]))

# generator <~> allows iteration witohut creating a copy
print(max(x for x in nums1 if x % 2 != 0))