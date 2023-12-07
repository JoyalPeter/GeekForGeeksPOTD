#Function to return list of integers visited in snake pattern in matrix.
def snakePattern(matrix):
    snake=[]
    for i in range(len(matrix)):
        if i%2==0:
           snake.extend(matrix[i])
        else:
            snake.extend(reversed(matrix[i])) #instead of reversed, iterate from last to first
    return snake

matrix = [[45, 48, 54],
          [21, 89, 87],
          [70, 78, 15]]
ans=snakePattern(matrix)
print(ans)
