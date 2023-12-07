#function that returns the sum of letters of houses at hop distance
def isValid(i,j,n,m):
    if(i >= 0 and j >= 0 and i < n and j < m):
        return True
    return False
def findHouseSum(mat,n,m,hop,i,j):
            sum = 0
            print("q",hop)
            # Calculate the indices for the top-left and the bottom-right corners of the submatrix
            il = i - hop
            jl = j - hop
            ir = i + hop
            jr = j + hop
            
            # Iterate over the rows of the submatrix
            for x in range(il,ir+1):
                # Check if the current index is valid, and if so, add the corresponding element to the sum
                if(isValid(x, jl, n, m)): 
                    sum += mat[x][jl]
                    
                if(isValid(x, jr, n, m)):
                    sum += mat[x][jr]
            
            
            # Iterate over the columns of the submatrix
            for x in range(jl+1,jr): # range so since jl and jr is already added  in above loop
                # Check if the current index is valid, and if so, add the corresponding element to the sum
                if(isValid(il, x, n, m)):
                    sum += mat[il][x]
                if(isValid(ir, x, n, m)):
                    sum += mat[ir][x]
            return sum
        
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