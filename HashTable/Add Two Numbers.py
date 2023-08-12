class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # l1 = ''.join(str(n) for n in l1[::-1])
        # l2 = ''.join(str(n) for n in l2[::-1])
        # res = str(int(l1)+int(l2))[::-1]
        
        # print([i for i in (str(int(''.join(str(n) for n in l1[::-1]))+int(''.join(str(n) for n in l2[::-1])))[::-1])])
        # print([','.join(str(e) for e in str(int(l1)+int(l2))[::-1])])

        return [i for i in (str(int(''.join(str(n) for n in l1[::-1]))+int(''.join(str(n) for n in l2[::-1])))[::-1])]

        # return [','.join(str(int(''.join(str(n) for n in l1[::-1]))+int(''.join(str(n) for n in l2[::-1])))[::-1])]

     


print(Solution().addTwoNumbers([2,4,3], [5,6,4]))        
