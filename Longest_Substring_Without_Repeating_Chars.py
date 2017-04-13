#Given a string, find the length of the longest substring without repeating characters
#Given "abcabcbb", the answer is "abc", which the length is 3.
#Given "bbbbb", the answer is "b", with the length of 1.
#Given "pwwkew", the answer is "wke", with the length of 3. 
#Note that the answer must be a substring, "pwke" is a subsequence and not a substring

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        ls = len (s)
        c1 =''
        s1 = ''
        maxlen = 0
        l1 =0
        i =0
        
        while i < ls:
            #print (i)
            c = s[i]
            if c not in c1:
                c1 = c1 +c
                l1 = l1 +1
            else:
                if l1>maxlen:
                    maxlen = l1
                    s1 = c1
                i = i-l1
                c1 = ''
                l1 = 0
            i = i +1
        if l1>maxlen:
            maxlen = l1
            s1 = c1    
        return maxlen
