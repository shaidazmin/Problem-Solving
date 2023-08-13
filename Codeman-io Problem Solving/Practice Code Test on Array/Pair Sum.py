class solutions:
    def pair_sum(self,  target, nums):
        seen = set()
        for num in nums:
            print(target - num, seen)
            if target - num in seen:
                return 'Yes'
            seen.add(num)
        return 'No'
    
print(solutions().pair_sum(5, [1, 2, 3, 4, 5,6]))


# N, M = map(int, input().split())
# nums = list(map(int, input().split()))[:N]
# print(solutions().pair_sum(M,nums))