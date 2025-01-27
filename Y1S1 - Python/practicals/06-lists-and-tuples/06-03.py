 # Write and test a function that determines if a given integer is a prime number. A
 # prime number is an integer greater than 1 that cannot be produced by multiplying
 # two other integers

def isPrime(inputNum):
    if inputNum < 2:
        return "Invalid input: number less than 2"
    for i in range(2, inputNum):
        if inputNum % i == 0:
            return False
    return True

print(isPrime(10))
print(isPrime(-10))
print(isPrime(20))
print(isPrime(300))