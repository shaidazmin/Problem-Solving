def countOfElements( a, n, x):
    count = 0
    for i in range(n):
        if a[i] <= x:
            count +=1
    return count        

print(countOfElements([1, 2, 4, 5, 8, 10], 6, 9))    