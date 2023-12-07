def minDist( arr, n, x, y):
        if x not in arr or y not in arr:
            return -1 # return -1 if either x or y is absent
        
        minDist=abs(arr.index(x)-arr.index(y)) #initializing the distance as the difference of the first occurrence of x and y
        current=0 #store current variable x or y
        
        for i in range(n): # find whether x or y occurs first
            if arr[i]==x:
                startIndx=i
                current=x
                break
            if arr[i]==y:
                startIndx=i
                current=y
                break
            
        indx=startIndx
        
        #if current is not same as the array element(x or y), find distance and update minimum if needed 
        for i in range(startIndx+1,n): 
            if arr[i]==x:
                if current!=x:
                    dist=i-indx
                    minDist=min(minDist,dist)
                    current=x
                indx=i
            
            if arr[i]==y:
                if current!=y:
                    dist=i-indx
                    minDist=min(minDist,dist)
                    current=y
                indx=i

        return minDist

n=4
arr=[1 ,2 ,3 ,2]
x=1 
y=2
distance=minDist( arr, n, x, y)
print(distance)