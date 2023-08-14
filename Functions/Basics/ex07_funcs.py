def average(numbers):
    return sum(numbers)/len(numbers)

# average(10, 20, 30) # bad
average(  [10, 20, 30] ) # ok
average(  (10, 20, 30) ) # ok
average((10, 20, 30)) # ok



