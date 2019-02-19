"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left is None:
            if root.right is None:
                return 1
            else:
                return 1 + self.minDepth(root.right)
        else:
            if root.right is None:
                return 1 + self.minDepth(root.left)
            else:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# iterative
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        stack = []
        if root:
            stack.append(root)
        flag = True
        while stack and flag:
            height += 1
            size = len(stack)
            while size:
                size -= 1
                node = stack.pop(0)
                if node.left is None and node.right is None:
                    flag = False
                    break
                else:
                    if node.left is not None:
                        stack.append(node.left)
                    if node.right is not None:
                        stack.append(node.right)
        return height