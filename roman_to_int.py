#Given a roman numeral, convert it to an integer.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        i = 0
        num1 = 0
        while i < (len(s)):
            num = convert.get(s[i])
            if (i < (len(s)-1)):
                if (convert.get(s[i]) < convert.get(s[i+1])):
                    num = num * -1
                else:
                    num = num * 1
            num1 += num
            i += 1
        
        return num1
