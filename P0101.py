"""
problem 101: Symmetric Tree
https://leetcode.com/problems/symmetric-tree/

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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def helper(node1, node2):
            if not node1:
                if not node2:
                    return True
                else:
                    return False
            else:
                if not node2:
                    return False
                else:
                    if node1.val == node2.val:
                        return helper(node1.left, node2.right) and helper(node1.right, node2.left)
                    else:
                        return False
        return helper(root.left, root.right)

# iterative
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_stack = [root]
        right_stack = [root]

        while left_stack and right_stack:
            node1 = left_stack.pop()
            node2 = right_stack.pop()
            if node1:
                if not node2:
                    return False
                else:
                    if node1.val == node2.val:
                        left_stack.append(node1.left)
                        left_stack.append(node1.right)
                        right_stack.append(node2.right)
                        right_stack.append(node2.left)
                    else:
                        return False
            else:
                if node2:
                    return False
                else:
                    return True

        if left_stack or right_stack:
            return False
        else:
            return True
