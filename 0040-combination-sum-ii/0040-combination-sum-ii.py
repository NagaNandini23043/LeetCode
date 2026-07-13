class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result=[]

        def back(start, comb, total):
            if total==target:
                result.append(comb[:])
                return
            
            if total>target:
                return
            
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue

                comb.append(candidates[i])
                back(i+1,comb,total+candidates[i])
                comb.pop()
        
        back(0,[],0)
        return result