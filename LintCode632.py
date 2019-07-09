"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        # Write your code here
        if root == None:
            return None
        left = self.maxNode(root.left)
        right = self.maxNode(root.right)
        return self.max(root, self.max(left, right))

    def max(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.val > right.val:
            return left
        else:
            return right


