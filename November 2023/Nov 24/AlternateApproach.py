'''Intuition
Every element in the n-th row is of the form (n-1)C0,(n-1)C1.....(n-1)C(n-1)'''
def nthRowOfPascalTriangle(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    ans=[]
    mod = 1000000007
    for i in range(n):
        element=nCr(n-1,i)
        ans.append(element)
    return ans

def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

def nCr(n,r):
    if r==n or r==0:
        return 1
    if r==1:
        return n
    return factorial(n)//(factorial(r)*factorial(n-r))



print(nthRowOfPascalTriangle(10))
