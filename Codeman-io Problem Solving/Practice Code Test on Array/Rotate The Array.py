class Solutions:
    def rotate_the_array(self, K, arr):
        n = len(arr)
        if K == 0:
            temp = arr[n - 1]
            for i in range(n - 1, 0, -1):
                arr[i] = arr[i - 1]
            arr[0] = temp
        elif K == 1:
            temp = arr[0]
            for i in range(1, n):
                arr[i - 1] = arr[i]
            arr[n - 1] = temp
        
        return arr    

print(Solutions().rotate_the_array(1, [1, 2, 3, 4]))        

N, K = map(int, input().split())
arr = list(map(int, input().split()))[:N]
print(Solutions().rotate_the_array(K,arr))