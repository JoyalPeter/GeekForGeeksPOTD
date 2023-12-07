def minimumStep ( n):
    shortestLength=0
    while(n>1):
        if(n%3==0):
            n=n//3
        else:
            n-=1
        shortestLength+=1
    return shortestLength

print(minimumStep(9))