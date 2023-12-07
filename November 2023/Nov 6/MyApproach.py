#function that returns the sum of letters of houses at hop distance
def findHouseSum(mat,n,m,hop,i,j):
        houseSum=0
        iVals=[]
        jVals=[]
        for x in range(i-hop,i+hop+1): 
            if (x)>=0 and (x)<n: #checks if x is in bounds
                iVals.append(x)
        for y in range(j-hop,j+hop+1):
            if y>=0 and y<m:
                jVals.append(y)
        
        for x in iVals:
            for y in jVals:
                if x==i and y==j: # Current house is not to be added. Only neighbors
                    continue
                if hop==2:
                    if (x==i-1 or x==i+1 or x==i) and (y==j-1 or y==j+1 or y==j): #If hop is 2, we dont need to add houses at hop 1
                        continue
                    else:
                        houseSum+=mat[x][y]
                else:
                    
                    houseSum+=mat[x][y]
        return houseSum
        
def matrixSum( n, m, mat, q, queries):
    queryAnswers=[]
    for query in queries:
        hop=query[0]
        i=query[1]
        j=query[2]
        queryAnswers.append(findHouseSum(mat,n,m,hop,i,j))
    return queryAnswers

n = 4
m = 5
mat = [[1, 2, 3, 4, 10], 
       [5, 6, 7, 8, 10], 
       [9, 1, 3, 4, 10], 
       [1, 2, 3, 4, 10]]
q = 2
queries = [[1, 0, 1], 
           [2, 0, 1]]
ans=matrixSum(n, m, mat, q, queries)
print(ans)