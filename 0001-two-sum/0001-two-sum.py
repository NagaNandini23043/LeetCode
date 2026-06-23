class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap={}
        for i,n in enumerate(nums):
            cd=target-n
            if cd in hashMap:
                return [hashMap[cd], i]
            hashMap[n]=i
        return