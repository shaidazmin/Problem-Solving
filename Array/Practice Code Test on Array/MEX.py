class Solutions:
    def find_minimum_non_negative(self, nums):
        prsent = set(nums)
        print(len(nums))
        for i in range(0, len(nums)):
            if i not in prsent:
                return i
    
print(Solutions().find_minimum_non_negative([1, 2, 0, 4, 4 ,6]))    

# N = int(input())
# nums = list(map(int, input().split))[:N]
# print(Solutions().find_minimum_non_negative(nums))