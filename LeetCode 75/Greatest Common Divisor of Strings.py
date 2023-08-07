class Solution(object):
    def gcdOfStrings(self,str1, str2) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        if str1 == str2:
            return str1
        i = 1
        while i < len(str2):
            if str2[i] == str1[i]:
                i+=1
        if i == len(str2):
            return str2        
            
        # if str(str1).startswith(str2):
        #     return str1[:int(if(len(str2)%2==0))]

        # def gcd(a, b):
        #     while a:
        #         print(a,b)
        #         a, b = b, a % b
        #     return a
        
        # one =  str1[:gcd(len(str1), len(str2))]
        # two = str2[:gcd(len(str2), len(str1))]
        # print(one,two)


# print(Solution().gcdOfStrings("ABCABC", "ABC"))

# print(Solution().gcdOfStrings("ABABAB", "ABAB"))

print(Solution().gcdOfStrings("ABABAB", "ABAB"))

# print(Solution().gcdOfStrings("LEET", "CODE"))