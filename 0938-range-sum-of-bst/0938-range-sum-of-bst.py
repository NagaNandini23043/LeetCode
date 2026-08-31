# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return 0
        sum=0
        if low<=root.val<=high:
            sum+=root.val
        
        sum+=self.rangeSumBST(root.left,low,high)
        sum+=self.rangeSumBST(root.right,low,high)

        return sum
