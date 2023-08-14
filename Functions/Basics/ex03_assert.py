
# 0! -> 1
# 3! -> 1 * 2 * 3
def factorial(n):
    assert type(n) is int, "n must be an integer"
    # if not(type(n) is int):
    #     raise AssertionError("n must be an integer")
    
    assert n >= 0, "n must be 0 or higher"

    result = 1
    for num in range(2,n+1):
        result *= num

    return result


print(factorial(5))
print(factorial(3))
print(factorial(8))

# print(factorial("asdasd"))
print(factorial(-3))
