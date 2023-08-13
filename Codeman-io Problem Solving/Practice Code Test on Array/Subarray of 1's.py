class Solutions:
    def sub_array(self, nums):
        max_sum = 0
        curr_sum = 0
        for num in nums:
            if num == 1:
                curr_sum +=1
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = 0
        return max_sum
    

# print(Solutions().sub_array([0, 1, 0, 1, 1, 0]))    

N = int(input())    
nums = list(map(int, input().split()))[:N]
print(Solutions().sub_array(nums))