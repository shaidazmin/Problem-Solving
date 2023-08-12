def addMatrices(matrixA, matrixB):
    n = len(matrixA)
    result = [[0] * n for _ in range(n)]
    print(result)
    
    for i in range(n):
        for j in range(n):
            result[i][j] = matrixA[i][j] + matrixB[i][j]
    
    # Print the result matrix (optional)
    for row in result:
        print(' '.join(map(str, row))) 

print(addMatrices([[1, 2], [3, 4]], [[4, 3], [2, 1]]))              