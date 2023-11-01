# create a dict storing the count of all elements
def frequencyCount(arr, N, P):
        arr2={i:0 for i in range(1,N+1)}
        for i in arr:
            if i<=N:
                arr2[i]+=1
        for i in range(1,N+1):
            arr[i-1]=arr2[i]

N=5
arr=[2,3,2,3,5]
P=5
frequencyCount(arr,N,P)
print(arr)