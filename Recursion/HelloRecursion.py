class Solution:

    # recursion number

    def print_recurstion_num(self, num):
        if num > 10:
            return 
        
        self.print_recurstion_num(num+1)
        print(num)

    # recursion Array

    def print_recurstion_arr(self, arr, start, end):
        if start > end:
            return
        print(arr[start])
        self.print_recurstion_arr(arr,start+1, end)
        
    # recursion Array Sum

    def print_recurstion_arr_sum(self, arr, start, end):
        if start > end:
            return arr[end]
        
        return arr[start] + self.print_recurstion_arr_sum(arr, start+1, end)
   
    # recursion factorial

    def print_recurstion_factorial(self, num):
        if num == 0:
            return 1
        
        return num * self.print_recurstion_factorial(num - 1)
    
    # recursion max value from Array

    def print_recursion_max_in_array(self, array, start, end):
        if start > end :
            return array[end]
        
        return max(array[start], self.print_recursion_max_in_array(array, start+1, end))
    
    # recursion palindrom

    def print_recursion_palindrome(self, st):
        





# print(Solution().print_recurstion_num(1))
# print(Solution().print_recurstion_arr_sum([1,5,3,5,7], 0 , 4))
# print(Solution().print_recurstion_factorial(5))
print(Solution().print_recursion_max_in_array([100,2,505,3,25,7], 0 , 5))