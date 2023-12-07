# Store the count at index as the number of times the original element has been added with P
def frequencyCount(arr, N, P):
        P+=1
        for i in arr:
            indx=i%P
            if indx<=N:
                arr[indx-1]+=P #indx+1 because of 1-based indexing
            
        for i in range(N):
            arr[i]=arr[i]//P

N=5
arr=[2,3,2,3,5]
P=5
frequencyCount(arr,N,P)
print(arr)