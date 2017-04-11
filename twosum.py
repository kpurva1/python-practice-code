
#Given an array of integers, return indices of the two numbers such that they add up to a specific target. Given nums = [2, 7, 11, 15], target = 9,Because nums[0] + nums[1] = 2 + 7 = 9,return [0, 1].
#space complexity O(1), time complexity O(n2)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range (0,len(nums)-1):
            for y in range (x+1,len(nums)):
                if (nums[x] + nums[y]) == target:
                    return [x,y]
 


#another solution using dictionary
#space complexity O(n), time complexity O(n)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = dict()
        for i in range (len(nums)):
            if nums[i] in hm:
                return (hm[nums[i]],i)
            hm[target - nums[i]] = i;
        
            
