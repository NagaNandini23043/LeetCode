class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        for ch in digits:
            if ch=="0" or ch=="1":
                return []
        
        result=[]
        phone_num={'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':'tuv', '9':"wxyz"}

        def backtrack(start,comb):
            if start==len(digits):
                result.append(comb)
                return
            
            for ch in phone_num[digits[start]]:
                backtrack(start+1, comb+ch)
        
        backtrack(0,"")
        return result