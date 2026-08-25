class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        R={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)):
            cur=R[s[i]]
            next_val=R[s[i+1]] if i+1<len(s) else 0
            if cur<next_val:
                result-=cur
            else:
                result+=cur
        return result