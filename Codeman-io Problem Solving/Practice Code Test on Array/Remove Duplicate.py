class Solutions():
    def removeDuplicats(self,arr):
        if not arr:
            return []
    
        n = len(arr)
        index = 1
        for i in range(1, n):
            if arr[i] != arr[i - 1]:
                arr[index] = arr[i]
                print(arr[i], arr[i-1])
                index += 1
        return ' '.join(str(e) for e in arr[:index])



# N = int(input())
# nums = list(map(int, input().split()))[:N]
# result = Solutions().removeDuplicats(nums)
# print(result)

print(Solutions().removeDuplicats([1, 3, 3, 4]))

