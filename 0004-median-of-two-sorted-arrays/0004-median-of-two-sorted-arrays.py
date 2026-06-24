class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums=nums1+nums2
        nums.sort()
        n=len(nums)
        ind = n//2
        res = 0
        if n%2==0:
            res=(nums[ind-1]+nums[ind])/2.0
            return res
        else:
            return nums[ind]
    
        