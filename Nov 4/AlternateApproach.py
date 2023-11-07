def transitionPoint( arr, n):
    if arr[0]==1:
        return 0
    lb = 0
    ub = n - 1
    # Perform Binary search
    while (lb <= ub):
        # Find mid 
        mid = (int)((lb + ub) / 2)
        
        # update lower_bound if 
    	# mid contains 0
        if (arr[mid] == 0):
            lb = mid + 1

        # If mid contains 1
        elif (arr[mid] == 1):
            
            # Check if it is the 
    		# left most 1 Return 
    		# mid, if yes
            if (arr[mid - 1] == 0): 
                return mid 
            
            # Else update 
    		# upper_bound 
            ub = mid-1
    return -1

n = 5
arr= [0,0,0,1,1]
ans=transitionPoint( arr, n)
print(ans)