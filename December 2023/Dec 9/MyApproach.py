import math

def digitSum(n):
    s=0
    while(n):
        s+=n%10
        n=n//10
    return s
    
def smithNum( n):
    if n==1:
        return 0
    
    #sieve of eratosthenes
    primes = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (primes[p] == True): 
            for i in range(p * p, n+1, p): 
                primes[i] = False
        p += 1
    
    #if n is prime
    if primes[n]: 
        return 0
        
    sumOfDigits=digitSum(n)    
    primeFactors=[i for i in range(2,len(primes)) if primes[i] and n%i==0]
    sumOfFactors=0
    
    for i in primeFactors:
        if i>10:
            sumOfDigitsI=digitSum(i)
        else:
            sumOfDigitsI=i
        temp=n
        #adding the number of times a prime appears as a factor
        while(temp%i==0):
            sumOfFactors+=sumOfDigitsI
            temp=temp//i
            if sumOfFactors>sumOfDigits:
                return 0
    
    if sumOfFactors==sumOfDigits:
        return 1
    else:
        return 0
    
print(smithNum(985))