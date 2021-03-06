#Find the largest palindrome made from the product of two n-digit numbers
#Since the result could be very large, you should return the largest palindrome mod 1337
#Input: 2, Output: 987 , Explanation: 99 x 91 = 9009, 9009 % 1337 = 987 

class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 10**n - 1
        maxpal = 0
        while x > 10**(n-1)-1:
            y = x-1
            while y > 10**(n-1)-1:
                p = x*y
                if str(p)==str(p)[::-1]:
                    if p > maxpal:
                        maxpal = p
                y = y -1
            x = x-1
        q = maxpal%1337
        return q
        
