import sys

def decrement( n, arr):
    if n <= 0:
        arr.append(n)
        return
    arr.append(n)
    decrement(n - 5, arr)
    arr.append(n)

def pattern( N):
    sys.setrecursionlimit(10**5) #increase recursion limit
    if N <= 0:
        return [N]
    n = N
    arr = []
    decrement(n, arr)
    return arr

print(pattern(16))