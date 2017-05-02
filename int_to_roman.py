# Given an integer, convert it to a roman numeral.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 4000:
            return (''.join(0))
        elif num < 1:
            return (''.join(0))
        
        convert = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        
        #print (convert)
        l = len(str(num))
        #print (l)
        a = []
        for i in range (l-1):
            rem = num%10
            a.append(rem)
            num = int(num/10)
        a.append(num)
        #print(a)
        roman = []
        for i in range (len(a)):
            if (a[i] < 4):
                for j in range (a[i]):
                    roman.append(convert.get(10**i))
            elif (a[i] == 4):
                #print ((4*(10**i))+(10**i))
                roman.append(convert.get((4*(10**i))+(10**i)))
                roman.append(convert.get(10 ** i))
            elif (a[i] == 5):
                roman.append(convert.get(5*(10**i)))
            elif (a[i] > 5 and a[i] < 9):
                less = a[i] - 5
                for j in range (less):
                    roman.append(convert.get(10 ** i))
                roman.append(convert.get(5*(10**i)))
        
            elif a[i] == 9:
                roman.append(convert.get(10 ** (i + 1)))
                roman.append(convert.get(10 ** i))
        #print (roman)
        return(''.join(roman[::-1]))
