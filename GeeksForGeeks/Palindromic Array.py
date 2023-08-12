def PalinArray(arr ,n):
    for i in range(n):
        if str(arr[i])!= str(arr[i])[::-1]:
            return 0
    return 1
print(PalinArray([121, 131, 20], 3))