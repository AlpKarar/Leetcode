# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def helper(root, isLeft):
            if not root:
                return
            
            if not root.left and not root.right:
                if isLeft:
                    res[0] += root.val
                
                return
            
            helper(root.left, True)
            helper(root.right, False)
        
        helper(root, False)

        return res[0]