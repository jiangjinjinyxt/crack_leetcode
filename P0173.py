"""
problem 173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/

solution:

""" 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.iterator = self.helper(root)
        def count_length(node):
            if not node:
                return 0
            else:
                return 1 + count_length(node.left) + count_length(node.right)
        self.length = count_length(root)

    def helper(self, node):
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.val
                node = node.right

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.length -= 1
        return next(self.iterator)

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.length > 0

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        value = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return value

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.stack else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()