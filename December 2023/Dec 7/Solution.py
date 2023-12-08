def countSubarrays(a, n, L, R):
    subCount = 0

    # find all subarrays with elements less than the limit
    subArrLen = 0
    for i in a:
        if i > R:
            subCount += (
                subArrLen * (subArrLen + 1)
            ) // 2  # no of subarrays is n(n+1)/2 (triangle numbers).
            subArrLen = 0
        else:
            subArrLen += 1
    subCount += (subArrLen * (subArrLen + 1)) // 2

    # reduce the no of subarrays formed by elements less than lower limit
    lowersArr = 0
    for i in a:
        if i < L:
            lowersArr += 1
        else:
            subCount -= (lowersArr * (lowersArr + 1)) // 2
            lowersArr = 0
    subCount -= (lowersArr * (lowersArr + 1)) // 2

    return subCount


print(countSubarrays([2, 0, 11, 3, 0],5,1,10))
