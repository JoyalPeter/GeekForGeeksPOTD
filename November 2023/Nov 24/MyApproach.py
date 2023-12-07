def nthRowOfPascalTriangle(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    ans=[[1],[1,1]]
    mod=1000000007
    for i in range(3,n+1):
        ans.append([1])
        for j in range(len(ans[-2])-1):
            ans[-1].append((ans[-2][j]+ans[-2][j+1])%mod) #Use two arrays instead of storing all rows
        ans[-1].append(1)
    return ans[-1]


print(nthRowOfPascalTriangle(10))
