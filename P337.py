# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rob(self, root):
	    """
	    :type root: TreeNode
	    :rtype
	    """
	    look_up = {None: 0}
	    return self.contain_root(root, look_up)

	def contain_root(self, root, look_up):
		if root in look_up:
			return look_up[root]
		else:
			value = max(root.val + self.not_contain_root(root.left, look_up) + self.not_contain_root(root.right, look_up),
				self.contain_root(root.left, look_up) + self.contain_root(root.right, look_up))
			look_up[root] = value
			return value
	def not_contain_root(self, root, look_up):
		if root is None:
			return 0
		else:
			return self.contain_root(root.left, look_up) + self.contain_root(root.right, look_up)