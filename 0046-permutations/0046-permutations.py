class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        if len(nums)==1:
            return [nums[:]]
        
        for _ in range(len(nums)):
            n=nums.pop(0)
            per=self.permute(nums)
            for p in per:
                p.append(n)
            result.extend(per)
            nums.append(n)
        return result



