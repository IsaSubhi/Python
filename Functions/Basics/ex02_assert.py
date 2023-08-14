
# 0! -> 1
# 3! -> 1 * 2 * 3
def factorial(n):
    assert type(n) is int
    # if not(type(n) is int):
    #     raise AssertionError("type(n) is int")

    assert n >= 0

    result = 1
    for num in range(2,n+1):
        result *= num

    return result


print(factorial(5))
print(factorial(3))
print(factorial(8))

print(factorial("asdasd"))
print(factorial(-3))
