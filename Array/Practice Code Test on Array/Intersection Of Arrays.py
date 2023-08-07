class Solutions:
    def intersectionOfArray(self, arr1, arr2):
        return ' '.join(str(e) for e in set(arr1) & set(arr2) )
# N, M = map(int, input().split())    
# arr1 = list(map(int, input().split()))[:N]
# arr2 = list(map(int, input().split()))[:M]


# print(Solutions().intersectionOfArray([1, 2, 3, 4, 5, 6], [1, 4, 3, 7]))

result = Solutions().intersectionOfArray([1, 2, 3, 4, 5, 6], [1, 4,3,7])
print(len(result.split(' ')))
print(result)

# print(Solutions().intersectionOfArray([1, 1, 3, 1,3], [1, 2, 3, 4, 5, 6]))