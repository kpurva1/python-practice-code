# Implement atoi to convert a string to an integer.
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        l = len(str)
        l1 = l -1
        sign = 0
        num = 0
        k = 1
        cnt = 0
        for i in range(l):
            #print (str[i])
            if i == 0 and str[i] == '-' and l > 1:
                sign = 1
                l1 = l1-1
            elif i == 0 and str[i] == '+':
                sign = 0
                l1 = l1 -1
            elif str[i] not in ('0','1','2','3','4','5','6','7','8','9') or k < 1:
                k = 0
                cnt += 1
            else:
                k = int(str[i])
                num += k*(10**l1)
                if k == 0:
                    k =1
                l1 -= 1
        num = num / (10**cnt)
        if sign == 1:
            num = num * -1
            if num < -2147483648:
                num = -2147483648
        if num > 2147483647:
            num = 2147483647
        
        return (num)
