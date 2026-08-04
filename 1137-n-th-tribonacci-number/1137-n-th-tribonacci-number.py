class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tab=[0]*(n+1)
        if n>0:
            tab[1]=1
        if n>1:
            tab[2]=1
        
        if n>=3:
            for i in range(3,n+1):
                tab[i]=tab[i-1]+tab[i-2]+tab[i-3]
        
        return tab[n]
        