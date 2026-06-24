class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        
        INT_MAX=2**31-1
        INT_MIN=-2**31

        i=0
        n=len(s)

        while i<n and s[i]==" ":
            i+=1
        
        if i==n:
            return 0

        sign=1
        if s[i]=='+':
            i+=1
        elif s[i]=='-':
            sign=-1
            i+=1
        
        result=0
        while i<n and s[i].isdigit():
            digit=int(s[i])
            result=result*10 + digit

            if sign *result<=INT_MIN:
                return INT_MIN
            if sign*result>=INT_MAX:
                return INT_MAX
            i+=1

        return result*sign
            