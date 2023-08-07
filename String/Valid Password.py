class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        password = ''.join(A)
        print(password)
        if not any(i.isdigit() for i in password):
            return 0
        if not  8 <= len(password) <=15:
            return 0
        if not any (i.islower() for i in password):
            return 0
        if not any (i.isupper for i in password):
            return 0
        if not any(char in ['@', '#', '%,' '&', '!', '$', '*'] for char in password):
            return 0
        return 1
    
print(Solution().solve(["M%trWIvSAP47"]))