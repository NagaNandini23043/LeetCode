class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        def backtrack(start, comb):
            if sum(comb)==target:
                result.append(comb[:])
                return
            
            if sum(comb)>target:
                return
            
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(i,comb)
                comb.pop()
            
        backtrack(0,[])
        return result