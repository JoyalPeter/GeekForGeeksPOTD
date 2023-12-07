# [Print Matrix in snake Pattern](https://www.geeksforgeeks.org/problems/print-matrix-in-snake-pattern-1587115621/1)
## Nov 8
### Easy

Given a matrix of size N x N. Print the elements of the matrix in the snake like pattern depicted below.

            10->20->30->40
                        |
                        v
            50<-60<-70<-80
            |
            v
            27->29->47->48
                        |
                        v
            50<-23<-32<-39

### Example 1:

#### Input:
N = 3 
matrix[][] = {{45, 48, 54},
             {21, 89, 87}
             {70, 78, 15}}

#### Output: 
45 48 54 87 89 21 70 78 15 

#### Explanation:
Matrix is as below:
45 48 54
21 89 87
70 78 15
Printing it in snake pattern will lead to 
the output as 45 48 54 87 89 21 70 78 15.

### Example 2:

#### Input:
N = 2
matrix[][] = {{1, 2},
              {3, 4}}

#### Output: 
1 2 4 3

#### Explanation:
Matrix is as below:
1 2 
3 4
Printing it in snake pattern will 
give output as 1 2 4 3.

### Your Task:
You don't need to read input or print anything. Complete the function snakePattern() that takes matrix as input parameter and returns a list of integers in order of the values visited in the snake pattern. 

Expected Time Complexity: O(N * N)
Expected Auxiliary Space: O(N * N) for the resultant list only.

### Constraints:
1 <= N <= 10**3
1 <= mat[i][j] <= 10**9