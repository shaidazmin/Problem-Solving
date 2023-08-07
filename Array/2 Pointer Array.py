class Solution(object):
    def moveZeroes(self, nums):
        # Soluation 1
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                print(l,r)

        # Soluation 2
       
        # l = 0
        # r = 0
        # while r < len(nums):
        #     if nums[r]:
        #         print(r)
        #         nums[l], nums[r] = nums[r], nums[l]
        #         l+=1
        #     r+=1 
        return nums   
            
print(Solution().moveZeroes([0,1,0,3,12])  )  