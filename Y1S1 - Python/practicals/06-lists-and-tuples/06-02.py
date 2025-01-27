# Write and test a function that takes an integer as its parameter and returns the
#  factors of that integer. (A factor is an integer which can be multiplied by another to
#  yield the original)

def factors(inputNum):
    if inputNum < 0:
        return "Invalid input: negative number"
    factors = []
    for i in range(1, inputNum+1):
        if inputNum % i == 0:
            factors.append(i)
    return factors
    

print(factors(10))
print(factors(-10))
print(factors(20))
print(factors(300))