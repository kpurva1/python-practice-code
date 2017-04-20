#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = nums1 + nums2
        nums3 = sorted(nums3)
        l = len(nums3)
        mid = int(l/2)
        print (mid)
        if l%2 == 1:
            return (nums3[mid])
        else:
            med = float(nums3[mid - 1] + nums3[mid])
            print (med)
            med = float(med/2)
            print (med)
            return med
