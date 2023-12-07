def columnWithMaxZeros(arr, N):
    maxZeros = 0
    indx = -1
    for i in range(N):
        currentCount = 0
        for j in range(N):
            if arr[j][i] == 0:
                currentCount += 1
        if currentCount > maxZeros:
            maxZeros = currentCount
            indx = i
            if maxZeros == N:
                break
    return indx

N=3
arr=[[0,1,0],[1,0,1],[0,1,1]]
ans=columnWithMaxZeros(arr, N)
print(ans)