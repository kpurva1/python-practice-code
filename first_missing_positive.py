 #Given an unsorted integer array, find the first missing positive integer.

#For example,
#Given [1,2,0] return 3,
#and [3,4,-1,1] return 2.

#Your algorithm should run in O(n) time and uses constant space. 

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] != 1 :
                return 1
            else:
                return nums[0]+1
        nums = sorted(nums)
        if 1 not in nums:
            return 1
        for i in range (len(nums)-1):
            if nums[i+1] != nums[i] +1 and nums[i+1] != nums[i]:
                if nums[i]+1 > 0:
                    return nums[i]+1
                
        return (nums[len(nums)-1]+1)
