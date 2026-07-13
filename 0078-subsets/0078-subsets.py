class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def back(start,comb):
            result.append(comb[:])
        
            for i in range(start,len(nums)):
                comb.append(nums[i])
                back(i+1,comb)
                comb.pop()
        
        back(0,[])
        return result