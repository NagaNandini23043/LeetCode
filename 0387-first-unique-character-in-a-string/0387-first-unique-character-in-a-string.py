class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashMap={}
        for i in s:
            hashMap[i]=hashMap.get(i,0)+1
        
        for i in range(len(s)):
            if hashMap[s[i]]==1:
                return i
        else:
            return -1

