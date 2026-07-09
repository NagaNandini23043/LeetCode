class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)

        while b!=0:
            c=a & b
            a= a ^ b
            b=c << 1
        
        return bin(a)[2:]