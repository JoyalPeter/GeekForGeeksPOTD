def sumTriangles(matrix, n): 
        sumUpper=0
        sumLower=0
        for i in range(n):
            sumLower+=sum(matrix[i][:i+1])
            sumUpper+=sum(matrix[i][i:])

        return [sumUpper,sumLower]

n=3
matrix=[[6, 5, 4], [1, 2, 5], [7, 9, 7]]
ans=sumTriangles(matrix,n)
print(ans)