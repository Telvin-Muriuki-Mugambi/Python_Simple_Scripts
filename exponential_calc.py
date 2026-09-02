# A function that returns the exponential result of 2 positive digits
def power_loop(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

print(power_loop(5, 5))  
print(5**5)

