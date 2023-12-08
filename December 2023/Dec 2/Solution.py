def isRepresentingBST(arr, N):
    for i in range(N - 1):
        if arr[i] >= arr[i + 1]:
            return 0
    return 1

print(isRepresentingBST([2,4,5],3))
print(isRepresentingBST([2,4,1],3))