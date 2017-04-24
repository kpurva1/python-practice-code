# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        sout = [''] * numRows

        #print (sout)
        idx = 0
        row = 0
        
        for x in s:
            sout[idx] += x
            if idx == 0:
                row = 1
            if idx == numRows - 1:
                row = -1
            idx += row
        return (''.join(sout))
