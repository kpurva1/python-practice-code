# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321 

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = str(x)
        if x < 0:
            a= int('-'+y[:0:-1])
            if a < -2147483648:
                return (0)
            else:
                return (a)
        else:
            a = int (y[::-1])
            if a < 2147483649:
                return (a)
            else:
                return (0)
        
