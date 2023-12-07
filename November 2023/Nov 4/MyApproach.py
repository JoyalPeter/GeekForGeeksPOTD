def transitionPoint( arr, n): 
        # Code here
        if 0 not in arr:
            return 0
        try:
            return arr.index(1)
        except ValueError:
            return -1

n = 5
arr= [0,0,0,1,1]
ans=transitionPoint( arr, n)
print(ans)