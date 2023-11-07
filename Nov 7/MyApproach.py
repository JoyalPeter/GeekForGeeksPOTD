def sumTriangles(matrix, n): 
        sumUpper=0
        sumLower=0
        for i in range(n):
            for j in range(n):
                if j<=i:                    # check condition as if(i==j) add in both elif(j<i) add in lower else add in upper
                    sumLower+=matrix[i][j]
                      
                if j>=i:
                    sumUpper+=matrix[i][j]

        return [sumUpper,sumLower]

n=3
matrix=[[6, 5, 4], [1, 2, 5], [7, 9, 7]]
ans=sumTriangles(matrix,n)
print(ans)