# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev=None
        self.minimum=float('inf')

        def inorder(root):
            if root is None:
                return
            
            inorder(root.left)

            if self.prev is not None:
                self.minimum=min(self.minimum, root.val-self.prev)
            
            self.prev=root.val

            inorder(root.right)
            
        inorder(root)
        return self.minimum

        