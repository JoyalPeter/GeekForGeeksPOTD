''' The idea is to use the Sieve of Eratosthenes to pre compute prime numbers up to a certain limit'''

def findPrime(n):
    num = n + 1
    while num:
        if isPrime[num]:
            return num
        num += 1
    return 0


def minNumber(arr, n):
    sum_val = sum(arr)
    if isPrime[sum_val]:
        return 0
    num = findPrime(sum_val)
    return num - sum_val


MAX = 1000005
isPrime = [True] * 1000005
isPrime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if isPrime[i]:
        for j in range(2 * i, MAX, i):
            isPrime[j] = False

print(minNumber([2, 4, 6, 8, 12], 5))
