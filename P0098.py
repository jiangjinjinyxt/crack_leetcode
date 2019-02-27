"""
problem 98: Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def helper(node, lower, upper):
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False
            if node.left:
                left = helper(node.left, lower, node.val)
            else:
                left = True
            if left:
                if node.right:
                    right = helper(node.right, node.val, upper)
                else:
                    right = True
                return right
            else:
                return False
        return helper(root, None, None)


# iterative
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [(root, None, None)]
        while stack:
            node, lower, upper = stack.pop()
            if node.right:
                if node.right.val > node.val:
                    if upper is not None and node.right.val >= upper:
                        return False
                    stack.append((node.right, node.val, upper))
                else:
                    return False
            if node.left:
                if node.left.val < node.val:
                    if lower is not None and node.left.val <= lower:
                        return False
                    stack.append((node.left, lower, node.val))
                else:
                    return False
        return True

# inorder
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
