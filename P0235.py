"""
Problem 235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

solution:

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# iterative
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_value = p.val
        q_value = q.val
        while True:
            if p_value > root.val:
                if q_value > root.val:
                    root = root.right
                else:
                    return root
            elif p_value < root.val:
                if q_value < root.val:
                    root = root.left
                else:
                    return root
            else:
                return root

# recursive
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val:
            if q.val <= root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val:
            if q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        else:
            return root