 #Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

#For example,
#Given nums = [0, 1, 3] return 2. 

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 and nums[0] == 1:
            return 0
        nums = sorted(nums)
        if nums[0] != 0:
            return 0
        for i in range (len(nums) -1 ):
            if nums[i] + 1 != nums[i+1]:
                return nums[i]+1
                
        return nums[len(nums)-1]+1
