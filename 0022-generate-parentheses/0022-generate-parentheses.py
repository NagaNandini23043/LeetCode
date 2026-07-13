class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        open=0
        close=0
        result=[]
        s=""

        def backtrack(s,open,close):
            if open==close==n:
                result.append(s)
                return
            
            if open<n:
                backtrack(s+"(", open+1,close)
            if close<open:
                backtrack(s+")", open, close+1)
        
        backtrack(s,open,close)
        return result