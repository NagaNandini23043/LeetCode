class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative=False
        if x<0:
            is_negative=True
            x*=-1
        
        result=0
        while x>0:
            result=(result*10)+(x%10)
            x=x//10
        
        if result>2 ** 31 -1:
            return 0
        return result*-1 if is_negative else result
        