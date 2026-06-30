class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        water=0
        leftMax=0
        rightMax=0
        while left<right:
            leftMax=max(leftMax, height[left])
            rightMax=max(rightMax, height[right])

            if leftMax<rightMax:
                water+=leftMax-height[left]
                left+=1
            else:
                water+=rightMax-height[right]
                right-=1
        return water

