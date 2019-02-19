"""
problem 100: Same Tree
https://leetcode.com/problems/same-tree/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p:
        	if q:
        		if p.val == q.val:
        			return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        		else:
        			return False
        	else:
        		return False
       	else:
       		if q:
       			return False
       		else:
       			return True



# iterative
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_stack = [p]
        q_stack = [q]
        while p_stack and q_stack:
        	p = p_stack.pop()
        	q = q_stack.pop()
        	if p is None:
        		if q is None:
        			continue
        		else:
        			return False
        	else:
        		if q is None:
        			return False
        		if p.val == q.val:
        			p_stack.append(p.left)
        			p_stack.append(p.right)
        			q_stack.append(q.left)
        			q_stack.append(q.right)
        		else:
        			return False
        if p_stack or q_stack:
        	return False
        else:
        	return True




