"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """

    def leafSum(self, root):
        # write your code here

        if root == None:
            return 0

        leftsum = self.leafSum(root.left)
        rightsum = self.leafSum(root.right)
        if root.left == None and root.right == None:
            return root.val
        return leftsum + rightsum
