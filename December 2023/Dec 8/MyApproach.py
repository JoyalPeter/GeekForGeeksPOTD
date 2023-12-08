import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def minNumber(arr, n):
    i = 0
    num = sum(arr)
    while True:
        if isPrime(num + i):
            return i
        else:
            i += 1

print(minNumber([2, 4, 6, 8, 12],5))
